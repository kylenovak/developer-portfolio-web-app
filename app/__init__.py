from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# import models
import app.models as models

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
