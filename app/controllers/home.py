from flask import Blueprint, request, render_template

home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/')
def hello():
    return render_template('home/index.html')
