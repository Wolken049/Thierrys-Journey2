myList = [64, 34, 25, 12, 22, 11, 90, 5, 11, 12, 34, 22, 67, 43, 27, 87, 92, 56, 32]

n = len(myList)
for i in range(1,n):
    insert_index = i
    current_value = myList.pop(i)
    for j in range(i-1, -1, -1):
        if myList[j] > current_value:
            insert_index = j
    myList.insert(insert_index, current_value)

print (myList)