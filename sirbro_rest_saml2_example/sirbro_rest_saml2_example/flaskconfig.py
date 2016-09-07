import os

class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'eoki99)u9uJ)J)J9jhgu5hg49)jjjJJKKK0Ij9jf')
    JSONIFY_PRETTYPRINT_REGULAR = True
