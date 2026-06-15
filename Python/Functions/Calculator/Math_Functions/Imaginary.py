def Imaginary_Numbers(n): #Insert indicies of i only
    if n % 2 == 0:
        if n % 4 == 0:
            return 1
        else:
            return -1
    else:
        Value = Imaginary_Numbers(n-1)
        if Value == 1:
            return "i"
        else:
            return "-i"
        
print(Imaginary_Numbers(61))

