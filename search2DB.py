"""
Author: Kevin Barasa
Phone : +254724778017
Email : kevin.barasa001@gmail.com
"""
from __future__ import absolute_import, print_function
import sys; 
from tweepy.streaming import StreamListener
from HTMLParser import HTMLParser
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json
import MySQLdb
import re
#Inialize connection
conn = MySQLdb.connect("localhost","root","","tweets")
conn.set_character_set('utf8')
c = conn.cursor()
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')
#Secrets input
consumer_key="2wkkossI2Ot5uu3zQhbRGT74P"
consumer_secret="iUFE8LBwqHxTmrAhnTyWXvlaaRdjbGbEI58SzdBhqACyQeNY3H"
access_token="3193849965-TwvvA6BH89Khsx7teCr8Go3rBm7n9HYsGsDtLQC"
access_token_secret="2s6Mh4BaTG043r9aqacvUkhOVNeBWcaJf1t5zfv9Yeykg"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        all_data = json.loads(HTMLParser().unescape(data))
        tags = ''
        name = all_data["user"]["name"]
        screen_name = all_data["user"]["screen_name"]
        tweet = all_data["text"]
        id_uniq = all_data["user"]["id"]
        profile_image_url = all_data["user"]["profile_image_url"]
        location = all_data["user"]["location"]
        lang = all_data["user"]["lang"]
        friends_count = all_data["user"]["friends_count"]
        followers_count = all_data["user"]["followers_count"]
        description = all_data["user"]["description"]
        favourites_count = all_data["user"]["favourites_count"]
        time_zone = all_data["user"]["time_zone"]
        statuses_count = all_data["user"]["statuses_count"]
        created_at = all_data["user"]["created_at"]
        #posted_from = all_data["coordinates"]
        composed_time = all_data["created_at"]
        favorite_count = all_data["favorite_count"]
        language = all_data["lang"]
        recipient_handle = all_data["in_reply_to_screen_name"]
        retweet_count = all_data["retweet_count"]
        c.execute("INSERT INTO uri (tags, name, screen_name, tweet, id_uniq, profile_image_url, location, lang, friends_count, followers_count, description, favourites_count, time_zone, statuses_count, created_at, composed_time, favorite_count, language, recipient_handle, retweet_count ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
            (tags, name, screen_name, tweet, id_uniq, profile_image_url, location, lang, friends_count, followers_count, description, favourites_count, time_zone, statuses_count, created_at, composed_time, favorite_count, language, recipient_handle, retweet_count))
        conn.commit()
        print((name,tweet,composed_time))
        return True


    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(locations = [33.91,-4.68,41.91,5.03])
    




