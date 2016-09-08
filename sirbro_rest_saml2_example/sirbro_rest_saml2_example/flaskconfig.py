import os

from sirbro_lib.flaskconfig import DefaultFlaskConfig

from flask import __version__ as FLASK_VERSION



class FlaskConfig(DefaultFlaskConfig):
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'eoki99)u9uJ)J)J9jhgu5hg49)jjjJJKKK0Ij9jf')
    JSONIFY_PRETTYPRINT_REGULAR = True
