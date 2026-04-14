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

def euler(a):
    print(a)
    print(math.e ** a)
    return math.e ** a

def empeuler():
    return math.e

#Functions
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)

def Febonacci(a):
    if a == 0 or a == 1:
        return 1
    else:
        return Febonacci(a-1) + Febonacci(a-2)
def log(a):
    return math.log(a)

def ln(a):
    return (log(a) / log(euler()))
    
def percent(a):
    return a/100
    
#Indicies    
def Inverse(a):
    return a ** -1

def Square(a):
    return a ** 2

def Cube(a):
    return a ** 3

def SqrRoot(a):
    return a ** (1/2)

def CubeRoot(a):
    return a ** (1/3)

def indicies(a, b):
    return a ** b

#Trigonometry
class Trig:
    class Trig1:
        @staticmethod
        def degsine(a):
            return math.sin(math.radians(a))
        
        def degcosine(a):
            return math.cos(math.radians(a))

        def degtangent(a):
            return math.tan(math.radians(a))


        def invdegsine(a):
            return math.degrees(math.asin(a))

        def invdegcosine(a):
            return math.degrees(math.acos(a))

        def invdegtangent(a):
            return math.degrees(math.atan(a))
        
    class Trig2:
        @staticmethod
        def radsine(a):
            return math.sin(a)

        def radcosine(a):
            return math.cos(a)

        def radtangent(a):
            return math.tan(a)
        
        def invradsine(a):
            return math.asin(a)

        def invradcosine(a):
            return math.acos(a)

        def invradtangent(a):
            return math.atan(a)
    class Trig3:
        pass
    class Trig4:
        @staticmethod
        def SinHyp(a):
            return math.sinh(a)
        def CosHyp(a):
            return math.cosh(a)
        def TanHyp(a):
            return math.tanh(a)
        
        def invSinHyp(a):
            return math.asinh(a)
        def invCosHyp(a):
            return math.acosh(a)
        def invTanHyp(a):
            return math.atanh(a)
    
    class Trig5:
        @staticmethod
        def cosec(a):
            return 1 / math.sin(a)
        def sec(a):
            return 1 / math.cos(a)
        def cotangent(a):
            return 1 / math.tan(a)
        
        def invcosec(a):
            return 1 / math.asin(a)
        def invsec(a):
            return 1 / math.acos(a)
        def invcotangent(a):
            return 1 / math.atan(a)
