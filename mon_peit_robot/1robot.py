import RPi.GPIO as GPIO
import time
import propulsion

GPIO.setmode(GPIO.BOARD)

print "+-----------------------------------------------------------+"
print "|   Mesure de distance par le capteur ultrasonore HC-SR04   |"
print "+-----------------------------------------------------------+"

Trig = 8          # Entree Trig du HC-SR04 branchee au GPIO 23
Echo = 10         # Sortie Echo du HC-SR04 branchee au GPIO 24

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

repet = input("Entrez un nombre de repetitions de mesure : ")

propulsion.init()

time.sleep(2) # pause au debut


for x in range(repet):    # On prend la mesure "repet" fois

   time.sleep(0.3)       # On la prend toute les 1 seconde

   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)

   while GPIO.input(Echo)==0:  ## Emission de l'ultrason
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

   print "La distance est de : ",distance," cm"


   if distance < 30 :
      print "alors on tourne !"
      propulsion.gauche(1)

   else :
      print "alors on avance !"
      propulsion.avant(1)


GPIO.cleanup()
