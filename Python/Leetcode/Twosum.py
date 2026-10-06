Array = [2, 3, 4, 6, 9, 30]

def Two_sum(Array, answer):
    Left = 0
    Right = len(Array) - 1

    while True:
        sum = Array[Left] + Array[Right]
        if sum == answer:
            return (Left, Right)
        elif sum < answer:
            Left += 1
        elif sum > answer:
            Right -= 1
        else:
            return "No sum found"

print(Two_sum(Array, 10))
