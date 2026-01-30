class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = Tree(9)
NodeA = Tree(3)
NodeB = Tree(5)
NodeC = Tree(2)
NodeD = Tree(1)
NodeE = Tree(7)
NodeF = Tree(8)
NodeG = Tree(4)
NodeH = Tree(6)

root.left = NodeA
root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF

NodeC.left = NodeG
NodeC.right = NodeH

min_pointer = root

class MinHeap:
    def __init__(self):
        self.root = None
        self.node = []
        self.min_pointer = None
        
    def insert(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)
        
print(min_pointer.data)