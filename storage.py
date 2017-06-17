import sqlite3
from constants import Constants
class Storage:

    def __init__(self):
       self.create_tweet_table()
       self.create_source_name_rows()

    def store_latest_tweet_id(self, sourceName, tweet_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute('UPDATE Tweet SET LastTweet = ? WHERE SourceName = ?', (sourceName, tweet_id))
        conn.commit()
        conn.close()

    def get_connection(self):
        return sqlite3.connect('tweets.db')

    def create_tweet_table(self):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute('CREATE TABLE IF NOT EXISTS Tweet (SourceName text NOT NULL UNIQUE, LastTweet integer)')
        except Exception as err:
            print(str(err))
        conn.commit()
        conn.close()
    
    def create_source_name_rows(self):
        conn = self.get_connection()
        c = conn.cursor()
        for sourceName in Constants.feeds_to_watch:
            c.execute('INSERT INTO Tweet(SourceName) SELECT ? WHERE NOT EXISTS(SELECT 1 FROM Tweet WHERE SourceName = ?);', (sourceName, sourceName))
        conn.commit()
        conn.close()