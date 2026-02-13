import math

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * math.factorial(a - 1)