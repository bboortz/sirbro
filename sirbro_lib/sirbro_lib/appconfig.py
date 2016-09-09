import os, platform

from sirbro_lib.flaskconfig import DefaultFlaskConfig



class DefaultBaseConfig(object):
    ENV = os.getenv('ENV', 'PROD')
    PYTHONVERSION = platform.python_version()
    
    def config_to_json(self):
        result = { 
            'ENV': self.ENV,
            'python-version': self.PYTHONVERSION,
        }
        return result


class DefaultCliConfig(DefaultBaseConfig):
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:8080/api')


class DefaultAppConfig(DefaultBaseConfig):
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
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

