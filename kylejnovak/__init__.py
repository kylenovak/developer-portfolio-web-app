from flask import Flask
from flask_mail import Mail

from kylejnovak.database import db

import os


# AWS EB only recognizes a callable object named application
application = app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
db.init_app(app)

# setup flask mail
mail = Mail()
mail.init_app(app)

from kylejnovak import views as view
from kylejnovak.views.admin.admin_view import admin
from kylejnovak.services.login_manager import login_manager

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
from kylejnovak.services.before_requests import *
# import error handlers
from kylejnovak.services.error_handlers import *
# import template filters
from kylejnovak.services.template_filters import *
