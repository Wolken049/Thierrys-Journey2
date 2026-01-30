def dice():
    import random
    import os
    x = random.randint(1, 6)
    if x == 1:
        return "You rolled a 1!"
    else:
        return "Careful"

print(dice())
