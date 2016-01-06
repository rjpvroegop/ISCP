import json
from TwitterAPI import TwitterAPI
from controller.TwitterLib.TweetProcessor import TweetProcessor
from controller.TwitterLib.TwitterStreamThread import TwitterStreamThread



class TweetStream:
    # default values
    search_word = 'happy'
    streaming = False

    # processor to process tweets (store, moodvalue etc.)
    processor = TweetProcessor()

    # get a dictionary with keys for the twitter api
    fr = open('src/controller/TwitterLib/twitter_api_keys.json')
    api_data = json.loads(fr.read())
    fr.close()

    # combine keys to create the OAUTH2 connection with Twitter, using the TwitterAPI
    api = TwitterAPI(api_data['consumer_key'], api_data['consumer_secret'],
                     api_data['access_token_key'], api_data['access_token_secret'])

    def __init__(self, tweet_gui):
        self.gui = tweet_gui

    def start_stream(self, tweets_to_add):
        max_tweets = tweets_to_add + self.processor.db.get_count()
        stream_thread = TwitterStreamThread(max_tweets, self.search_word, self.api)
        stream_thread.start()

    def set_search_word(self, search_word):
        self.search_word = search_word

    def change_collection(self, collection_name):
        self.processor.mongo_adapter.set_collection(collection_name)
