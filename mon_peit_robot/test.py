
import RPi.GPIO as GPIO
import time
import propulsion

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

propulsion.init()
propulsion.avant(1)

time.sleep(1)
propulsion.avant(2)
time.sleep(1)
propulsion.gauche(2)
time.sleep(1)
propulsion.droite(2)

propulsion.stop()

GPIO.cleanup()

