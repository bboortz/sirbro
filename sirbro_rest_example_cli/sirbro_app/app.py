
from sirbro_app import __projname__, __projver__
from sirbro_app.appconfig import AppConfig
from sirbro_lib import __projname__ as __libname__, __projver__ as __libver__
from sirbro_lib.logger import getLogger



#
# * basic configuration *
#
LOGGER = getLogger('app')
appconfig = AppConfig



#
# * run the app
#
def run_app():
    LOGGER.info("%s %s starting..." % (__projname__, __projver__) )
    LOGGER.debug("using %s %s." % (__libname__, __libver__) )
    LOGGER.info("BASE_URL is %s." % (AppConfig.BASE_URL) )


    LOGGER.info("%s %s stopped." % (__projname__, __projver__) )

def get_app():
    return app

