import RPi.GPIO as GPIO
import time
import propulsion
import tourelle

GPIO.setmode(GPIO.BOARD)

print "+-----------------------------------------------------------+"
print "|   Mesure de distance par le capteur ultrasonore HC-SR04   |"
print "+-----------------------------------------------------------+"


#propulsion.init()



#propulsion.avant(1)

tourelle.init()
tourelle.droite()
tourelle.gauche()
tourelle.face()



time.sleep(1) # pause au debut


GPIO.cleanup()
