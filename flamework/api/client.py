import urllib
import httplib
import base64
import json
import logging

from request import encode_multipart_formdata, encode_urlencode

class OAuth2:

    def __init__(self, access_token, **kwargs):

        self.access_token = access_token

        self.hostname = kwargs['hostname']
        self.endpoint = kwargs['endpoint']

        logging.debug("setup API to use %s%s" % (self.hostname, self.endpoint))

    def execute_method(self, method, kwargs, encode=encode_urlencode):

        logging.debug("calling %s with args %s" % (method, kwargs))

        kwargs['method'] = method
        kwargs['access_token'] = self.access_token

        (headers, body) = encode(kwargs)

        url = self.endpoint
        logging.debug("calling %s" % url)

        conn = httplib.HTTPSConnection(self.hostname)
        conn.request('POST', url, body, headers)

        rsp = conn.getresponse()
        body = rsp.read()

        logging.debug("response is %s" % body)

        try:
            data = json.loads(body)
        except Exception, e:
            logging.error(e)
            raise Exception, e

        # check status here...

        return data

    def execute_method_paginated(self, method, kwargs, cb, encode=encode_urlencode):

        pages = None
        page = 1

        while not pages or page <= pages:

            kwargs['page'] = 1
            rsp = self.execute_method(method, kwargs, encode)

            if not cb(rsp):
                logging.warning("execute_method_paginated callback did not return True, halting iteration")
                break

            if not pages:
                pages = rsp.get('pages', None)

            if not pages:
                logging.error("can not determine pagination information")
                break

            page += 1
        
if __name__ == '__main__':

    import sys
    import pprint
    import time
    import optparse

    parser = optparse.OptionParser(usage="python api.py --host <HOST> --endpoint <ENDPOINT> --access-token <ACCESS TOKEN>")

    # sudo make me read a config file...

    parser.add_option('--access-token', dest='access_token',
                        help='Your Flamework API access token',
                        action='store')

    parser.add_option('--host', dest='host',
                        help='Your Flamework API host',
                        action='store')

    parser.add_option('--endpoint', dest='endpoint',
                        help='Your Flamework API endpoint',
                        action='store')

    parser.add_option("-v", "--verbose", dest="verbose",
                      help="enable chatty logging; default is false", 
                      action="store_true", default=False)

    options, args = parser.parse_args()
    
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    api = OAuth2(options.access_token)

    # Sample API call goes here

    sys.exit()
