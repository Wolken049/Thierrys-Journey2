from BinaryTree import BinaryTree

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