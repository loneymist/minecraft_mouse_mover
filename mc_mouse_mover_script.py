from re import L
import pyautogui
import keyboard
import time
c=0
while True:
    if keyboard.is_pressed("="):
        c=1
    while c == 1:
            keyboard.press("w")
            time.sleep(0.15)
            keyboard.release("w")
            pyautogui.moveTo(960, 540,duration=0.2)
            keyboard.press("s")
            time.sleep(0.3)
            keyboard.release("s")
            pyautogui.moveTo(990, 540,duration=0.2)
            pyautogui.moveTo(930, 540,duration=0.2)
            pyautogui.moveTo(960, 540,duration=0.2)
            if keyboard.is_pressed("x")==True:
                c=0