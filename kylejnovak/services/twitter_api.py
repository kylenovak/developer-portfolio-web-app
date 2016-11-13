from flask import Markup
from twython import Twython
from kylejnovak import app
import re


def get_twitter_username():
    return app.config['TWITTER_USERNAME']


def wrap_hashtags_in_html(tweet_text):
    hashtags = [text for text in tweet_text.split() if text.startswith('#')]
    wrap_hashtags = '|'.join(hashtags)
    regex = r'(((' + wrap_hashtags + ')\s*?)+)'
    return Markup(re.compile(regex, re.I).sub(r'<em class="green-text">\1</em>', tweet_text))


def get_twitter_recent_tweets():
    recent_tweets = []

    CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
    CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
    ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
    ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    user_timeline = twitter.get_user_timeline(screen_name="KyleJosephNovak", count=10, include_retweets=False)
    for tweet in user_timeline:
        recent_tweet = dict()
        recent_tweet['text'] = wrap_hashtags_in_html(tweet['text'])
        recent_tweet['created_at'] = tweet['created_at']
        recent_tweets.append(recent_tweet)

    return recent_tweets
