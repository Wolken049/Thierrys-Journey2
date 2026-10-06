List = [64, 34, 25, 12, 22, 11, 90, 5, 11, 12, 34, 22, 67, 43, 27, 87, 92, 56, 32]

def merge_sort(List: list):
    if len(List) <= 1:
        return List
    m = len(List) // 2
    a = merge_sort(List[:m])
    b = merge_sort(List[m:])
    r = []

    while a and b:
        if a [0] <= b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))
    return r + a + b

print(merge_sort(List))
