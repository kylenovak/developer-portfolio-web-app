from flask import Flask

from . import views as view
from .views.admin.admin_view import admin

from .database import db
from .services.login_manager import login_manager

import os


application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(application)
login_manager.init_app(application)
admin.init_app(application)

application.register_blueprint(view.home_page)
application.register_blueprint(view.about_page)
application.register_blueprint(view.contact_page)
application.register_blueprint(view.projects_page)
application.register_blueprint(view.resume_page)
application.register_blueprint(view.login_page)
application.register_blueprint(view.register_page)

# data to set before each request
from .services.before_requests import *
# import error handlers
from .services.error_handlers import *
