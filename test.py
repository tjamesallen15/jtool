import pyautogui
import pyscreeze
import keyboard as kb
import time
import sys

from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
import ahv

pkeyboard = Controller()

testLoop = True
testVar = False

# dg = input("What to run?")
# print(dg)

# runs = input("How many runs?")
# print(runs)
ahv.runAhv()

# cabalwindow = pyautogui.locateOnScreen('cabalwindow.jpg', grayscale=False, confidence=.5)
# pyautogui.moveTo(cabalwindow[0] + 50, cabalwindow[1] + 15)
# pyautogui.click(cabalwindow[0] + 50, cabalwindow[1] + 15)
# print(cabalwindow)
