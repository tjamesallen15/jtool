import pyautogui as pyauto
import pygetwindow as pywin
import pyscreeze
import keyboard as shortcut
import os
import time
import sys
import uuid
import tkinter.font as tkFont

import util
import macro.hva as hva
import macro.hvenh as hvenh
import macro.sca as sca
import macro.hw as hw
import macro.cfa as cfa
import macro.lha as lha
import macro.tm as tm
import macro.pca as pca

from tkinter import *
from tkinter import ttk
from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
pynboard = Controller()

masterList = [
  "Hazardous Valley (Awakened)",
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)",
  "Steamer Crazy (Awakened)",
  "Catacomb Frost (Awakened)",
  "Lava Hellfire (Awakened)",
  "Holy Windmill",
  "Terminus Machina",
  "Panic Cave (Awakened)"
]
dungeonList = [
  "Hazardous Valley (Awakened)",
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)",
  "Steamer Crazy (Awakened)",
  "Catacomb Frost (Awakened)",
  "Lava Hellfire (Awakened)",
  "Holy Windmill",
  "Terminus Machina",
  "Panic Cave (Awakened)"
]
runList = [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50]
bmList = [1, 0]
buffList = [1, 0]
shortList = [1, 0]
appFont = "Tahoma 10"

frameSize = "330x230"
appName = "Cabal JTool "
version = "v4.95"
appFullName = appName + version
dgList = []
runCount = []
startButton = []
macroLbl = []
runNumberLbl = []
rootFrame = []
battlemode = 0
buffs = 1
shorts = 1
atk = 0
veras = 0

def start():
  cabalwindow = pyauto.locateOnScreen(util.imgCabalWindow, grayscale=False, confidence=.9)
  choice = dgList.get()
  mode = battlemode.get()
  buff = buffs.get()
  short = shorts.get()
  runs = runCount.get()
  atktype = atk.get()
  vera = veras.get()

  util.initialize(cabalwindow, rootFrame, macroLbl, runNumberLbl)
  util.setVariables(mode, buff, short, atktype, vera)

  if (choice == masterList[0]):
    hva.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[1] or choice == masterList[2] or choice == masterList[3]):
    hvenh.initialize(rootFrame, startButton, choice, runs)
  elif (choice == masterList[4]):
    sca.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[5]):
    cfa.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[6]):
    lha.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[7]):
    hw.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[8]):
    tm.initialize(rootFrame, startButton, runs)
  elif (choice == masterList[9]):
    pca.initialize(rootFrame, startButton, runs)

def generateGui():
  # CREATE FRAME
  global rootFrame
  rootFrame = Tk()
  rootFrame.title(appFullName)
  rootFrame.resizable(0, 0)
  rootFrame.geometry(frameSize)

  photo = PhotoImage(file = util.imgAppIcon)
  rootFrame.iconphoto(False, photo)

  rootFrame.option_add("*TCombobox*Listbox.font", appFont)
  rootFrame.option_add("*Font", appFont)

  dungeon = Label(rootFrame, text="Dungeon: ")
  dungeon.place(x=10, y=10)

  global dgList
  dgList = ttk.Combobox(values=dungeonList, state="readonly")
  dgList.current(7)
  dgList.config(width=30)
  dgList.place(x=75, y=10)

  runsLbl = Label(rootFrame, text="Runs: ")
  runsLbl.place(x=10, y=43)

  global runCount
  runCount = ttk.Combobox(values=runList, state="readonly")
  runCount.current(0)
  runCount.config(width=5)
  runCount.place(x=75, y=43)

  global startButton
  startButton = Button(rootFrame, text="Start", command=start)
  startButton.config(width=10)
  startButton.place(x=230, y=40)

  # var = IntVar(value=1)
  # checkbutton = ttk.Checkbutton(rootFrame, text="", 
  #   onvalue=1, offvalue=0, variable=var)
  # checkbutton.place(x=230, y=75)
  # print("TEST: " + str(var.get()))
  # startButton.place(x=140, y=40)

  global runNumberLbl
  runNumberLbl = Label(rootFrame, text="Run #: --")
  runNumberLbl.place(x=140, y=75)

  # stopButton = Button(rootFrame, text="Stop", state="disabled")
  # stopButton.config(width=10)
  # stopButton.place(x=230, y=40)

  askBmLbl = Label(rootFrame, text="Mode II: ")
  askBmLbl.place(x=10, y=75)

  # global bmTwo
  # bmTwo = ttk.Combobox(values=bmList, state="readonly")
  # bmTwo.current(1)
  # bmTwo.config(width=5)
  # bmTwo.place(x=75, y=75)

  global battlemode
  battlemode = IntVar(value=0)
  chkBtnMode = ttk.Checkbutton(rootFrame, text="", onvalue=1, offvalue=0, variable=battlemode)
  chkBtnMode.place(x=75, y=76)

  licenseLbl = Label(rootFrame, text="Status: Free")
  licenseLbl.place(x=140, y=105)

  shortsLbl = Label(rootFrame, text="Buffs: ")
  shortsLbl.place(x=10, y=105)

  global buffs
  buffs = IntVar(value=0)
  chkBtnBuffs = ttk.Checkbutton(rootFrame, text="", onvalue=1, offvalue=0, variable=buffs)
  chkBtnBuffs.place(x=75, y=106)
  # buffs = ttk.Combobox(values=buffList, state="readonly")
  # buffs.current(0)
  # buffs.config(width=5)
  # buffs.place(x=75, y=105)

  expirationLbl = Label(rootFrame, text="Expiration: 12/12/2024")
  expirationLbl.place(x=140, y=135)

  askShorts = Label(rootFrame, text="Shorts: ")
  askShorts.place(x=10, y=135)

  global shorts
  shorts = IntVar(value=0)
  chkBtnShorts = ttk.Checkbutton(rootFrame, text="", onvalue=1, offvalue=0, variable=shorts)
  chkBtnShorts.place(x=75, y=136)
  # shorts = ttk.Combobox(values=shortList, state="readonly")
  # shorts.current(0)
  # shorts.config(width=5)
  # shorts.place(x=75, y=135)

  global macroLbl
  macroLbl = Label(rootFrame, text="Action: --")
  macroLbl.place(x=140, y=165)

  atkLbl = Label(rootFrame, text="Range: ")
  atkLbl.place(x=10, y=165)

  global atk
  atk = IntVar(value=0)
  checkBtnAtk = ttk.Checkbutton(rootFrame, text="", onvalue=1, offvalue=0, variable=atk)
  checkBtnAtk.place(x=75, y=166)

  global veraLbl
  veraLbl = Label(rootFrame, text="Veradrix:")
  veraLbl.place(x=10, y=195)

  global veras
  veras = IntVar(value=0)
  checkBtnVera = ttk.Checkbutton(rootFrame, text="", onvalue=1, offvalue=0, variable=veras)
  checkBtnVera.place(x=75, y=196)

  rootFrame.mainloop()

# GENERATE MAIN
generateGui()
