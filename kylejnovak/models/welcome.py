from datetime import datetime
from kylejnovak.database import db


class Welcome(db.Model):
    __tablename__ = 'welcome'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return '<Welcome id {:d}>'.format(self.id)

    def __str__(self):
        return self.content
