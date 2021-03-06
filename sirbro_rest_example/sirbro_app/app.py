
from sirbro_app import __projname__, __projver__
from sirbro_app.appconfig import AppConfig
from sirbro_app.blueprint.apiv1 import blueprint as blueprint_apiv1
from sirbro_lib import __projname__ as __libname__, __projver__ as __libver__
from sirbro_lib.logger import getLogger
from sirbro_lib.blueprint_base import blueprint as  blueprint_base

from flask import Flask



#
# * basic configuration *
#
LOGGER = getLogger('app')
appconfig = AppConfig
app = Flask(__name__)
app.config.from_object(appconfig.__FLASKCONFIG__)
app.register_blueprint(blueprint_base)
app.register_blueprint(blueprint_apiv1, url_prefix="/api/v1/")
app.register_blueprint(blueprint_apiv1, url_prefix="/api/")



#
# * run the app
#
def run_app():
    LOGGER.info("%s %s starting..." % (__projname__, __projver__) )
    LOGGER.debug("using %s %s." % (__libname__, __libver__) )
    LOGGER.info("listening on PORT 8080.")

    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)

    LOGGER.info("%s %s stopped." % (__projname__, __projver__) )

def get_app():
    return app

