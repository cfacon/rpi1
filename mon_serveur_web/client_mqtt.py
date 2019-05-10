#!/usr/bin/python


import paho.mqtt.client as mqtt #import the client1
import time
import Queue
import actions_robot2




actions = actions_robot2.actions()

q = Queue.Queue()
c = 0
a = 1

def worker():
    while not q.empty():
        item = q.get()
        print("depile ", item)
	actions.action(item)
	time.sleep(1)
        q.task_done()


############
def on_message(client, q, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    msg = message.payload.decode("utf-8")

    actions.action(msg)

#    if msg == "stop":
#        with q.mutex:
#         q.queue.clear()
#        q.put(msg)
#    if q.empty:
#        print("->empty")
#        q.put(msg)
#        worker()
#    else:
#        print("->not empty")
#        q.put(msg)

#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)
    print("  ")


########################################
broker_address="localhost"

#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1", userdata=c) #create new instance
client.on_message=on_message #attach function to callback

client.username_pw_set("apo", "frgs6422")


client.user_data_set(q)

actions.inita()

print("connecting to broker")
client.connect(broker_address) #connect to broker


client.loop_start() #start the loop

topic = "robot/commande"

print("Subscribing to topic",topic)
client.subscribe(topic)
print("Publishing message to topic",topic)
client.publish(topic,"OFF")
#time.sleep(10) # wait
#client.loop_stop() #stop the loop



client.loop_forever()
quit()
