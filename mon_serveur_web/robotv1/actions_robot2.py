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

    if action=='left':
      print "_____gauche"
      propulsion.gauche(0.1)
    if action=='left up':
      print "_____gauche avant"
      propulsion.gauche_avant(0.1)
    if action=='right':
      print "_____droite"
      propulsion.droite(0.1)
    if action=='up':
      print "_____avant"
      propulsion.avant(1)
    if action=='down':
      print "_____arriere"
      propulsion.arriere(1)
    if action=='stop':
      print "_____arret"
      propulsion.stop()


#    tourelle.tourner(self.angle)
