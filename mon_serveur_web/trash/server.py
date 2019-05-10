#!/usr/bin/python
 
import BaseHTTPServer
import CGIHTTPServer
 
PORT = 8090
server_address = ("", PORT)

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print "Serveur actif sur le port :", PORT

httpd = server(server_address, handler)
httpd.serve_forever()

from urlparse import urlparse
query = urlparse(self.path).query
query_components = dict(qc.split("=") for qc in query.split("&"))
imsi = query_components["imsi"]

