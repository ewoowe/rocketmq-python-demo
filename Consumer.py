import json
import time

from rocketmq.client import PushConsumer, ConsumeStatus

from NodeDiscoverMessage import json2NodeDiscoverMessage


def callback(msg):
    print(msg.body)
    node = json.loads(msg.body, object_hook=json2NodeDiscoverMessage)
    print('node: nodeId=%s, ip=%s, type=%s' % (node.nodeId, node.ip, node.type))
    return ConsumeStatus.CONSUME_SUCCESS

consumer = PushConsumer('NM4')
consumer.set_name_server_address('127.0.0.1:9876')
consumer.subscribe('NodeDiscovery', callback)
consumer.start()

while True:
    time.sleep(3600)

consumer.shutdown()