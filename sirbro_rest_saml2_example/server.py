#!/usr/bin/env python3

import os
import sys

from sirbro_rest_saml2_example import __projname__, __projver__
from sirbro_rest_saml2_example.appconfig import AppConfig
from sirbro_rest_saml2_example.blueprint import apiv1 as blueprint_apiv1
from sirbro_lib import __projname__ as __libname__, __projver__ as __libver__
from sirbro_lib.logger import getLogger
from sirbro_lib.blueprint_base import blueprint as  blueprint_base

from flask import Flask
from flask_bootstrap import Bootstrap





#
# * basic configuration *
#
LOGGER = getLogger('server')



#
# * main routine *
#
def main():
    LOGGER.info("%s %s starting..." % (__projname__, __projver__) )
    LOGGER.debug("using %s %s." % (__libname__, __libver__) )
    LOGGER.info("listening on PORT 8080.")

    appconfig = AppConfig
    app = Flask(__name__)
    app.config.from_object(appconfig.FLASKCONFIG)
    app.register_blueprint(blueprint_base)
    app.register_blueprint(blueprint_apiv1)
    Bootstrap(app)
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)

    LOGGER.info("%s %s started." % (__projname__, __projver__) )

if __name__ == "__main__":
    main()
