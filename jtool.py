import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut
import os
import time
import sys
import uuid
import tkinter.font as tkFont

import ahv

from tkinter import *
from tkinter import ttk
from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
pynboard = Controller()

dungeonList = [
  "Hazardous Valley (Awakened)"
  # "Hazardous Valley (Hard)",
  # "Hazardous Valley (Medium)",
  # "Hazardous Valley (Easy)",
]
runList = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30]
# runList = [1, 2, 3, 4, 5]
bmList = [1, 0]
buffList = [1, 0]
shortList = [1, 0]
appFont = "Tahoma 10"

dgList = []
runEntry = []
bmTwo = []
buffs = []
shorts = []
startButton = []
macroLbl = []
runNumberLbl = []
rootFrame = []

def start():
  choice = dgList.get()

  if (choice == dungeonList[0]):
    ahv.initialize(rootFrame, startButton, macroLbl, runNumberLbl, bmTwo.get(), buffs.get(), shorts.get(), runEntry.get())

def generateGui():
  # CREATE FRAME
  global rootFrame
  rootFrame = Tk()
  rootFrame.title("Cabal JTool v2.10")
  rootFrame.resizable(0, 0)
  rootFrame.geometry("330x165")

  rootFrame.option_add("*TCombobox*Listbox.font", appFont)
  rootFrame.option_add("*Font", appFont)

  dungeon = Label(rootFrame, text="Dungeon: ")
  dungeon.place(x=10, y=10)

  global dgList
  dgList = ttk.Combobox(values=dungeonList, state="readonly")
  dgList.current(0)
  dgList.config(width=30)
  dgList.place(x=75, y=10)

  runsLbl = Label(rootFrame, text="Runs: ")
  runsLbl.place(x=10, y=43)

  global runEntry
  runEntry = ttk.Combobox(values=runList, state="readonly")
  runEntry.current(0)
  runEntry.config(width=5)
  runEntry.place(x=75, y=43)

  global startButton
  startButton = Button(rootFrame, text="Start", command=start)
  startButton.config(width=10)
  startButton.place(x=230, y=40)
  # startButton.place(x=140, y=40)

  global runNumberLbl
  runNumberLbl = Label(rootFrame, text="Run #: --")
  runNumberLbl.place(x=140, y=43)

  # stopButton = Button(rootFrame, text="Stop", state="disabled")
  # stopButton.config(width=10)
  # stopButton.place(x=230, y=40)

  askBmLbl = Label(rootFrame, text="Mode 2: ")
  askBmLbl.place(x=10, y=75)

  global bmTwo
  bmTwo = ttk.Combobox(values=bmList, state="readonly")
  bmTwo.current(1)
  bmTwo.config(width=5)
  bmTwo.place(x=75, y=75)

  licenseLbl = Label(rootFrame, text="Status: Trial")
  licenseLbl.place(x=140, y=75)

  askBuffs = Label(rootFrame, text="Buffs: ")
  askBuffs.place(x=10, y=105)

  global buffs
  buffs = ttk.Combobox(values=buffList, state="readonly")
  buffs.current(0)
  buffs.config(width=5)
  buffs.place(x=75, y=105)

  expirationLbl = Label(rootFrame, text="Expiration: 12/12/2024")
  expirationLbl.place(x=140, y=105)

  askShorts = Label(rootFrame, text="Shorts: ")
  askShorts.place(x=10, y=135)

  global shorts
  shorts = ttk.Combobox(values=shortList, state="readonly")
  shorts.current(0)
  shorts.config(width=5)
  shorts.place(x=75, y=135)

  global macroLbl
  macroLbl = Label(rootFrame, text="Action: --")
  macroLbl.place(x=140, y=135)

  rootFrame.mainloop()

## GENERATE MAIN
generateGui()

# cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
# pyauto.moveTo(cabalwindow[0] + 50, cabalwindow[1] + 15)
# pyauto.click(cabalwindow[0] + 50, cabalwindow[1] + 15)


