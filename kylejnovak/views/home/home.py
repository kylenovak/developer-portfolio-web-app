from flask import Blueprint, render_template

from kylejnovak.services import github_api
from kylejnovak.services import twitter_api

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/')
def home():
    recent_tweets = twitter_api.get_twitter_recent_tweets()
    starred_repos = github_api.get_github_starred_repos()
    return render_template('home.html',
                           github_repos=starred_repos,
                           github_repos_length=len(starred_repos),
                           github_username=github_api.get_github_username(),
                           recent_tweets=recent_tweets,
                           recent_tweets_length=len(recent_tweets),
                           twitter_username=twitter_api.get_twitter_username())
