Stack_Size = 5
Stack = [0] * Stack_Size
top = -1

def push(item):
    global top
    if top == Stack_Size - 1:
        print("Stack Overflow")  # Changed message for clarity
    else:
        top += 1
        Stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return None
    else:
        item = Stack[top]
        top -= 1
        return item
    
push(50)
push(10)
push(30)
push(40)
push(20)
print(pop())

print(Stack)