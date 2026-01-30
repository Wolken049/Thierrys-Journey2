def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high]