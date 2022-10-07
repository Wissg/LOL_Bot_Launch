from pyautogui import *
import pyautogui
import keyboard
import random
import win32api, win32con
from pynput.mouse import Controller, Button
from time import sleep


mouse = Controller()
sleep(5)

def AcceptGame():
    if pyautogui.locateOnScreen('pic\\accept.png')!= None:
        print("accepter")
        x, y = pyautogui.locateCenterOnScreen('pic\\accept.png', confidence=0.9)
        print(f"x={x} y={y}")
        pyautogui.click(x, y)
        sleep(0.5)

while keyboard.is_pressed('q') == False:
    AcceptGame()