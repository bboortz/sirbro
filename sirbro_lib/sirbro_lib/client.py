
from sirbro_app.appconfig import AppConfig
from sirbro_lib.logger import getLogger

import urllib.request



LOGGER = getLogger('client')



class BaseClient(object):

    def __init__(self):
        self.BASE_URL = "%s" % (AppConfig.BASE_URL)

    def log_request(self, request):
        str = "REQUEST: %s %s" % ( request.get_method(), request.get_full_url() )
        LOGGER.debug(str)
        headers = request.header_items()
        for h in headers:
            LOGGER.debug(">> %s" % h)

    def get_request(self, url, **params):
        url = '%s%s?%s' % (self.BASE_URL, url, params)
        request = urllib.request.Request(url)
        urllib.request.HTTPHandler(debuglevel=1)
        self.log_request(request)
        response = urllib.request.urlopen(request)
        return ( response.read().decode(AppConfig.ENCODING) )

    def post_request(self, url, **data):
        import json
        post_data = urllib.urlencode({'data': json.dumps(data)})
        fh = urllib2.urlopen('%s%s' % (self.BASE_URL, url), post_data)
        response = fh.read()
        return json.loads(response)

