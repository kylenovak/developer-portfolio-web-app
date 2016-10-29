from datetime import datetime
from ..database import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    subtitle = db.Column(db.String(255), nullable=False)
    url_slug = db.Column(db.String(255), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return '<Project id {:d} {}>'.format(self.id, self.title)

    def __str__(self):
        return self.title
