import os

from sirbro_rest_saml2_example.flaskconfig import FlaskConfig

class AppConfig(object):
    ENV = "PROD"
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    FLASKCONFIG = FlaskConfig
