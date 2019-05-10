#!/usr/bin/env python
# -*- coding: latin-1 -*-


import RPi.GPIO as GPIO
import time

servo_pin = 11  # gpio18

depart = 2      # rapport cyclique pour que le servo 
                # soit au début de son mouvement
                # à ajuster pour votre servo!

arrivee = 13    # rapport cyclique pour que le servo 
                # soit à la fin de son mouvement
                # à ajuster pour votre servo!
     
GPIO.setmode(GPIO.BOARD)  # notation board plutôt que BCM

GPIO.setup(servo_pin, GPIO.OUT)  # pin configurée en sortie

pwm = GPIO.PWM(servo_pin, 50)  # pwm à une fréquence de 50 Hz

position = depart   # on commence à la position de départ

pwm.start(depart)  # on commence le signal pwm



while True:

    if position < arrivee:  # si nous ne sommes pas pas arrivés, 
                            # nous avançons un peu
         pwm.ChangeDutyCycle(float(position))  
         position = position + 0.1
         time.sleep (0.1)
    else:
         position = depart  # si nous sommes arrivés, 
                            # retour à la position de départ
pwm.stop
