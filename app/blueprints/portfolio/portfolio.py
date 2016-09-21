from flask import Blueprint, render_template

portfolio_page = Blueprint('portfolio', __name__, template_folder='templates')


@portfolio_page.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
