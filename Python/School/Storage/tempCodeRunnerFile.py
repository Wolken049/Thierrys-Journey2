def preorder_traversal(self, node):
        if node is not None:
            print(node.item, end = " ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)