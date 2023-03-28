import json

from rocketmq.client import Producer, Message

from NodeDiscoverMessage import nodes, NodeDiscoverMessage2json

producer = Producer('nokiaAdapter||mano')
producer.set_name_server_address('127.0.0.1:9876')
producer.start()

for node in nodes:
    msg = Message('NodeDiscovery')
    json = json.dumps(node, default=NodeDiscoverMessage2json)
    print(json)
    msg.set_body(json)
    ret = producer.send_sync(msg)
producer.shutdown()
