
from sirbro_lib.appconfig import DefaultApiConfig
from sirbro_app.flaskconfig import FlaskConfig

class AppConfig(DefaultApiConfig):
    __FLASKCONFIG__ = FlaskConfig
    FLASK_VERSION = __FLASKCONFIG__.FLASK_VERSION
    FLASK_DEBUG = __FLASKCONFIG__.DEBUG
    FLASK_TESTING = __FLASKCONFIG__.TESTING
    
#    def config_to_json(self):
#        result = { 
#            'ENV': self.ENV,
#            'IP': self.IP,
#            'PORT': self.PORT,
#            'python-version': self.PYTHONVERSION,
#            'flask-version': self.FLASKCONFIG.FLASK_VERSION ,
#            'flask-debug': self.FLASKCONFIG.DEBUG ,
#            'flask-testing': self.FLASKCONFIG.TESTING ,
#        }
#        return result
