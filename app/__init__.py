from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['AUTHOR'] = 'Kyle J. Novak'
app.config['YEAR_APP_BUILT'] = 2016

db = SQLAlchemy(app)

# import models
import app.models as models

# data to set before each request
from app.before_requests import *

# import error handlers
from app.error_handlers import *

# import blueprints
import app.blueprints as bp
app.register_blueprint(bp.home_page)
app.register_blueprint(bp.admin_page)
app.register_blueprint(bp.about_page)
app.register_blueprint(bp.contact_page)
app.register_blueprint(bp.portfolio_page)
app.register_blueprint(bp.projects_page)
app.register_blueprint(bp.resume_page)
app.register_blueprint(bp.guestbook_page)
