# Import des modules
import RPi.GPIO as GPIO
import time

# led
led = 4

# Initialisation de la numerotation et des E/S
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)

rapport = 10.0
sens = True

p = GPIO.PWM(led, 200)
p.start(rapport) #ici, rapport_cyclique vaut entre 0.0 et 100.0

# On fait varier l'intensite de la LED
while True:
    if sens and rapport < 100.0:
        rapport += 10.0
    elif sens and rapport >= 100.0:
        sens = False
    elif not sens and rapport > 10.0:
        rapport -= 10.0
    elif rapport == 10.0:
        sens = True
    p.ChangeDutyCycle(rapport)
    time.sleep(0.25)

GPIO.cleanup()


