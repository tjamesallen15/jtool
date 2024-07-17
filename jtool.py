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
LIST_CLICKS = [10, 20, 30, 40, 50, 100, 200, 500]

list_dg = []
btn_start = []
btn_pause = []
btn_fury = []
btn_force = []
btn_upgrade = []
btn_mails = []
lbl_macro = []
lbl_misc = []
lbl_current_run = []
frame_root = []
val_run_count = []
val_click_count = []

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
  btn_fury.config(state="disabled")
  frame_root.update()
  cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  util.set_cabal_window(cabalwindow)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(125, 205)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_fury.config(state="active")
  frame_root.update()

def buy_upgrade():
  btn_upgrade.config(state="disabled")
  frame_root.update()
  cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  util.set_cabal_window(cabalwindow)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(15, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_upgrade.config(state="active")
  frame_root.update()

def buy_force():
  btn_force.config(state="disabled")
  frame_root.update()
  cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  util.set_cabal_window(cabalwindow)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(45, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_force.config(state="active")
  frame_root.update()

def get_mails():
  btn_mails.config(state="disabled")
  frame_root.update()
  cabalwindow = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  util.set_cabal_window(cabalwindow)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(510, 310, 0.5)
    util.move_click(510, 525, 0.5)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_mails.config(state="active")
  frame_root.update()

def log_misc_action(message):
  msgBuilder = StringVar()
  msgBuilder = util.MSG_ACTION + message
  print(msgBuilder)
  lbl_misc.config(text=msgBuilder)
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

  tab_control = ttk.Notebook(frame_root)
  tab_dungeon = ttk.Frame(tab_control)
  tab_misc = ttk.Frame(tab_control)
  tab_control.add(tab_dungeon, text ='Dungeon')
  tab_control.add(tab_misc, text ='Misc')
  tab_control.pack(expand = 1, fill ="both")

  # Tab Dungeon
  lbl_dungeon_list = Label(tab_dungeon, text="Dungeon: ")
  lbl_dungeon_list.place(x=10, y=10)

  global list_dg
  list_dg = ttk.Combobox(tab_dungeon, values=LIST_DUNGEON, state="readonly")
  list_dg.current(0)
  list_dg.config(width=30)
  list_dg.place(x=75, y=10)

  lbl_runs = Label(tab_dungeon, text="Runs: ")
  lbl_runs.place(x=10, y=43)

  global val_run_count
  val_run_count = ttk.Combobox(tab_dungeon, values=LIST_RUN, state="")
  val_run_count.current(0)
  val_run_count.config(width=5)
  val_run_count.place(x=75, y=43)

  global btn_start
  btn_start = Button(tab_dungeon, text="Start", command=start)
  btn_start.config(width=10)
  btn_start.place(x=230, y=40)

  # global btn_fury
  # btn_fury = Button(tab_dungeon, text="Fury", command=buy_fury)
  # btn_fury.config(width=10)
  # btn_fury.place(x=145, y=40)

  global lbl_current_run
  lbl_current_run = Label(tab_dungeon, text="Run #: --")
  lbl_current_run.place(x=140, y=105)

  lbl_mode = Label(tab_dungeon, text="Mode II: ")
  lbl_mode.place(x=10, y=75)

  global val_mode
  val_mode = IntVar(value=0)
  chkbtn_mode = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_mode)
  chkbtn_mode.place(x=75, y=76)

  lbl_party = Label(tab_dungeon, text="Party: ")
  lbl_party.place(x=140, y=75)

  global val_party
  val_party = IntVar(value=0)
  chkbtn_party = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_party)
  chkbtn_party.place(x=185, y=76)

  lbl_leader = Label(tab_dungeon, text="Leader: ")
  lbl_leader.place(x=235, y=75)

  global val_leader
  val_leader = IntVar(value=0)
  chkbtn_leader = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_leader)
  chkbtn_leader.place(x=293, y=76)

  lbl_license = Label(tab_dungeon, text="Status: Free")
  lbl_license.place(x=140, y=135)

  lbl_shorts = Label(tab_dungeon, text="Buffs: ")
  lbl_shorts.place(x=10, y=105)

  global val_buffs
  val_buffs = IntVar(value=1)
  chkbtn_buffs = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_buffs)
  chkbtn_buffs.place(x=75, y=106)

  lbl_expiration = Label(tab_dungeon, text="Expiration: 12/12/2024")
  lbl_expiration.place(x=140, y=165)

  lbl_shorts = Label(tab_dungeon, text="Shorts: ")
  lbl_shorts.place(x=10, y=135)

  global val_shorts
  val_shorts = IntVar(value=1)
  chkbtn_shorts = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_shorts)
  chkbtn_shorts.place(x=75, y=136)

  global lbl_macro
  lbl_macro = Label(tab_dungeon, text="Action: --")
  lbl_macro.place(x=140, y=195)

  lbl_atk_type = Label(tab_dungeon, text="Range: ")
  lbl_atk_type.place(x=10, y=165)

  global val_atk_type
  val_atk_type = IntVar(value=0)
  chkbtn_atk_type = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0,
    variable=val_atk_type)
  chkbtn_atk_type.place(x=75, y=166)

  lbl_vera = Label(tab_dungeon, text="Veradrix:")
  lbl_vera.place(x=10, y=195)

  global val_vera
  val_vera = IntVar(value=0)
  chkbtn_vera = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_vera)
  chkbtn_vera.place(x=75, y=196)

  # Tab Misc
  lbl_step = Label(tab_misc, text="Open NPC Store before clicking the buy buttons.")
  lbl_step.place(x=10, y=10)

  global btn_fury
  btn_fury = Button(tab_misc, text="Buy Fury", command=buy_fury)
  btn_fury.config(width=10)
  btn_fury.place(x=10, y=40)

  global btn_upgrade
  btn_upgrade = Button(tab_misc, text="Buy Upgrade", command=buy_upgrade)
  btn_upgrade.config(width=12)
  btn_upgrade.place(x=100, y=40)

  global btn_force
  btn_force = Button(tab_misc, text="Buy Force", command=buy_force)
  btn_force.config(width=12)
  btn_force.place(x=205, y=40)

  global btn_mails
  btn_mails = Button(tab_misc, text="Get Mails", command=get_mails)
  btn_mails.config(width=10)
  btn_mails.place(x=10, y=75)

  lbl_misc_clicks = Label(tab_misc, text="Clicks: ")
  lbl_misc_clicks.place(x=10, y=115)

  global val_click_count
  val_click_count = ttk.Combobox(tab_misc, values=LIST_CLICKS, state="")
  val_click_count.current(0)
  val_click_count.config(width=5)
  val_click_count.place(x=75, y=115)

  global lbl_misc
  lbl_misc = Label(tab_misc, text="Action: --")
  lbl_misc.place(x=10, y=145)

  frame_root.mainloop()

# GENERATE MAIN
generate_gui()

