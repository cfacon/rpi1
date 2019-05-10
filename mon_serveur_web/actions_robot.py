#!/usr/bin/python
#import tourelle
import propulsion
import time

class actions:
  def __init__(self): # constructeur
    self.angle = 90

# init 
#    tourelle.tourner(90)
  def clean(a):
    propulsion.stop()
    propulsion.clean()

  def inita(a):
    propulsion.init()
    time.sleep(0.1)

  def action(self, action):
    print "action==>"+action 
#    propulsion.init()
    t = 0
#    time.sleep(0.1)

    if action=='/macros/turn_left/':
      print "gauche"
      time.sleep(t)   
      propulsion.gauche(0.1)
    if action=='/macros/turn_right/':
      print "droite"
      time.sleep(t)   
      propulsion.droite(0.1)
    if action=='/macros/go_forward/':
      print "avant"
      time.sleep(t)   
      propulsion.avant(1)
    if action=='/macros/go_backward/':
      print "arriere"
      time.sleep(t)   
      propulsion.arriere(1)
    if action=='/macros/stop/':
      print "arret"
      time.sleep(t)   
      propulsion.stop()


#    tourelle.tourner(self.angle)
