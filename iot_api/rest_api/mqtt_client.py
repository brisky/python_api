from datetime import datetime

import paho.mqtt.client as mqtt
import dataset

try:
    from rest_api import redis_helper as r
except ModuleNotFoundError:
    import redis_helper as r

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
    msg_value ={'timestamp': datetime.now(), 'value': payload}

    # redis
    r.put_data(topic, msg_value)

    # Database
    db = dataset.connect('sqlite:///sensors.sqlite3')
    table = db[topic] # create db table
    table.insert(msg_value)
    db.close()


def main():
    r.connect()
    client = mqtt.Client()
    client.on_connect = on_connect_callback
    client.username_pw_set('cfreire', '65Zc2E')
    client.connect('iot.cfreire.pt')
    client.loop_forever()


if __name__ == '__main__':
    main()