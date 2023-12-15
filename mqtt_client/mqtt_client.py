from datetime import datetime

import paho.mqtt.client as mqtt
import dataset


def on_connect_callback(client, userdata, flags, rc):
    if rc == 0: # ok
        print('Connection OK')
        # topic = '#' # The whole tree
        topic = 'esp32/+/sensors/#'
        client.subscribe(topic)
        client.message_callback_add(topic, on_message_callback) # call to fuinction later
    else:
        print('Connection fail')
    
def on_message_callback(client, userdata, msg):
    print(msg.topic, msg.payload)
    topic = msg.topic.split('/')[-1]
    payload = float(msg.payload)

    # Database
    db = dataset.connect('sqlite:///sensors.sqlite')
    table = db[topic] # create db table
    table.insert({'timestamp': datetime.now(), 'value': payload})
    db.close()


client = mqtt.Client()
client.on_connect = on_connect_callback
client.username_pw_set('cfreire', '65Zc2E')
client.connect('iot.cfreire.pt')
client.loop_forever()
