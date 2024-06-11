import os
import pyautogui
import pyscreeze
import keyboard as kb
import time
import sys
import uuid
import tkinter.font as tkFont

import ahv

from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
from tkinter import *
from tkinter import ttk
pkeyboard = Controller()

dungeonList = [
  "Hazardous Valley (Awakened)",
  "Hazardous Valley (Hard)",
]
runList = [1, 5, 10, 15, 20, 25, 30]
appFont = "Tahoma 10"

def start():
  choice = dgList.get()

  if (choice == dungeonList[0]):
    ahv.initialize(rootFrame, startButton, macroLbl, runEntry.get()) 

def generateGui():
  # CREATE FRAME
  rootFrame = Tk()
  rootFrame.title("Cabal JTool")
  rootFrame.resizable(0, 0)
  rootFrame.geometry("330x135")

  rootFrame.option_add("*TCombobox*Listbox.font", appFont)
  rootFrame.option_add("*Font", appFont)

  dungeon = Label(rootFrame, text="Dungeon: ")
  dungeon.place(x=10, y=10)

  dgList = ttk.Combobox(values=dungeonList, state="readonly")
  dgList.current(0)
  dgList.config(width=30)
  dgList.place(x=75, y=10)

  runs = Label(rootFrame, text="Runs: ")
  runs.place(x=10, y=43)

  runEntry = ttk.Combobox(values=runList, state="readonly")
  runEntry.current(0)
  runEntry.config(width=5)
  runEntry.place(x=75, y=43)

  startButton = Button(rootFrame, text="Start", command=start)
  startButton.config(width=10)
  startButton.place(x=140, y=40)

  stopButton = Button(rootFrame, text="Stop", state="disabled")
  stopButton.config(width=10)
  stopButton.place(x=230, y=40)

  licenseLbl = Label(rootFrame, text="Status: Activated")
  licenseLbl.place(x=10, y=75)

  expirationLbl = Label(rootFrame, text="Expiration: 00/00/2024")
  expirationLbl.place(x=175, y=75)

  macroLbl = Label(rootFrame, text="Action: --")
  macroLbl.place(x=10, y=105)

  rootFrame.mainloop()

generateGui()
# 1 pyautogui.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 670)
# 2 pyautogui.moveTo(cabalwindow[0] + 430, cabalwindow[1] + 670)
# 3 pyautogui.moveTo(cabalwindow[0] + 470, cabalwindow[1] + 670)
# 4 pyautogui.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 670)
# 5 pyautogui.moveTo(cabalwindow[0] + 540, cabalwindow[1] + 670)
# 6 pyautogui.moveTo(cabalwindow[0] + 570, cabalwindow[1] + 670)
# 7 pyautogui.moveTo(cabalwindow[0] + 610, cabalwindow[1] + 670)
# 8 pyautogui.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 670)
# 9 pyautogui.moveTo(cabalwindow[0] + 680, cabalwindow[1] + 670)
# 10 pyautogui.moveTo(cabalwindow[0] + 715, cabalwindow[1] + 670)
# 11 pyautogui.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 670)
# 12 pyautogui.moveTo(cabalwindow[0] + 790, cabalwindow[1] + 670)