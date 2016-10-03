from flask import Flask


import os

from .database import db
from .users.auth import login_manager
from .admin import admin

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)
login_manager.init_app(app)
admin.init_app(app)

# data to set before each request
from .before_requests import *
# import error handlers
from .error_handlers import *

# import blueprints
from . import views as view
from .users.views.login.login import login_page
from .users.views.register.register import register_page
app.register_blueprint(view.home_page)
app.register_blueprint(view.about_page)
app.register_blueprint(view.contact_page)
app.register_blueprint(view.projects_page)
app.register_blueprint(view.resume_page)
app.register_blueprint(login_page)
app.register_blueprint(register_page)
