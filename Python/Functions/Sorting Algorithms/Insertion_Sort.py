def InsertSort(a):
    n = len(a)
    for i in range(1, n):
        insert_index = i
        current_value = a[i]
        for j in range(i-1, -1, -1):
            if a[j] > current_value:
                a[j + 1] = a[j]
                insert_index = j
            else:
                break
        a[insert_index] = current_value
    return a