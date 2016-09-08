
from sirbro_lib.appconfig import DefaultAppConfig
from sirbro_rest_saml2_example.flaskconfig import FlaskConfig

class AppConfig(DefaultAppConfig):
    FLASKCONFIG = FlaskConfig
    
    def config_to_json(self):
        result = { 
            'ENV': self.ENV,
            'IP': self.IP,
            'PORT': self.PORT,
            'python-version': self.PYTHONVERSION,
            'flask-version': self.FLASKCONFIG.FLASK_VERSION ,
            'flask-debug': self.FLASKCONFIG.DEBUG ,
            'flask-testing': self.FLASKCONFIG.TESTING ,
        }
        return result
