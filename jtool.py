import os
import time
import sys
import uuid
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller
import pyautogui as pyauto
import pygetwindow as pywin
import pyscreeze
import keyboard as shortcut

import util
import macro.hva as hva
import macro.hvenh as hvenh
import macro.sca as sca
import macro.hw as hw
import macro.cfa as cfa
import macro.lha as lha
import macro.tm as tm
import macro.pca as pca
import macro.hk as hk
import macro.s1p as s1p
pynboard = Controller()

LIST_MASTER = [
  "Hazardous Valley (Awakened)",
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)",
  "Steamer Crazy (Awakened)",
  "Catacomb Frost (Awakened)",
  "Lava Hellfire (Awakened)",
  "Holy Windmill",
  "Terminus Machina",
  "Panic Cave (Awakened)",
  "Holy Keldrasil",
  "Altar of Siena B1F (Prideus)"
]

LIST_DUNGEON = [
  "Hazardous Valley (Awakened)",
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)",
  "Steamer Crazy (Awakened)",
  "Catacomb Frost (Awakened)",
  "Lava Hellfire (Awakened)",
  "Holy Windmill",
  "Terminus Machina",
  "Panic Cave (Awakened)",
  "Holy Keldrasil",
  "Altar of Siena B1F (Prideus)"
]

LIST_RUN = [1, 5, 10, 20, 30, 40, 50, 100]

list_dg = []
btn_start = []
btn_pause = []
lbl_macro = []
lbl_current_run = []
frame_root = []
val_run_count = []

val_mode = 0
val_buffs = 1
val_shorts = 1
val_atk_type = 0
val_vera = 0
val_party = 0
val_leader = 0

def start():
  cabalwindow = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  choice = list_dg.get()
  mode = val_mode.get()
  buff = val_buffs.get()
  short = val_shorts.get()
  runs = val_run_count.get()
  atk_type = val_atk_type.get()
  vera = val_vera.get()
  party = val_party.get()
  leader = val_leader.get()

  util.initialize(cabalwindow, frame_root, lbl_macro, lbl_current_run)
  util.set_variables(mode, buff, short, atk_type, vera, party, leader, runs)

  if (choice == LIST_MASTER[0]):
    hva.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[1] or choice == LIST_MASTER[2] or choice == LIST_MASTER[3]):
    hvenh.initialize(frame_root, btn_start, choice, runs)
  elif (choice == LIST_MASTER[4]):
    sca.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[5]):
    cfa.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[6]):
    lha.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[7]):
    hw.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[8]):
    tm.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[9]):
    pca.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[10]):
    hk.initialize(frame_root, btn_start, runs)
  elif (choice == LIST_MASTER[11]):
    s1p.initialize(frame_root, btn_start, runs)

def buy_fury():
  btn_start.config(state="disabled")
  btn_pause.config(state="disabled")
  frame_root.update()
  cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  util.set_cabal_window(cabalwindow)
  util.go_cabal_window()

  for x in range(170):
    util.move_click(125, 205)
    print("Click #: " + str(x))

  btn_start.config(state="active")
  btn_pause.config(state="active")
  frame_root.update()

def generate_gui():
  # CREATE FRAME
  global frame_root
  frame_root = Tk()
  frame_root.title(util.APP_FULL_NAME)
  frame_root.resizable(0, 0)
  frame_root.geometry(util.APP_FRAME_SIZE)

  img_photo = PhotoImage(file = util.IMG_APP_ICON)
  frame_root.iconphoto(False, img_photo)

  frame_root.option_add("*TCombobox*Listbox.font", util.APP_FONT)
  frame_root.option_add("*Font", util.APP_FONT)
  # frame_root.eval('tk::PlaceWindow . right')

  lbl_dungeon_list = Label(frame_root, text="Dungeon: ")
  lbl_dungeon_list.place(x=10, y=10)

  global list_dg
  list_dg = ttk.Combobox(values=LIST_DUNGEON, state="readonly")
  list_dg.current(0)
  list_dg.config(width=30)
  list_dg.place(x=75, y=10)

  lbl_runs = Label(frame_root, text="Runs: ")
  lbl_runs.place(x=10, y=43)

  global val_run_count
  val_run_count = ttk.Combobox(values=LIST_RUN, state="")
  val_run_count.current(0)
  val_run_count.config(width=5)
  val_run_count.place(x=75, y=43)

  global btn_start
  btn_start = Button(frame_root, text="Start", command=start)
  btn_start.config(width=10)
  btn_start.place(x=230, y=40)

  global btn_pause
  btn_pause = Button(frame_root, text="Fury", command=buy_fury)
  btn_pause.config(width=10)
  btn_pause.place(x=145, y=40)

  global lbl_current_run
  lbl_current_run = Label(frame_root, text="Run #: --")
  lbl_current_run.place(x=140, y=105)

  lbl_mode = Label(frame_root, text="Mode II: ")
  lbl_mode.place(x=10, y=75)

  global val_mode
  val_mode = IntVar(value=0)
  chkbtn_mode = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_mode)
  chkbtn_mode.place(x=75, y=76)

  lbl_party = Label(frame_root, text="Party: ")
  lbl_party.place(x=140, y=75)

  global val_party
  val_party = IntVar(value=0)
  chkbtn_party = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_party)
  chkbtn_party.place(x=185, y=76)

  lbl_leader = Label(frame_root, text="Leader: ")
  lbl_leader.place(x=235, y=75)

  global val_leader
  val_leader = IntVar(value=0)
  chkbtn_leader = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_leader)
  chkbtn_leader.place(x=293, y=76)

  lbl_license = Label(frame_root, text="Status: Free")
  lbl_license.place(x=140, y=135)

  lbl_shorts = Label(frame_root, text="Buffs: ")
  lbl_shorts.place(x=10, y=105)

  global val_buffs
  val_buffs = IntVar(value=1)
  chkbtn_buffs = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_buffs)
  chkbtn_buffs.place(x=75, y=106)

  lbl_expiration = Label(frame_root, text="Expiration: 12/12/2024")
  lbl_expiration.place(x=140, y=165)

  lbl_shorts = Label(frame_root, text="Shorts: ")
  lbl_shorts.place(x=10, y=135)

  global val_shorts
  val_shorts = IntVar(value=1)
  chkbtn_shorts = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_shorts)
  chkbtn_shorts.place(x=75, y=136)

  global lbl_macro
  lbl_macro = Label(frame_root, text="Action: --")
  lbl_macro.place(x=140, y=195)

  lbl_atk_type = Label(frame_root, text="Range: ")
  lbl_atk_type.place(x=10, y=165)

  global val_atk_type
  val_atk_type = IntVar(value=0)
  chkbtn_atk_type = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0,
    variable=val_atk_type)
  chkbtn_atk_type.place(x=75, y=166)

  lbl_vera = Label(frame_root, text="Veradrix:")
  lbl_vera.place(x=10, y=195)

  global val_vera
  val_vera = IntVar(value=0)
  chkbtn_vera = ttk.Checkbutton(frame_root, text="", onvalue=1, offvalue=0, variable=val_vera)
  chkbtn_vera.place(x=75, y=196)

  frame_root.mainloop()

# GENERATE MAIN
generate_gui()
