from flask import Blueprint, render_template

contact_page = Blueprint('contact', __name__, template_folder='templates')


@contact_page.route('/contact')
def contact():
    return render_template('contact.html')
