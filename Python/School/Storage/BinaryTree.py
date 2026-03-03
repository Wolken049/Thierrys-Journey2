from OrderTree import *

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.item, end = " ")
            self.inordertraversal(node.right)
        
    def preorder_traversal(self, node):
        if node is not None:
            print(node.item, end = " ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postordertraversal(node.right)
            print(node.item, item = " ")
        
        
Tree = BinaryTree()

for value in [27, 15, 35, 10, 20, 30, 40]:
    Tree.insert(value)
    
Tree.inorder_traversal(Tree.root)