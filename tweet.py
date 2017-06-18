import tweepy
import time
from constants import Constants 
from finder import Finder
from replacer import Replacer
from storage import Storage

auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)

api = tweepy.API(auth)
finder = Finder()
replacer = Replacer()
storage = Storage()

storage.get_all_tweets()

for source in Constants.feeds_to_watch:
    print(source)
    last_read_id = storage.get_latest_read_tweet_id(source)
    try:
        tweets = api.user_timeline(screen_name = source, since_id = last_read_id)
    except tweepy.error.TweepError:
        tweets = []
        pass
    if tweets and len(tweets) > 0:
        storage.store_latest_tweet_id(source, tweets[0].id)
        trump_related_tweets = finder.get_trump_related_tweets(tweets)
        replaced_tweets = replacer.replace_trump_references(trump_related_tweets)
        cleaned_tweets = replacer.clean_tweets(replaced_tweets, source)
        for tweet in cleaned_tweets:
            try:
                print('Writing status ' + tweet.text)
                api.update_status(tweet.text)
            except tweepy.error.TweepError as err:
                print(err)
                pass
