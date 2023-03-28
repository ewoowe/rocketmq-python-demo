import json

from rocketmq.client import Producer, Message

from NodeDiscoverMessage import nodes

producer = Producer('nokiaAdapter||mano')
producer.set_name_server_address('127.0.0.1:9876')
producer.start()

for node in nodes:
    msg = Message('NodeDiscovery')
    msg.set_body(json.dumps(node.__dict__))
    ret = producer.send_sync(msg)
producer.shutdown()
