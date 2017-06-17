import tweepy
from constants import Constants 

auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

for source in Constants.feeds_to_watch:
    print(source)
    tweets = api.user_timeline(source)
    for tweet in tweets:
        text  = tweet.text
        print(text)