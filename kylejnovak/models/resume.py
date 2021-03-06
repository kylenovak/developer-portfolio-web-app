from datetime import datetime
from kylejnovak.database import db
from sqlalchemy.dialects.postgresql import JSON


class Resume(db.Model):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True)
    resume_content = db.Column(JSON, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return '<Resume id {:d}>'.format(self.id)

    def __str__(self):
        return self.content
