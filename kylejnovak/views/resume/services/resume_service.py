from kylejnovak.database import db
from kylejnovak.models.resume import Resume


class ResumeService(object):

    def __init__(self):
        self.query = db.session.query
        self.resume = Resume

    def get_resume(self):
        return self.query(self.resume).first()
