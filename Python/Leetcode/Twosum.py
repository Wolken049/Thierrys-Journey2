def Twosum(Numbs : list, Target : int):
    Sum_list = [-1] * 2
    
    try:
        for i in range(len(Numbs)):
            for j in range(len(Numbs)):
                if Numbs[i] != Numbs[j]:
                    if (Numbs[i] + Numbs[j]) == Target:
                        Sum_list[0] = i
                        Sum_list[1] = j
    except Exception:
        print("RunTime")
        
Numbs = [2, 5, 4, 6, 9, 7, 3, 1]
Target = 15

Result = Twosum(Numbs, Target)

print(Result)