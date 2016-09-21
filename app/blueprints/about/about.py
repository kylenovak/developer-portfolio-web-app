from flask import Blueprint, render_template

about_page = Blueprint('about', __name__, template_folder='templates')


@about_page.route('/about')
def about():
    return render_template('about.html')
