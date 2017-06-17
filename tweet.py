import tweepy
from constants import Constants 
from finder import Finder
auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)

api = tweepy.API(auth)
finder = Finder()

for source in Constants.feeds_to_watch:
    print(source)
    tweets = api.user_timeline(source)
    trump_related_tweets = finder.get_trump_related_tweets(tweets)
    for tweet in trump_related_tweets:
        print(tweet.text)