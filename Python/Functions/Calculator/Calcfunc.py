import math

#Arithmatic
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

#Constants
def pi():
    return math.pi

def euler():
    return math.e

#Functions
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)
    
def percent(a):
    return a/100
    
#Indicies    
def Square(a):
    return a ^ 2

def Cube(a):
    return a ^ 3

def SqrRoot(a):
    return a ^ (1/2)

def CubeRoot(a):
    return a ^ (1/3)

def indicies(a, b):
    return a ^ b

#Trigonometry
def radsine(a):
    return math.sin(a)

def radcosine(a):
    return math.cos(a)

def radtangent(a):
    return math.tan(a)

def degsine(a):
    return math.sin(math.radians(a))

def degcosine(a):
    return math.cos(math.radians(a))

def degtangent(a):
    return math.tan(math.radians(a))

def invradsine(a):
    return math.asin(a)

def invradcosine(a):
    return math.acos(a)

def invradtangent(a):
    return math.atan(a)

def invdegsine(a):
    return math.degrees(math.asin(a))

def invdegcosine(a):
    return math.degrees(math.acos(a))

def invdegtangent(a):
    return math.degrees(math.atan(a))

