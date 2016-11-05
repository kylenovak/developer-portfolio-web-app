import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False

    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
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
