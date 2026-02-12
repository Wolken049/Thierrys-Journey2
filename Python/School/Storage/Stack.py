class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        if self.isFull() + 1:
            return "Stack is Full"
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def isFull(self):
        return len(self.stack) >= 4
    def size(self):
        return len(self.stack)
    
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
myStack.push('D')
myStack.push('E')
myStack.push('F')
    
print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("isFull: ", myStack.isFull())
print("Size: ", myStack.size())
print("Stack: ", myStack.stack)