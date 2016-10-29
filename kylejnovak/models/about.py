from datetime import datetime
from ..database import db


class About(db.Model):
    __tablename__ = 'about'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return '<About id {:d}>'.format(self.id)

    def __str__(self):
        return self.content
