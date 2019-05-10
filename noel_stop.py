

# Import des modules
import RPi.GPIO as GPIO
import time

# led
led1 = 4
led2 = 17
led3 = 18

# Initialisation de la numerotation et des E/S
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(led2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(led3, GPIO.OUT, initial = GPIO.LOW)




GPIO.cleanup()


