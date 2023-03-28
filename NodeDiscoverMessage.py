from enum import Enum

NodeType = Enum('NodeType', ('CN_TP_Nokia_FDDLTE', 'CN_TP_Nokia_5GNR', 'AN_TP_Nokia_FDDLTE', 'AN_TP_Nokia_5GNR',
                             'AN_ICTNJ_FDDLTE', 'AN_ICTNJ_5GNR', 'AN_ICTNJ_NORMAL'))


class NodeDiscoverMessage():
    nodeId: str = None
    ip: str = None
    type: NodeType = None

    def __init__(self, nodeId, ip, type):
        self.nodeId = nodeId
        self.ip = ip
        self.type = type

def json2NodeDiscoverMessage(dict_json):
    return NodeDiscoverMessage(dict_json['nodeId'], dict_json['ip'], dict_json['type'])

def NodeDiscoverMessage2json(node):
    return {
        'nodeId': node.nodeId,
        'ip': node.ip,
        'type': node.type.name
    }

node1 = NodeDiscoverMessage('1', '127.0.0.1', NodeType.CN_TP_Nokia_FDDLTE)
node2 = NodeDiscoverMessage('2', '127.0.0.2', NodeType.CN_TP_Nokia_5GNR)
node3 = NodeDiscoverMessage('3', '127.0.0.3', NodeType.AN_TP_Nokia_FDDLTE)
node4 = NodeDiscoverMessage('4', '127.0.0.4', NodeType.AN_TP_Nokia_5GNR)
node5 = NodeDiscoverMessage('5', '127.0.0.5', NodeType.AN_ICTNJ_FDDLTE)
node6 = NodeDiscoverMessage('6', '127.0.0.6', NodeType.AN_ICTNJ_5GNR)
node7 = NodeDiscoverMessage('7', '127.0.0.7', NodeType.AN_ICTNJ_NORMAL)
nodes = [node1, node2, node3, node4, node5, node6, node7]
