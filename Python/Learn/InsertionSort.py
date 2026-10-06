myList = [64, 34, 25, 12, 22, 11, 90, 5, 11, 12, 34, 22, 67, 43, 27, 87, 92, 56, 32]

def insertion_sort(arr: list) -> list:
    # Outer loop starts at index 1 because a single element (index 0) is already sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements larger than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element right
            j -= 1  # Move left to compare the next element

        # Insert key into the empty spot created by shifting
        arr[j + 1] = key
        print(arr)

    return arr

print("Sorted Array:", insertion_sort(myList))
