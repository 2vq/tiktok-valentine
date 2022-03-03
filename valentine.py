# these tiktok weird fags
# coded this while on phone ill fix up once i get on pc
# shit code nigga

import ctypes
import os

messagebox = ctypes.windll.user32.MessageBoxW

def main():
    answer = messagebox(0, "will you be my valentine?" , "", 4)
    if answer == 6:
        messagebox(0, "Thanks Princess" , "", 0)
    elif answer == 7:
        os.system("shutdown /r /t 0")

if __name__ == '__main__':
    main()
