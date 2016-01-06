import os; print(os.getcwd())
from view import TweetGui

class Main:
    def __init__(self):
        self.tweet_gui = TweetGui.TweetMenu()

Main()