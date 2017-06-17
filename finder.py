class Finder:
    def get_trump_related_tweets(self, tweets):
        trump_related = []
        for tweet in tweets:
            if 'trump' in tweet.text.lower():
                trump_related.append(tweet)
        return trump_related