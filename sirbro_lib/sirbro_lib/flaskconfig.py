import os

from flask import __version__ as FLASK_VERSION



class DefaultFlaskConfig(object):
    FLASK_VERSION = FLASK_VERSION
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'NONE')
    JSONIFY_PRETTYPRINT_REGULAR = True
