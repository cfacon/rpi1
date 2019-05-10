## Controle d'un moteur DC par le Raspberry Pi

import RPi.GPIO as GPIO
from time import sleep

Moteur1A = 16      ## premiere sortie du premier moteur, pin 16
Moteur1B = 18      ## deuxieme sortie de premier moteur, pin 18
Moteur1E = 22      ## enable du premier moteur, pin 22

Moteur2A = 19      ## premiere sortie du premier moteur, pin 16
Moteur2B = 21      ## deuxieme sortie de premier moteur, pin 18
Moteur2E = 23      ## enable du premier moteur, pin 22


def init():
 GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM


 GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
 GPIO.setup(Moteur1B,GPIO.OUT)
 GPIO.setup(Moteur1E,GPIO.OUT)

 GPIO.setup(Moteur2A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
 GPIO.setup(Moteur2B,GPIO.OUT)
 GPIO.setup(Moteur2E,GPIO.OUT)


def arriere(t):
 print"arriere.."

 init()
 GPIO.output(Moteur1A,GPIO.LOW)
 GPIO.output(Moteur1B,GPIO.HIGH)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.LOW)
 GPIO.output(Moteur2B,GPIO.HIGH)
 GPIO.output(Moteur2E,GPIO.HIGH)

 sleep(t)  ## on laisse tourner le moteur 5 secondes avec des parametres
 stop()


def avant(t):
 print "avant.."

 init()

 print "Rotation sens direct, vitesse maximale (rapport cyclique 100%)"
 GPIO.output(Moteur1A,GPIO.HIGH)
 GPIO.output(Moteur1B,GPIO.LOW)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.HIGH)
 GPIO.output(Moteur2B,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.HIGH)

 sleep(t)  ## on laisse tourner le moteur 5 secondes avec des parametres
 stop()

def gauche(t):
 print "gauche.."
 init()
 GPIO.output(Moteur2A,GPIO.HIGH)
 GPIO.output(Moteur2B,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.HIGH)

 GPIO.output(Moteur1A,GPIO.LOW)
 GPIO.output(Moteur1B,GPIO.HIGH)
 GPIO.output(Moteur1E,GPIO.HIGH) 

 sleep(t)
 stop()

def droite(t):
 print "gauche.."
 init()
 GPIO.output(Moteur1A,GPIO.HIGH)
 GPIO.output(Moteur1B,GPIO.LOW)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.LOW)
 GPIO.output(Moteur2B,GPIO.HIGH)
 GPIO.output(Moteur2E,GPIO.HIGH)

 sleep(t)
 stop()


def stop():
 print "Arret du moteur"
 GPIO.output(Moteur1E,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.LOW)
 GPIO.cleanup()
