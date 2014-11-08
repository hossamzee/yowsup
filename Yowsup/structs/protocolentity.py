from .protocoltreenode import ProtocolTreeNode
import unittest
class ProtocolEntity(object):
    def __init__(self, tag):
        self.tag = tag

    def getTag(self):
        return self.tag

    def isType(self,  typ):
        return self.tag == typ
    
    def _createProtocolTreeNode(self, attributes, children = None, data = None):
        return ProtocolTreeNode(self.getTag(), attributes, children, data)
        
    
    def toProtocolTreeNode(self):
        pass

    def fromProtocolTreeNode(self, protocolTreeNode):
        pass


class ProtocolEntityTest(unittest.TestCase):
    def setUp(self):
        self.skipTest("override in child classes")

    def test_generation(self):
        entity = self.ProtocolEntity.fromProtocolTreeNode(self.node)
        self.assertEqual(entity.toProtocolTreeNode().toString(), self.node.toString())