import RPi.GPIO as GPIO
import time
import propulsion

GPIO.setmode(GPIO.BOARD)

print "+-----------------------------------------------------------+"
print "|   Mesure de distance par le capteur ultrasonore HC-SR04   |"
print "+-----------------------------------------------------------+"

#Trig = 8          # Entree Trig du HC-SR04 branchee au GPIO 23
#Echo = 10         # Sortie Echo du HC-SR04 branchee au GPIO 24

#GPIO.setup(Trig,GPIO.OUT)
#GPIO.setup(Echo,GPIO.IN)

#GPIO.output(Trig, False)




propulsion.init()

time.sleep(2) # pause au debut




propulsion.droite(1)
time.sleep(0.5)       # On la prend toute les x seconde


GPIO.cleanup()
