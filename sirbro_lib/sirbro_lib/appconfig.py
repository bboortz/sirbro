import os, platform

from sirbro_lib.flaskconfig import DefaultFlaskConfig

class DefaultAppConfig(object):
    ENV = os.getenv('ENV', 'PROD')
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    PYTHONVERSION = platform.python_version()
    FLASKCONFIG = DefaultFlaskConfig
    
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
