#!/usr/bin/env python
# -*- coding: latin-1 -*-

import RPi.GPIO as GPIO
import time

#11 et 16

#servo_pin = 11  # équivalent de GPIO 18
servo_pin = 16  # équivalent de GPIO 18

GPIO.setmode(GPIO.BOARD)  # notation board plutôt que BCM

GPIO.setup(servo_pin, GPIO.OUT)  # pin configurée en sortie

pwm = GPIO.PWM(servo_pin, 50)  # pwm à une fréquence de 50 Hz

#1 a 13
rapport = 7       # rapport cyclique initial de 7%

pwm.start(rapport)

while True:
    print "Rapport cyclique actuel: " , rapport
    rapport = raw_input ("Rapport cyclique désiré:  ")
    pwm.ChangeDutyCycle(float(rapport))

