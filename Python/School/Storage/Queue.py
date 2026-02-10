class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        if self.isFull():
            return "Queue is Full"
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    def peak(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0
    def isFull(self):
        return(len(self.queue)) > 4
    def size(self):
        return len(self.queue)
    
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
myQueue.enqueue('D')
myQueue.enqueue('E')
myQueue.enqueue('F')

print("Queue: ", myQueue.queue)
print("Dequeue: ", myQueue.dequeue())
print("Queue after dequeing: ", myQueue.queue)
print("Peak: ", myQueue.peak())
print("isFull: ", myQueue.isFull())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
print("Stack: ", myQueue.queue)