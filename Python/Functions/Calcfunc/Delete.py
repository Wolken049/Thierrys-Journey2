def Add(a, b):
    return a + b
def Sub(a, b):
    return a - b
def Multi(a, b):
    return a * b
def Div(a, b):
    return a / b

print("Welcome to Basic calculator")
Numb1 = float(input("Enter Numb1: "))
Numb2 = float(input("Enter Numb2: "))

Ans = input("Would you like to Add, Subtract, Multiply or Divide: ")

match Ans.lower(): #Thanks 
    case "add":
        print(Add(Numb1, Numb2))
    case "subtract":
        print(Sub(Numb1, Numb2))
    case "multiply":
        print(Multi(Numb1, Numb2))
    case "divide":
        print(Div(Numb1, Numb2))
        
#Ok it works