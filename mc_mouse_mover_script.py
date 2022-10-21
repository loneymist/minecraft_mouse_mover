from re import L
import pyautogui
import keyboard
import time
c=0
while True:
    if keyboard.is_pressed("z"):
        c=1
    while c == 1:
            keyboard.press("w")
            keyboard.press("s")
            pyautogui.moveTo(990, 540,duration=1)
            pyautogui.moveTo(930, 540,duration=1)
            keyboard.press("w")
            keyboard.press("s")
            if keyboard.is_pressed("x")==True:
                c=0