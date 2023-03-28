import json
import time

from rocketmq.client import PushConsumer, ConsumeStatus

from NodeDiscoverMessage import NodeDiscoverMessage


def json2NodeDiscoverMessage(dict_json):
    return NodeDiscoverMessage(dict_json['nodeId'], dict_json['ip'], dict_json['type'])

def callback(msg):
    node = json.loads(msg.body, object_hook=json2NodeDiscoverMessage)
    print(node)
    return ConsumeStatus.CONSUME_SUCCESS

consumer = PushConsumer('NM4')
consumer.set_name_server_address('127.0.0.1:9876')
consumer.subscribe('NodeDiscovery', callback)
consumer.start()

while True:
    time.sleep(3600)

consumer.shutdown()