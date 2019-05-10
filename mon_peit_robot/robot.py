import RPi.GPIO as GPIO
import time
import propulsion
import tourelle

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


def mesure() :

   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)

   while GPIO.input(Echo)==0:  ## Emission de l'ultrason
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s
   return distance

def choix_dir() :
# tourelle a gauche
   tourelle.gauche()
   time.sleep(0.3)       # On la prend toute les x seconde
   d_gauche = mesure()
   d_gauche = mesure()
   print "R2 La distance gauche est de : ",d_gauche," cm"

# tourelle a droite
   tourelle.droite()
   time.sleep(0.3)       # On la prend toute les x seconde
   d_droite = mesure()
   d_droite = mesure()
   print "R2 La distance droite est de : ",d_droite," cm"
   time.sleep(0.3)       # On la prend toute les x seconde


# tourelle en face
   tourelle.face()
   d_face = mesure()
   print "R2 La distance en face est de : ",d_face," cm"
   time.sleep(0.3)       # On la prend toute les x seconde

#   d = ("gauche" if d_gauche > d_droite else "droite")
   if d_gauche > d_droite :
      dmax = d_gauche
      dir = "gauche"
   else :
      dmax = d_droite
      dir = "droite"

   if dmax > d_face :
      dir = dir
   else :
      dmax = d_face
      dir = "face"

   print "dir:",dir," dmax:",dmax
   return dir


propulsion.init()
tourelle.init()
tourelle.milieu()

time.sleep(1) # pause au debut


for x in range(repet):    # On prend la mesure "repet" fois

   time.sleep(0.3)       # On la prend toute les x seconde

   distance = mesure()
   if distance > 30 :
      print "OK on avance !"
      propulsion.avant(1)

   else :
      dir = choix_dir()

      if dir == "gauche" :
         print "alors on tourne a gauche!"
         propulsion.gauche(1)

      elif dir == "droite" :
         print "alors on tourne a droite !"
         propulsion.droite(1)

      elif dir == "face" :
         print "alors on avance !"
         propulsion.avant(1)

   time.sleep(0.5)       # On la prend toute les x seconde


GPIO.cleanup()
 
