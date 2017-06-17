import sqlite3
from constants import Constants
class Storage:

    def __init__(self):
        self.conn = sqlite3.connect('tweets.db')
        # need to initialize table if it doesnt exist
        #need to initialize sources if they dont exist

    def store_latest_tweet_id(self, source, tweet_id):
        c = self.conn.cursor()