from kylejnovak.database import db
from kylejnovak.models.about import About


class AboutService(object):

    def __init__(self):
        self.query = db.session.query
        self.about = About

    def get_about(self):
        return self.query(self.about.content).first()
