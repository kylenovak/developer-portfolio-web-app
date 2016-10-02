from kylejnovak import db
from datetime import datetime


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, content='', create_date='', update_date=''):
        self.content = content
        self.create_date = create_date
        self.update_date = update_date

    def __repr__(self):
        return '<Contact id {:d}>'.format(self.id)

    def __str__(self):
        return self.content
