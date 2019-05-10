#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import actions_robot
 

PORT_NUMBER = 8080
from urlparse import urlparse

from pprint import pprint



actions = actions_robot.actions()


class myHandler(BaseHTTPRequestHandler):


        def do_POST(self):
	        self._set_headers()
        	self.log_request()
	        pprint (vars(self))
        	path, _, query_string = self.path.partition('?')
	        print path

        	actions.action(path)

	        return
	
	#Handler for the GET requests
	def do_GET(self):
                print 'get..' + self.path

                if self.path=='/favicon.ico':
                  print 'favicon..'
                else:
                  query = urlparse(self.path).query
                  print query
		  # filtre sur val ici
                  query_components = dict(qc.split("=") for qc in query.split("&"))
                  print query_components["action"]
                  actions.action("/macros/turn_left/")

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Commande recu !")
		return
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port' , PORT_NUMBER
	
        actions.inita()

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
        actions.clean()
	server.socket.close()
