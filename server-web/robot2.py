#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import web
import RPi.GPIO as GPIO
import threading


# definit GPIO en sortie 
GPIO.setmode(GPIO.BCM)

pins = [17,23]
servo_pin1 = 17
servo_pin2 = 23
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
vset = 0
horizontal=7
vertical=7



def Volt():
    channel = 0  
    
# definit la page de nom index pour le site web 
urls = ('/','index') 
dossier_web = web.template.render('templates/')

app = web.application(urls, globals())


# definit l action a effectuer quand la page index est appele 
class index:
    
    # utilise quand la page est demande 
    def GET(self):  
        return dossier_web.index()
    
	def TEST()
		pwm1 = GPIO.PWM(servo_pin1, 50)
		pwm2 = GPIO.PWM(servo_pin2, 50)
        pwm1.ChangeDutyCycle(float(horizontal))
        pwm2.ChangeDutyCycle(float(vertical))
        time.sleep(0.5)
		GPIO.cleanup()

	
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
        

                
        elif hasattr(userdata,'orientation'):
            if userdata.orientation=='btb':
                vertical=vertical +0.5
                if vertical > 13:
                    vertical = 13
            elif userdata.orientation=='bth':
                vertical=vertical - 0.5
                if vertical < 2:
                    vertical = 2
            elif userdata.orientation=='btd':
                horizontal=horizontal - 0.5
                if horizontal < 2:
                    horizontal = 2
            elif userdata.orientation=='btg':
                horizontal=horizontal + 0.5
                if horizontal >13:
                    horizontal = 13
			TEST()
                
class ServoThread(threading.Thread):
    def run(self) :
        global vertical
        global horizontal
		
		
        while True :
            pwm1.ChangeDutyCycle(float(horizontal))
            pwm2.ChangeDutyCycle(float(vertical))
            time.sleep(0.1)


			
                    
# programme 
if __name__ == '__main__':
    #myServo= ServoThread()
    myServo.start()
#    GPIO.add_event_detect(15, GPIO.RISING)      # Interruption front montant
#    GPIO.add_event_callback(15,StopEvent,50)
    app.run()    

                    
