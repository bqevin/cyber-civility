from __future__ import absolute_import, print_function
import sys; 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json
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
        all_data = json.loads(data)
        #Write all data in a text file
        text_file = open("twitter_data.txt", "w")
        #Parse all_data as tring so it doen't throw object error
        text_file.write(str(all_data))
        print(all_data)
        return True
        

    def on_error(self, status):
        print(status)
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['python', 'javascript', 'ruby'])
    




