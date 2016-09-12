
from sirbro_app.appconfig import AppConfig
from sirbro_lib.logger import getLogger
from sirbro_lib.client import BaseClient

import urllib.request



LOGGER = getLogger('apiv1')
API_VERSION = "v1"
BASE_URL = "%s/%s" % (AppConfig.BASE_URL, API_VERSION)



class Client(BaseClient):

    def __init__(self):
        self.BASE_URL = "%s/%s" % (AppConfig.BASE_URL, API_VERSION)

    def get_alive(self):
        result = self.get_request("/alive")
        return result

    def get_info(self):
        result = self.get_request("/info")
        return result

    def get_config(self):
        result = self.get_request("/config")
        return result
