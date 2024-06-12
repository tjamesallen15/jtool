import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut
import time
import sys

from tkinter import *
from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
pynboard = Controller()

# GLOBAL VARIABLES
select = 'z'
dash = '1'
fade = '2'
attack = ['3', '4', '5']
buffAttack = ['6']
loot = '7'
fury = '8'
pots = '9'
bmaura = '0'
bm3atk = '-'
bm3 = '='
deselect = Key.esc
lootSpace = Key.space

msgAction = "Action: "