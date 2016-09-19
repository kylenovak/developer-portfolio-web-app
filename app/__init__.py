import os
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


from app.error_handlers import *

import app.blueprints as blueprint
app.register_blueprint(blueprint.home)
