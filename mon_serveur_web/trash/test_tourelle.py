
import RPi.GPIO as GPIO
import time

#11 et 16
mbas = 26 # verticale
mhaut = 24 # horizontale

GPIO.setmode(GPIO.BOARD)
GPIO.setup(mbas, GPIO.OUT)
GPIO.setup(mhaut, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5

angle = 55
duree = 1

pwm=GPIO.PWM(mhaut,100)
pwm.start(5)

angleChoisi = float(angle)/10 + ajoutAngle
pwm.ChangeDutyCycle(angleChoisi)
time.sleep(duree)
GPIO.cleanup()

