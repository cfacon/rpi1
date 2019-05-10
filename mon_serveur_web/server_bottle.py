import datetime
import bottle
#import globalConfig
from bottle import route, run, request, response, redirect, template, static_file

@bottle.route("/")
@bottle.view("joy.tpl")
def index() :
    print ("ok")
    heure = datetime.datetime.now().strftime("<p>Nous sommes le %d/%m/%Y, il est %H:%M:%S</p>")
    return {"title":"Horloge", "body" : heure}

@bottle.route('/assets/<filepath:path>')
def assets(filepath):
  return static_file(filepath, root='assets/')


@route('/cmd/<cmd>')
def controls(cmd):

  if globalConfig.dir != cmd:
    globalConfig.dir = cmd
    print ("_____cmd:"+cmd)

  return ''



#bottle.run(bottle.app(), host='0.0.0.0', port=8080, debug= False, reloader=True)
bottle.run(host='0.0.0.0', port=8080)

