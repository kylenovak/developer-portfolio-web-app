from flask import Blueprint, render_template, Markup, g

from kylejnovak.services import github_api
from kylejnovak.services import twitter_api
from kylejnovak.views.home.services.home_service import HomeService

home_service = HomeService()

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/')
def home():
    welcome_content = home_service.get_welcome()

    if welcome_content is not None:
        welcome_content = Markup(welcome_content)

    recent_tweets = twitter_api.get_twitter_recent_tweets()
    starred_repos = github_api.get_github_starred_repos()

    return render_template('home.html',
                           welcome_text=welcome_content,
                           github_repos=starred_repos,
                           github_repos_length=len(starred_repos),
                           github_username=github_api.get_github_username(),
                           recent_tweets=recent_tweets,
                           recent_tweets_length=len(recent_tweets),
                           twitter_username=twitter_api.get_twitter_username())
