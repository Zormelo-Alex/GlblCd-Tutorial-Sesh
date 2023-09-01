import paho.mqtt.client as mqtt
import time

Connected = False  # global variable for the state of the connection

school = input("Please enter your school name\n")
username = input("Please enter your user name\n")
# topic = input("Please enter the topic")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        tempmessage = school + "/"+ username + " joined the chat"
        client.publish("glblcd", tempmessage)
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("2.tcp.eu.ngrok.io", 17913, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)


try:
    while True:
        message = input('Your message: ')
        message = school + "/" + username + ": " + message
        client.publish("glblcd", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()