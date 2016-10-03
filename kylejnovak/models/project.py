from datetime import datetime
from ..database import db
from sqlalchemy.ext.hybrid import hybrid_property


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    subtitle = db.Column(db.String(255))
    url_slug = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow())

    @hybrid_property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        if self.url_slug is None:
            self.url_slug = title.replace(' ', '-')
        self.title = title

    def __repr__(self):
        return '<Project id {:d} {}>'.format(self.id, self.title)

    def __str__(self):
        return self.title
