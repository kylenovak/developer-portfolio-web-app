from kylejnovak.database import db
from kylejnovak.models.welcome import Welcome


class HomeService(object):

    def __init__(self):
        self.query = db.session.query
        self.welcome = Welcome

    def get_welcome(self):
        return self.query(self.welcome).first()
