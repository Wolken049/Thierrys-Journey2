Numb = [5, 3, 4, 7, 8, 6, 0, 9 ,1 , 2]

item = input("Please enter item to be found: ")

found = False

try:
    for i in Numb:
        if Numb[i] == int(item):
            found = True
    if found:
        print("Item found")
    else:
        print("Item not found")
except Exception:
    print("Type a valid number")