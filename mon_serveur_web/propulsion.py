## Controle d'un moteur DC par le Raspberry Pi

import RPi.GPIO as GPIO
from time import sleep

Moteur2A = 11      ## premiere sortie du premier moteur, pin 16
Moteur2B = 13      ## deuxieme sortie de premier moteur, pin 18
Moteur2E = 15      ## enable du premier moteur, pin 22

Moteur1A = 19      ## premiere sortie du premier moteur, pin 16
Moteur1B = 21      ## deuxieme sortie de premier moteur, pin 18
Moteur1E = 23      ## enable du premier moteur, pin 22

GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM

def clean():
 GPIO.cleanup()

def init():
 GPIO.cleanup()
 GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM


# moteur gauche
 GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
 GPIO.setup(Moteur1B,GPIO.OUT)
 GPIO.setup(Moteur1E,GPIO.OUT)

# moteur droit
 GPIO.setup(Moteur2A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
 GPIO.setup(Moteur2B,GPIO.OUT)
 GPIO.setup(Moteur2E,GPIO.OUT)

 stop()

 pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la pin 22 a une frequence de 50 Hz
 pwm.start(80)   ## on commemnce avec un rapport cyclique de 100%



def test(t):
 print "test.."
############################################
############################################
############################################
############################################



def avant(t):
 print"go avant.."

# init()
 GPIO.output(Moteur1A,GPIO.LOW)
 GPIO.output(Moteur1B,GPIO.HIGH)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.LOW)
 GPIO.output(Moteur2B,GPIO.HIGH)
 GPIO.output(Moteur2E,GPIO.HIGH)

# sleep(t)  ## on laisse tourner le moteur 5 secondes avec des parametres
# stop()


def arriere(t):
 print "arriere.."

# init()

 print "Rotation sens direct, vitesse maximale (rapport cyclique 100%)"
 GPIO.output(Moteur1A,GPIO.HIGH)
 GPIO.output(Moteur1B,GPIO.LOW)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.HIGH)
 GPIO.output(Moteur2B,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.HIGH)

# sleep(t)
# stop()
# sleep(t)  ## on laisse tourner le moteur 5 secondes avec des parametres

def gauche(t):
 print "gauche.."
# init()
 GPIO.output(Moteur2A,GPIO.HIGH)
 GPIO.output(Moteur2B,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.HIGH)

 GPIO.output(Moteur1A,GPIO.LOW)
 GPIO.output(Moteur1B,GPIO.HIGH)
 GPIO.output(Moteur1E,GPIO.HIGH) 

# sleep(t)
# stop()

def droite(t):
 print "droite.."
# init()
 GPIO.output(Moteur1A,GPIO.HIGH)
 GPIO.output(Moteur1B,GPIO.LOW)
 GPIO.output(Moteur1E,GPIO.HIGH)

 GPIO.output(Moteur2A,GPIO.LOW)
 GPIO.output(Moteur2B,GPIO.HIGH)
 GPIO.output(Moteur2E,GPIO.HIGH)

# sleep(t)
# stop()


def stop():
 print "Arret du moteur"
 GPIO.output(Moteur1E,GPIO.LOW)
 GPIO.output(Moteur2E,GPIO.LOW)
# GPIO.cleanup()
