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

    if action=='g':
      print "_gauche"
      propulsion.gauche(0.1)
    if action=='d':
      print "_droite"
      propulsion.droite(0.1)
    if action=='av':
      print "_avant"
      propulsion.avant(1)
    if action=='ar':
      print "_arriere"
      propulsion.arriere(1)
    if action=='stop':
      print "_arret"
      propulsion.stop()


#    tourelle.tourner(self.angle)
