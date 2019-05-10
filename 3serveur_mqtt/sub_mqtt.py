import paho.mqtt.client as mqtt 
broker_address="localhost" 

client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("robot/commande","av")#publish
