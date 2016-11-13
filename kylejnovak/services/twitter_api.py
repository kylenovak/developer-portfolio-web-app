from twython import Twython

from kylejnovak import app


def get_twitter_username():
    return app.config['TWITTER_USERNAME']


def get_twitter_recent_tweets():
    recent_tweets = []

    CONSUMER_KEY = app.config['TWITTER_CONSUMER_KEY']
    CONSUMER_SECRET = app.config['TWITTER_CONSUMER_SECRET']
    ACCESS_TOKEN = app.config['TWITTER_ACCESS_TOKEN']
    ACCESS_SECRET = app.config['TWITTER_ACCESS_SECRET']

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    user_timeline = twitter.get_user_timeline(screen_name="KyleJosephNovak", count=5, include_retweets=False)
    for tweet in user_timeline:
        recent_tweet = dict()
        recent_tweet['text'] = tweet['text']
        recent_tweet['created_at'] = tweet['created_at']
        recent_tweets.append(recent_tweet)

    return recent_tweets
