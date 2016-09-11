
from sirbro_app.appconfig import AppConfig
from sirbro_lib.logger import getLogger

import urllib.request

LOGGER = getLogger('apiv1')



class Client(object):

    def __init__(self):
        pass

    def log_request(self, request):
        str = "%s %s %s" % ( request.get_method(), request.get_full_url(), request.get_header("Host") )
        print (request.header_items() )
        LOGGER.debug(str)

    def get_request(self, url, **params):
        url = '%s%s?%s' % (AppConfig.BASE_URL, url, params)
        request = urllib.request.Request(url)
        LOGGER.debug( dir(request) )
        self.log_request(request)
        LOGGER.debug( dir(request) )
        response = urllib.request.urlopen(request)
        return (response.read().decode('utf-8'))

    def post_request(self, url, **data):
        import json
        post_data = urllib.urlencode({'data': json.dumps(data)})
        fh = urllib2.urlopen('%s%s' % (AppConfig.BASE_URL, url), post_data)
        response = fh.read()
        return json.loads(response)

    def get_info(self):
        result = self.get_request("/info")
        return result
