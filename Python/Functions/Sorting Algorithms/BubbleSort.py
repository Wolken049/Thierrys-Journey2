def Bubble(Numb):
    n = len(Numb)
    
    for i in range(n - 1):
        for j in range(n-i-1):
            if Numb[j] > Numb[j + 1]:
                Numb[j], Numb[j + 1] = Numb[j + 1], Numb[j]
    return Numb