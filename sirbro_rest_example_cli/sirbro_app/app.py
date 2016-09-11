
from sirbro_app import __projname__, __projver__
from sirbro_app.appconfig import AppConfig
from sirbro_app.api.apiv1 import Client
from sirbro_lib.logger import getLogger



#
# * basic configuration *
#
LOGGER = getLogger('app')
appconfig = AppConfig
client = Client()



#
# * run the app
#
def api_get_info():
    result = client.get_info()
    print( result )


