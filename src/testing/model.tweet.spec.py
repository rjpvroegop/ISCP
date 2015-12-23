import unittest

from model.tweet import Tweet


class TestStringMethods(unittest.TestCase):

    # ---
    # - the test methods
    # ---

    def test_same(self):
        self.assertEqual(self.create_tweet, self.create_tweet)

    def test_different(self):
        self.assertNotEqual(self.create_tweet, self.create_tweet_different)

    def test_empty_text_tweet(self):
        empty_text = ""
        self.assertEqual(self.create_tweet_without_text().text, empty_text)

    def test_empty_user_tweet(self):
        anonymous = "anonymous"
        self.assertEqual(self.create_tweet_without_user().username, anonymous)

    def test_create_user_with_mood(self):
        self.assertEqual(self.create_tweet_without_mood().mood, self.create_tweet().mood)

    def test_tweet_no_argument(self):
        with self.assertRaises(TypeError):
            self.create_empty_tweet()

    def test_tweet_empty_data(self):
        self.assertEqual(
            self.create_tweet_without_text().text,
            self.create_tweet_without_data().text
        )
        self.assertEqual(
            self.create_tweet_without_user().username,
            self.create_tweet_without_data().username
        )

    # ---
    # - methods that we can test stuff from
    # ---

    def create_tweet(self):
        return Tweet({
            "user": {"name": "test user"},
            "text": "test text test text test text"
            # mood is set to 0 automatically
        })

    def create_tweet_different(self):
        return Tweet({
            "user": {"name": "test user"},
            "text": "test text test text test text 2"
            # mood is set to 0 automatically
        })

    def create_tweet_without_text(self):
        return Tweet({
            "user": {"name": "test user"},
        })

    def create_tweet_without_user(self):
        return Tweet({
            "text": "test text test text test text"
        })

    def create_tweet_without_mood(self):
        return Tweet({
            "user": {"name": "test user"},
            "text": "test text test text test text",
            "mood": 10
        })

    def create_tweet_without_data(self):
        return Tweet({})

    def create_empty_tweet(self):
        return Tweet()

    def create_wrong_tweet(self):
        return Tweet(None)

    def change_username(self, tweet):
        tweet.username = "something else"
        return tweet

    def change_mood(self, tweet):
        tweet.mood = "something else"
        return tweet

    def change_text(self, tweet):
        tweet.text = "something else"
        return tweet

if __name__ == '__main__':
    unittest.main()