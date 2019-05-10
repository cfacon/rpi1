#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Contrôle d'un moteur pas avec un Raspberry Pi
L'utilisateur choisit le nombre de pas qui sera fait par le moteur
electroniqueamateur.blogspot.com
'''

import RPi.GPIO as GPIO
import time
     
GPIO.setmode(GPIO.BOARD)  #notation board plutôt que BCM
     
pin_bobine_1_1 = 15    #GPIO 22
pin_bobine_1_2 = 16    #GPIO 23
pin_bobine_2_1 = 18    #GPIO 24
pin_bobine_2_2 = 22    #GPIO 25

# configuration des pins en sortie
GPIO.setup(pin_bobine_1_1, GPIO.OUT)
GPIO.setup(pin_bobine_1_2, GPIO.OUT)
GPIO.setup(pin_bobine_2_1, GPIO.OUT)
GPIO.setup(pin_bobine_2_2, GPIO.OUT)

print "----CONTRÔLE D'UN MOTEUR PAS À PAS -----"
     
def marche_avant(attente, nombre_de_pas):

    for i in range(0, nombre_de_pas):
        prochainStep(i % 4)
        time.sleep(attente)

def marche_arriere(attente, nombre_de_pas):
    for i in range(0, nombre_de_pas):
        prochainStep(3 - (i % 4))
        time.sleep(attente)

def reglage_pins(pin1, pin2, pin3, pin4):
    GPIO.output(pin_bobine_1_1, pin1)
    GPIO.output(pin_bobine_1_2, pin2)
    GPIO.output(pin_bobine_2_1, pin3)
    GPIO.output(pin_bobine_2_2, pin4)

def prochainStep(numero):
    if (numero == 0):
        reglage_pins(1, 0, 1, 0)
    if (numero == 1):
        reglage_pins(0, 1, 1, 0)
    if (numero == 2):
        reglage_pins(0, 1, 0, 1)
    if (numero == 3):
        reglage_pins(1, 0, 0, 1)
     
def gauche(t):
    reglage_pins(0, 0, 1, 0)
    time.sleep(t)

    
def droite(t):
    reglage_pins(0, 0, 0, 1)
    time.sleep(t)


#un demi tour 0.2
attente = 0.2

#un quart de tour 0.1
attente2 = 0.1

# droite
#reglage_pins(0, 0, 0, 1)
#time.sleep(attente)

# gauche
#reglage_pins(0, 0, 1, 0)
#time.sleep(attente2)

droite(0.05)
#gauche(0.05)

GPIO.cleanup()

