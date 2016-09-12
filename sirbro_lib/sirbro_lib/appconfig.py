import os, platform

from sirbro_lib.flaskconfig import DefaultFlaskConfig
from sirbro_lib.json import *



jsonUtil = jsonUtil()



class DefaultBaseConfig(dict):
    ENV = os.getenv('ENV', 'PROD')
    ENCODING = "utf-8"
    PYTHONVERSION = platform.python_version()

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self[attr]

#    def __repr__(self):
#        return json.dumps(self.__dict__)

#    def to_JSON(self):
#        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#    def __newClazz__(cls, *args, **kw):
#        constructor = getattr(cls, "__new__")
#        instance = constructor(cls) if constructor is object.__new__ else constructor(cls, *args, **kw)
#        instance.__init__(cls, *args, **kw)
#        return instance

#    def config_to_json(self):
#        clazz = __newClazz__("DefaultBaseConfig")
#        result = JsonClazzEncoder().encode(DefaultBaseConfig())
#        return result
#        print("la %s" % self.__dict__)
#        return jsonUtil.dump_json(self.__dict__)

#    def config_to_json(self):
#        result = { }
#        clazz = DefaultBaseConfig()
#        members = [attr for attr in dir(clazz) if not callable(attr) and not attr.startswith("__")]
#        for m in members:
#            result[m] = getattr(clazz, m)
#
#        return result



class DefaultCliConfig(DefaultBaseConfig):
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:8080/api')


class DefaultApiConfig(DefaultBaseConfig):
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    __FLASKCONFIG__ = DefaultFlaskConfig
    
    def get_flask_config(self):
        return self.__FLASKCONFIG

