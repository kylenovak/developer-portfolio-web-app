import os
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


import app.controllers as controller
app.register_blueprint(controller.home)
