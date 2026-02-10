class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
root = TreeNode('R')
NodeA = TreeNode('A')
NodeB = TreeNode('B')
NodeC = TreeNode('C')
NodeD = TreeNode('D')
NodeE = TreeNode('E')
NodeF = TreeNode('F')
NodeG = TreeNode('G')

root.left = NodeA
root.right = NodeB

NodeA.left = NodeC
NodeA.right = NodeD

NodeB.left = NodeE
NodeB.right = NodeF

NodeC.left = NodeG

print("root, right, left, data:", root.right.left.data)