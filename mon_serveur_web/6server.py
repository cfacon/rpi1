import actions_robot2
from sys import version as python_version
import logging
from BaseHTTPServer import HTTPServer
import json



from cgi import parse_header, parse_multipart

from pprint import pprint

if python_version.startswith('3'):
    from urllib.parse import parse_qs
    from http.server import BaseHTTPRequestHandler
else:
    from urlparse import parse_qs
    from BaseHTTPServer import BaseHTTPRequestHandler

actions = actions_robot2.actions()

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.log_request()
#	pprint (vars(self))
	path, _, query_string = self.path.partition('?')
#	print path

	actions.action(path)

        return


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    actions.inita()
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
