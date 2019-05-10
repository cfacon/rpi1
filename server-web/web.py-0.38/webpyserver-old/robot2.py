#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import web
import spidev
import RPi.GPIO as GPIO from RPIO
import PWM from web
import form
import threading
# definit GPIO en sortie
GPIO.setmode(GPIO.BCM)
PWM.setup()
PWM.init_channel(0)

pins = [17,18,22,24,25,27,4]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

vitmotd = GPIO.PWM(4,500)
vitmotg = GPIO.PWM(27,500)
vset = 30

horizontal=150
vertical=150
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def StopEvent(pin): # Sous Programme capteur
    print("Detection obstacle")
    vitmotd.stop()
    vitmotg.stop()
    GPIO.output(25,0)
    GPIO.output(24,0)
    Volt() def Volt():
    spiDevice = spidev.SpiDev() # Creation d'un objet de com SPI
    channel = 0
    spiDevice.open(0,0) # Ouverture de la com SPI vers le MCP3008, broche CE0 (/dev/spidev0.0)
    values = spiDevice.xfer2([1,(8+channel)<<4,0]) # Envoi de 3 bytes (requis par le  MCP3008, 128=>channel 0), renvoi une liste de 3 ytes pour les valeurs
    index = ((values[1]&3) << 8) + values[2] # Valeur codee sur 10 bits
    print "Tension =", round(index*(13.2/1023),2),"V" # Affichage de la tension arrondie à 2 décimales
    if index < 700 :
        print "Batterie faible"
        for x in range(4):
            GPIO.output(22,1)
            time.sleep(0.1)
            GPIO.output(22,0)
            time.sleep(0.1)

# definit la page de nom index pour le site web
urls = ('/','index') 
dossier_web = web.template.render('templates/') 
app = web.application(urls, globals())

# definit l action a effectuer quand la page index est appele
class index:

    # utilise quand la page est demande
    def GET(self):
        return dossier_web.index()

    # traite une requete ajax
    def POST(self):
        global vset
        global vertical
        global horizontal
        userdata = web.input()
        if hasattr(userdata,'vitesse'):
            if userdata.vitesse == '0':
                vset=30
            elif userdata.vitesse == '1':
                vset=45
            elif userdata.vitesse == '2':
                vset=55
            elif userdata.vitesse == '3':
                vset=70
            elif userdata.vitesse == '4':
                vset=85
            elif userdata.vitesse == '5':
                vset=100
            return(userdata.vitesse)

        elif hasattr(userdata,'direction'):
            if userdata.direction == 'avant':
                vitmotd.start(vset)
                vitmotg.start(vset)
                GPIO.output(25,1)
                GPIO.output(24,1)
            elif userdata.direction == 'gauche':
                vitmotd.start(vset)
                vitmotg.stop()
                GPIO.output(25,1)
                GPIO.output(24,0)
            elif userdata.direction == 'droite':
                vitmotd.stop()
                vitmotg.start(vset)
                GPIO.output(25,0)
                GPIO.output(24,1)
            elif userdata.direction == 'arriere':
                vitmotd.start(vset)
                vitmotg.start(vset)
                GPIO.output(25,0)
                GPIO.output(24,0)
            elif userdata.direction == 'stop':
                vitmotd.stop()
                vitmotg.stop()
                GPIO.output(25,0)
                GPIO.output(24,0)
                Volt()

        elif hasattr(userdata,'orientation'):
            if userdata.orientation=='btb':
                vertical=vertical +2
                if vertical > 180:
                    vertical = 180
            elif userdata.orientation=='bth':
                vertical=vertical - 2
                if vertical < 120:
                    vertical = 120
            elif userdata.orientation=='btd':
                horizontal=horizontal - 2
                if horizontal < 120:
                    horizontal = 120
            elif userdata.orientation=='btg':
                horizontal=horizontal + 2
                if horizontal >180:
                    horizontal = 180

class ServoThread(threading.Thread):
    def run(self) :
        global vertical
        global horizontal
        while True :
           PWM.add_channel_pulse(0, 17, 0, horizontal)
           PWM.add_channel_pulse(0, 18 ,0, vertical)
           time.sleep(0.05)

# programme
if __name__ == '__main__':
    myServo= ServoThread()
    myServo.start()
    GPIO.add_event_detect(15, GPIO.RISING) # Interruption front montant
    GPIO.add_event_callback(15,StopEvent,50)
    app.run()

