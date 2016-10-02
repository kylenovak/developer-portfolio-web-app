from flask import g, Markup
from app import app
from app.services.footer import copyright


@app.before_request
def before_requests():
    # mark this text as safe
    g.copyright_text = Markup(copyright.get_copyright_text(app))
