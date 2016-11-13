import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False

    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True

    TWITTER_USERNAME = 'KyleJosephNovak'
    TWITTER_CONSUMER_KEY = 'jqbHkP4OTvX1HpBqROwjRr2AX'
    TWITTER_CONSUMER_SECRET = 'jQkfTqnJjs99TCl9WryhbrAHp9d3SQnjJNRC5Ra7Rv5CBjMxCO'
    TWITTER_ACCESS_TOKEN = '792891903016513536-qv5rVowHWx2L5AtQBzdbwckgH5YwJDt'
    TWITTER_ACCESS_SECRET = 'kFrVabKmVd2o4796IwdVlpY0jY3OqPudFrCiTicM8UoC8'

    GITHUB_USERNAME = 'kylenovak'
    GITHUB_API_TOKEN = 'e26ed3487b1fe28b2722abc8d431bc50a4627ea5'

    WTF_CSRF_SECRET_KEY = 's,XtdcQK4N]nQs&rCC&j1!oR.0FvMcsZ'
    SECRET_KEY = 'xTAJcB(pcH_Bdqti6OB;Isd0RZ=1+S_L'

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AUTHOR = 'Kyle J. Novak'

    YEAR_APP_BUILT = 2016


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
