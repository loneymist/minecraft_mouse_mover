import pyautogui
import keyboard
c=0
while True:
    if keyboard.is_pressed("z"):
        c=1
    if keyboard.is_pressed("x"):
        c = 0
    while c == 1:
        pyautogui.moveTo(1000, 600,duration=2)
        pyautogui.moveTo(1100, 605,duration=2)
