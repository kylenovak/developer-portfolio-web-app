from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)


import app.models as models
admin = Admin(app, name='Kyle J. Novak', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(models.Project, db.session))


# data to set before each request
from app.before_requests import *

# import error handlers
from app.error_handlers import *

# import blueprints
import app.blueprints as bp
app.register_blueprint(bp.home_page)
app.register_blueprint(bp.about_page)
app.register_blueprint(bp.contact_page)
app.register_blueprint(bp.projects_page)
app.register_blueprint(bp.resume_page)
