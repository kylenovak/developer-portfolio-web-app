from flask import g, Markup

from .. import application
from . import copyright


@application.before_request
def before_requests():
    # mark this text as safe
    g.copyright_text = Markup(copyright.get_copyright_text(app))
