from kylejnovak.database import db
from kylejnovak.models.bio import Bio


class BioService(object):

    def __init__(self):
        self.query = db.session.query
        self.bio = Bio

    def get_bio(self):
        return self.query(self.bio).first()
