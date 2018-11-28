from __future__ import absolute_import, print_function

import tweepy
#import pdb
import os
import datetime

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key        = os.environ['TWEEPY_CONSUMER_KEY']
consumer_secret     = os.environ['TWEEPY_CONSUMER_SECRET']

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token        = os.environ['TWEEPY_ACCESS_TOKEN']
access_token_secret = os.environ['TWEEPY_ACCESS_TOKEN_SECRET']

auth                = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api                 = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print("Hi! I am " + api.me().name + "! and time is: {}".format(datetime.datetime.now()))
print("We must show our last 5 tweets")

for item in tweepy.Cursor(api.user_timeline).items(5):
    print("******")
    print(item.text)

#pdb.set_trace()
