import sys
import threading
from TwitterAPI.TwitterError import TwitterRequestError, TwitterConnectionError
from controller.TwitterLib.TweetProcessor import TweetProcessor



class TwitterStreamThread(threading.Thread):

    processor = TweetProcessor()

    def __init__(self, number_to_add, search_word, api):
        threading.Thread.__init__(self)
        self.api = api
        self.search_word = search_word
        self.numbers_to_add = number_to_add

        # because we break the loop, exception gets raised.
        # If we break the loop ourselves, we set this to false to prevent
        # the user from see'ing the error
        self.loop_error = True

    def run(self):
        # start stream using TwitterAPI
        try:
            r = self.api.request('statuses/filter', {'track': self.search_word})
            for tweet_json in r.get_iterator():

                if not self.processor.process(tweet_json):
                    break

                # break if max tweets number is reached (user defined)
                if self.processor.db.get_count() >= self.numbers_to_add:
                    # Since we stop the loop ourselves, the exception does not need to work
                    # it will get called, but skips if his is false.
                    self.loop_error = False
                    break

        except TwitterRequestError:
            print("Twitter api credentials don't seem to be working.")
        except TwitterConnectionError:
            print("Could not connect to the internet. Please check your connection.")
        except:
            # If this is true, there was an exception.
            # If it was not, we stopped the loop ourselves.
            # Unfortunate, I didn't find a way to solve this proper.
            if self.loop_error:
                print("Could not start stream; Check connection\n" + sys.exc_info()[0])