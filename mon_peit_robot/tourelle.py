
import RPi.GPIO as GPIO
import time

ajoutAngle = 5
angle = 55
duree = 1
mbas = 26 # verticale
mhaut = 24 # horizontale


def init() :
 #11 et 16

 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(mbas, GPIO.OUT)
 GPIO.setup(mhaut, GPIO.OUT)
 GPIO.setwarnings(False)

# milieu horizontale
def milieu() :

 angle = 90
 pwm=GPIO.PWM(mhaut,100)
 pwm.start(5)

 angleChoisi = float(angle)/10 + ajoutAngle
 pwm.ChangeDutyCycle(angleChoisi)
 time.sleep(duree)

def droite() :

 angle = 50
 pwm=GPIO.PWM(mbas,100)
 pwm.start(5)

 angleChoisi = float(angle)/10 + ajoutAngle
 pwm.ChangeDutyCycle(angleChoisi)
 time.sleep(duree)

def gauche() :

 angle = 130
 pwm=GPIO.PWM(mbas,100)
 pwm.start(5)

 angleChoisi = float(angle)/10 + ajoutAngle
 pwm.ChangeDutyCycle(angleChoisi)
 time.sleep(duree)

def face() :

 angle = 90
 #pwm=GPIO.PWM(mhaut,80)
 pwm=GPIO.PWM(mbas,100)
 pwm.start(5)

 angleChoisi = float(angle)/10 + ajoutAngle
 pwm.ChangeDutyCycle(angleChoisi)
 time.sleep(duree)

