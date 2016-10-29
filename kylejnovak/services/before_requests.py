from flask import g, Markup

from kylejnovak import app
from kylejnovak.services import copyright


@app.before_request
def before_requests():
    # mark this text as safe
    g.copyright_text = Markup(copyright.get_copyright_text(app))
