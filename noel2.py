
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

flag = 0

while flag < 40:
    GPIO.output(led1, not GPIO.input(led1))
    time.sleep(0.1)
    GPIO.output(led2, not GPIO.input(led2))
    time.sleep(0.1)
    GPIO.output(led3, not GPIO.input(led3))
    time.sleep(0.1)
    flag += 1




GPIO.cleanup()


