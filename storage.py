import sqlite3
from constants import Constants
class Storage:

    def __init__(self):
        self.create_tweet_table()
        self.create_source_name_rows()

    def store_latest_tweet_id(self, sourceName, tweet_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Tweet SET LastTweet = ? WHERE SourceName = ?', (tweet_id, sourceName ))
        conn.commit()
        conn.close()

    def get_latest_read_tweet_id(self, sourceName):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT LastTweet from Tweet where SourceName = ?', (sourceName,))
        last_read = 0
        for row in cursor:
            last_read = row[0]
        conn.close()
        return last_read

    def get_connection(self):
        return sqlite3.connect('tweets.db')

    def create_tweet_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Tweet (SourceName text NOT NULL UNIQUE, LastTweet integer)')
        conn.commit()
        conn.close()
    
    def create_source_name_rows(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        for sourceName in Constants.feeds_to_watch:
            cursor.execute('INSERT INTO Tweet(SourceName) SELECT ? WHERE NOT EXISTS(SELECT 1 FROM Tweet WHERE SourceName = ?);', (sourceName, sourceName))
        conn.commit()
        conn.close()

    def get_all_tweets(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * FROM Tweet'):
            print(row)