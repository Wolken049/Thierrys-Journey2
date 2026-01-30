class SearchNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inOrderTraversal(node):
        if node is None:
            return
        inOrderTraversal(node.left)
        print(node.data, end=", ")
        inOrderTraversal(node.right)

root = SearchNode(13)
node7 = SearchNode(7)
node15 = SearchNode(15)
node3 = SearchNode(3)
node8 = SearchNode(8)
node14 = SearchNode(14)
node19 = SearchNode(19)
node18 = SearchNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

inOrderTraversal(root)