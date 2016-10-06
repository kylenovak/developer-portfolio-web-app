from flask import Flask

from . import views as view

from .services.database import db
from .services.login_manager import login_manager
from .services.admin.admin_view import admin

import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)
login_manager.init_app(app)
admin.init_app(app)

app.register_blueprint(view.home_page)
app.register_blueprint(view.about_page)
app.register_blueprint(view.contact_page)
app.register_blueprint(view.projects_page)
app.register_blueprint(view.resume_page)
app.register_blueprint(view.login_page)
app.register_blueprint(view.register_page)

# data to set before each request
from .services.before_requests import *
# import error handlers
from .services.error_handlers import *
