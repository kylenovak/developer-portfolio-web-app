from app import db
from datetime import datetime


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, title='', content='', create_date='', update_date=''):
        self.title = title
        self.content = content
        self.create_date = create_date
        self.update_date = update_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
