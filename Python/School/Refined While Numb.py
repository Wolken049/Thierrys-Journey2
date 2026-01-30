count = 0
Num = 0
while Num != -1:
    try:
        count += 1
        num = int(input("Please enter a number: "))
    except Exception:
        print("Error")