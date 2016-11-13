from twython import Twython

from kylejnovak import app

import requests
import json


CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)


def oauth_req(url):
    user_timeline = twitter.get_user_timeline(screen_name="KyleJosephNovak", count=5, include_retweets=False)
    print(user_timeline[0]['created_at'])
    return None


def get_twitter_recent_tweets():
    home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json')
