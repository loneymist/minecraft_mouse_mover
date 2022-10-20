import pyautogui
import keyboard
import mouse
c=0
while True:
    if keyboard.is_pressed("z"):
        c=1
    while c == 1:

            pyautogui.moveTo(990, 540,duration=1)
            pyautogui.moveTo(930, 540,duration=1)
            if keyboard.is_pressed("x")==True:
                c=0
