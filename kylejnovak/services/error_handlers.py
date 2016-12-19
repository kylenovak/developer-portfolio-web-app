from flask import render_template
from kylejnovak import app


@app.errorhandler(404)
def page_not_found(exception):
    app.logger.error(exception)
    return render_template('page_not_found.html'), 404


@app.errorhandler(500)
def internal_error(exception):
    app.logger.error(exception)
    return render_template('internal_error.html'), 500
