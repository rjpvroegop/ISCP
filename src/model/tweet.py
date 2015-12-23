import sys


class Tweet:
    def __init__(self, tweet):
        try:
            self.username = tweet['user']['name']
        except KeyError:
            self.username = "anonymous"
            print("This tweet has no user, setting anonymous")
        except:
            print(sys.exc_info()[0])

        try:
            self.text = tweet['text']
        except KeyError:
            self.text = ""
            print("This tweet has no text. Left empty.")
        except:
            print(sys.exc_info()[0])

        self.mood = 0

    def __del__(self):
        # making ready for garbage collection
        # print('deleted tweet')
        pass
