from controller.DBManage.MongoAdapter import MongoAdapter
from controller.tweet_analyse.MoodAnalyser import MoodAnalyser
from model.tweet import Tweet


class TweetProcessor:
    mood_analyser = MoodAnalyser()
    mongo_adapter = MongoAdapter()
    db = mongo_adapter

    def process(self, tweet_json):
        # analyser returns model.tweet object
        self.analysed_tweet = self.mood_analyser.analyse(Tweet(tweet_json))

        # write to database:
        try:
            self.db.insert_one(self.analysed_tweet)
            self.analysed_tweet = None
            print(self.db.get_count())
        except:
            self.analysed_tweet = None
            print("Could not connect to database.")
            return False

        return True
