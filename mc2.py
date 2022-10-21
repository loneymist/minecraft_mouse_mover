from re import L
import pyautogui
import keyboard
import time
c=0
while True:
    if keyboard.is_pressed("z"):
        c=1
    while c == 1:
            time.sleep(1)
            keyboard.press("a")
            keyboard.press("d")
            time.sleep(1)
            if keyboard.is_pressed("x")==True:
                c=0