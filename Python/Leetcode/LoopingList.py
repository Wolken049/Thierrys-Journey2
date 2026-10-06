class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

    def SetNext(self, NewNode):
        self.Next = NewNode

    def GetData(self):
        return self.Data

    def GetNext(self):
        return self.Next

class LinkedList:
    def __init__(self):
        self.Root = None

    def AddNode(self, NewNode : Node):
        CurrentNode = self.Root
        Added = False
        if self.Root is None:
            self.Root = NewNode
            CurrentNode = NewNode
        else:
            while not Added:
                if CurrentNode.GetNext() is None:
                    CurrentNode.SetNext(NewNode)
                    Added = True
                else:
                    CurrentNode = CurrentNode.GetNext()
    def RemoveNode(self):
        PreviousNode = self.Root
        CurrentNode = self.Root
        Removed = False
        if self.Root is None:
            return "List is already Empty"
        else:
            while not Removed:
                if CurrentNode.GetNext() is None:
                    del CurrentNode
                    PreviousNode.SetNext(None)
                    Removed = True
                else:
                    PreviousNode = CurrentNode
                    CurrentNode = CurrentNode.GetNext()

    def PrintList(self):
        End = False
        Output = f""
        if self.Root is None:
            print("List is empty")
        else:
            CurrentNode = self.Root
            while not End:
                Output += f"{CurrentNode.GetData()} "
                if CurrentNode.GetNext() is None:
                    End = True
                else:
                    CurrentNode = CurrentNode.GetNext()
            print(Output)

Node1 = Node(2)
Node2 = Node(5)
Node3 = Node(9)
Node4 = Node(14)
Node5 = Node(18)
Node6 = Node(20)

List = LinkedList()
List.PrintList()
List.AddNode(Node1)
List.AddNode(Node2)
List.AddNode(Node3)
List.AddNode(Node4)
List.AddNode(Node5)
List.AddNode(Node6)
List.PrintList()
List.RemoveNode()
List.PrintList()
print(Node5.GetNext())
