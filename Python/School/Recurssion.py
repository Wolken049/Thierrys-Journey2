import random

Numb = []

for i in range (10):
    Numb.append(random.randint(0, 10))
    
print(Numb)

def RecursiveCount(arr, data, index = 0):
    if index == len(arr):
        return 0
    
    if arr[index] == data:
        return 1 + RecursiveCount(arr, data, index + 1)
    else:
        return RecursiveCount(arr, data, index + 1)