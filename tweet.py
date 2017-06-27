import tweepy
import os
from constants import Constants 
from finder import Finder
from replacer import Replacer
from storage import Storage
from html_generator import HtmlGenerator
from image_generator import ImageGenerator
import subprocess

auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)

api = tweepy.API(auth)
finder = Finder()
replacer = Replacer()
storage = Storage()
generator = HtmlGenerator()
imgGenerator = ImageGenerator()

generator.generate('author', '10/22/1986', 'text')

storage.get_all_tweets()

for source in Constants.feeds_to_watch:
    print(source)
    last_read_id = storage.get_latest_read_tweet_id(source)
    try:
        tweets = api.user_timeline(screen_name = source, since_id=last_read_id)
    except tweepy.error.TweepError:
        tweets = []
        pass
    if tweets and len(tweets) > 0:
        storage.store_latest_tweet_id(source, tweets[0].id)
        trump_related_tweets = finder.get_trump_related_tweets(tweets)
        replaced_tweets = replacer.replace_trump_references(trump_related_tweets)
        cleaned_tweets = replacer.clean_tweets(replaced_tweets)
        for tweet in cleaned_tweets:
            created_at = tweet.created_at.strftime('%A, %B %d, %Y at %I:%M %p')
            author = tweet.author.name
            text = tweet.text

            html = generator.generate(author, created_at, text)
            imgGenerator.generate_image(html)
            try:
                print('Writing status ' + tweet.text)
                api.update_with_media('./pics/out.png')
            except tweepy.error.TweepError as err:
                print(err)
                pass

