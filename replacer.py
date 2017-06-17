import re
class Replacer:
    def replace_trump_references(self, tweets):
        replaced_tweets = []
        for tweet in tweets:
            if 'Donald Trump' in tweet.text:
                tweet.text = re.sub(r'Donald Trump', 'Hillary Clinton', tweet.text)
            if 'realDonaldTrump' in tweet.text:
                tweet.text = re.sub(r'realDonaldTrump', 'realHillaryClinton', tweet.text)
            if 'Trump' in tweet.text:
                tweet.text = re.sub(r'Trump', 'Clinton', tweet.text)
            if 'Melania' in tweet.text:
                tweet.text = re.sub(r'Melania', 'Bill', tweet.text)
            if 'Ivanka' in tweet.text:
                tweet.text = re.sub(r'Ivanka', 'Chelsea', tweet.text)
            replaced_tweets.append(tweet)

        return replaced_tweets
    
    def clean_tweets(self, tweets, source):
        for tweet in tweets:
            tweet.text = re.sub(r'https:\/\/t.co\/.+\b', '', tweet.text)
            tweet.text = re.sub(r'…', '', tweet.text)
            tweet.text = re.sub(r'@', '', tweet.text)
            if len(tweet.text) < 135:
                tweet.text += ' -' + source
        return tweets