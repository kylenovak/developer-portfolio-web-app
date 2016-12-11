from flask import g, Markup

from kylejnovak import app
from kylejnovak.services import copyright
from kylejnovak.services.bio_service import BioService

bio_service = BioService()


@app.before_request
def before_requests():
    # mark this text as safe
    g.copyright_text = Markup(copyright.get_copyright_text(app))

    bio_content = bio_service.get_bio()
    if bio_content is not None:
        bio_content = Markup(bio_content)

    g.bio_content = Markup(bio_content)
