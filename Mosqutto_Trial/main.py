import paho.mqtt.client as mqtt


# school = input("Please enter your school name")
# username = input("Please enter your user name")
# topic = input("Please enter the topic")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe('#')
    
def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("2.tcp.eu.ngrok.io", 17913, 60)

client.loop_forever()