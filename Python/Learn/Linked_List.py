class Linked_List:
    
    class Node:
        def __init__(self, node):
            self.node = node
            self.next = None
    
    def __init__(self):
        self.Head = None
    
    def Add_Node(self, new_node):
        self.New_node = new_node
        
        if self.Head is None:
            self.Head = new_node
        
        else:
            Current = self.Head
            while Current.next:
                Current = Current.next
            Current.next = new_node
    
    def Traverse(self):
        Current = self.Head
        
        while Current:
            print(Current.node)
            Current = Current.next
    
    def Remove(self, Remove_Node):
        Current = self.Head
        Previous = None
        while Current:
            if Current.node == Remove_Node:
                if Previous is None:
                    self.Head = Current.next
                else:
                    Previous.next = Current.next    
                return True
            
            Previous = Current
            Current = Current.next
        return False
    
    def Lowest(self):
        head = self.Head
        min_value = head.node
        current_node = head.next
        while current_node:
            if current_node.node < min_value:
                min_value = current_node.node
            current_node = current_node.next
        return min_value

my_list = Linked_List()
for x in range(6):
    Input = Linked_List.Node(f"Node{x}")
    my_list.Add_Node(Input)
my_list.Traverse()
print(my_list.Lowest())