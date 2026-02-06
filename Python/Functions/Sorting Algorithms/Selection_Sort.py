def Selection(arr):
    n = len(arr)
    
    for i in range (n - 1):
        mid = i
        for j in range (i+1, n):
            if arr[j] < arr[mid]:
                mid = j
    mid
                