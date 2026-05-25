import ctypes
import os
import random
def Shutdown():
    ctypes.windll.user32.MessageBoxW(0, "Your laptop will shut down at any time and you will never know til it is too late", "Achtung", 0x30)

    Time = random.randint(1, 43200)

    os.system(f"shutdown /s /t {Time} > nul 2>&1")
