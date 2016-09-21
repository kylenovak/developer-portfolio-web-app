from flask import Blueprint, render_template

guestbook_page = Blueprint('guestbook', __name__, template_folder='templates')


@guestbook_page.route('/guestbook')
def guestbook():
    return render_template('guestbook.html')
