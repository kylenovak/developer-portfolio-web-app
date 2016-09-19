import os
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


from app.controllers.home import home

app.register_blueprint(home)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404