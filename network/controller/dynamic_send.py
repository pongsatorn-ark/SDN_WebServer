import paho.mqtt.client as mqtt
import time

mqtt_auth = {
    'username': 'administrator',
    'password': 'P@ssw0rd@DevNet'
}


def on_connect(client, userdata, flags, rc):
    global loop_flag
    loop_flag = 0


broker_address = "localhost"
client = mqtt.Client()
client.username_pw_set("administrator", "P@ssw0rd@DevNet")
client.on_connect = on_connect
client.connect(broker_address, 1883)

loop_flag = 1
counter = 0
while loop_flag == 1:
    client.publish("test", payload="Hello", qos=0)
    print(counter)
    counter += 1
    time.sleep(300)

client.disconnect()
client.loop_stop()
