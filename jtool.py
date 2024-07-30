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
LIST_RUN_RESTART = [0, 30, 40, 50, 100]
LIST_CLICKS = [10, 20, 30, 40, 50, 100, 200, 500]
LIST_RESOLUTION = ["2560x1440", "1920x1080"]
LIST_LOAD_TIME = ["30 seconds", "45 seconds", "60 seconds", "75 seconds", "90 seconds", "105 seconds", "120 seconds"]

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
val_run_restart = []
val_click_count = []
val_pword = []
val_pin = []

val_mode = 0
val_buffs = 1
val_shorts = 1
val_atk_type = 0
val_vera = 0
val_party = 0
val_leader = 0
val_resolution = 0
val_load_time = 0
val_dungeon_restart = 0

def start():
  cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  choice = list_dg.get()
  mode = val_mode.get()
  buff = val_buffs.get()
  short = val_shorts.get()
  runs = int(val_run_count.get())
  atk_type = val_atk_type.get()
  vera = val_vera.get()
  party = val_party.get()
  leader = val_leader.get()
  run_restart = val_run_restart.get()
  pword = val_pword.get()
  pin = val_pin.get()
  reso = val_resolution.get()
  load_time = int(val_load_time.get().split(' ')[0])
  dungeon_restart = val_dungeon_restart.get()

  util.initialize(cabal_window, frame_root, lbl_macro, lbl_current_run)
  util.initialize_region()
  util.set_variables(mode, buff, short, atk_type, vera, party, leader, runs, run_restart, pword, pin, reso, load_time)

  if dungeon_restart == 1:
    restart_cabal_application()

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

def restart_cabal_application():
  util.log_action(util.MSG_DUNGEON_RESTART)
  util.exit_cabal_application()
  util.select_task_bar()
  util.open_cabal_application()
  util.move_cabal_application()
  util.type_pword()
  util.enter_cabal_world()
  util.move_bead_window()

def buy_fury():
  btn_fury.config(state="disabled")
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(125, 205)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_fury.config(state="active")
  frame_root.update()

def buy_upgrade():
  btn_upgrade.config(state="disabled")
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(15, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_upgrade.config(state="active")
  frame_root.update()

def buy_force():
  btn_force.config(state="disabled")
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(45, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_force.config(state="active")
  frame_root.update()

def get_mails():
  btn_mails.config(state="disabled")
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
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
  tab_premium = ttk.Frame(tab_control)
  tab_misc = ttk.Frame(tab_control)
  tab_control.add(tab_dungeon, text ='Dungeon')
  tab_control.add(tab_premium, text ='Premium')
  tab_control.add(tab_misc, text ='Others')
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

  global lbl_current_run
  lbl_current_run = Label(tab_dungeon, text="Run #: --")
  lbl_current_run.place(x=140, y=105)

  lbl_mode = Label(tab_dungeon, text="Mode II: ")
  lbl_mode.place(x=10, y=75)

  global val_mode
  val_mode = IntVar(value=0)
  chkbtn_mode = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_mode)
  chkbtn_mode.place(x=75, y=76)

  lbl_party = Label(tab_dungeon, text="Party: ", state="disabled")
  lbl_party.place(x=140, y=75)

  global val_party
  val_party = IntVar(value=0)
  chkbtn_party = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_party, state="disabled")
  chkbtn_party.place(x=185, y=76)

  lbl_leader = Label(tab_dungeon, text="Leader: ", state="disabled")
  lbl_leader.place(x=235, y=75)

  global val_leader
  val_leader = IntVar(value=0)
  chkbtn_leader = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_leader, state="disabled")
  chkbtn_leader.place(x=293, y=76)

  lbl_license = Label(tab_dungeon, text="Status: Free")
  lbl_license.place(x=140, y=135)

  lbl_buffs = Label(tab_dungeon, text="Buffs: ")
  lbl_buffs.place(x=10, y=105)

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

  # Tab Premium
  lbl_run_restart = Label(tab_premium, text="Run Restart: ")
  lbl_run_restart.place(x=10, y=10)

  global val_run_restart
  val_run_restart = ttk.Combobox(tab_premium, values=LIST_RUN_RESTART, state="")
  val_run_restart.current(0)
  val_run_restart.config(width=5)
  val_run_restart.place(x=92, y=10)

  lbl_run_restart_note = Label(tab_premium, text="Restart every run specified.")
  lbl_run_restart_note.place(x=155, y=10)

  lbl_dungeon_restart = Label(tab_premium, text="DG Restart: ")
  lbl_dungeon_restart.place(x=10, y=43)

  global val_dungeon_restart
  val_dungeon_restart = IntVar(value=0)
  chkbtn_dungeon_restart = ttk.Checkbutton(tab_premium, text="", onvalue=1, offvalue=0, variable=val_dungeon_restart)
  chkbtn_dungeon_restart.place(x=90, y=43)

  lbl_dungeon_restart_note = Label(tab_premium, text="Restart first before macro.")
  lbl_dungeon_restart_note.place(x=155, y=43)

  lbl_pword = Label(tab_premium, text="Password: ")
  lbl_pword.place(x=10, y=75)

  global val_pword
  val_pword = StringVar()
  entry_pword = Entry(tab_premium, show="*", textvariable=val_pword, width=15)
  entry_pword.place(x=85, y=75)

  lbl_pin = Label(tab_premium, text="PIN: ")
  lbl_pin.place(x=205, y=75)

  global val_pin
  val_pin = StringVar()
  entry_pin = Entry(tab_premium, show="*", textvariable=val_pin, width=10)
  entry_pin.place(x=240, y=75)

  lbl_resolution = Label(tab_premium, text="Resolution: ")
  lbl_resolution.place(x=10, y=105)

  global val_resolution
  val_resolution = ttk.Combobox(tab_premium, values=LIST_RESOLUTION, state="readonly")
  val_resolution.current(0)
  val_resolution.config(width=12)
  val_resolution.place(x=85, y=105)

  lbl_resolution_note = Label(tab_premium, text="Only listed resolution above are supported. ")
  lbl_resolution_note.place(x=10, y=135)

  lbl_load_time = Label(tab_premium, text="Load Time: ")
  lbl_load_time.place(x=10, y=165)

  global val_load_time
  val_load_time = ttk.Combobox(tab_premium, values=LIST_LOAD_TIME, state="readonly")
  val_load_time.current(0)
  val_load_time.config(width=12)
  val_load_time.place(x=85, y=165)

  lbl_load_time_note = Label(tab_premium, text="Adjust based on application load in login. ")
  lbl_load_time_note.place(x=10, y=195)

  # Tab Misc
  lbl_step = Label(tab_misc, text="Open NPC Store before clicking the buy buttons.")
  lbl_step.place(x=10, y=10)

  global btn_fury
  btn_fury = Button(tab_misc, text="Fury", command=buy_fury)
  btn_fury.config(width=8)
  btn_fury.place(x=10, y=40)

  global btn_upgrade
  btn_upgrade = Button(tab_misc, text="Upgrade", command=buy_upgrade)
  btn_upgrade.config(width=8)
  btn_upgrade.place(x=85, y=40)

  global btn_force
  btn_force = Button(tab_misc, text="Force", command=buy_force)
  btn_force.config(width=8)
  btn_force.place(x=160, y=40)

  global btn_mails
  btn_mails = Button(tab_misc, text="Mails", command=get_mails)
  btn_mails.config(width=8)
  btn_mails.place(x=235, y=40)

  lbl_misc_clicks = Label(tab_misc, text="Clicks: ")
  lbl_misc_clicks.place(x=10, y=80)

  global val_click_count
  val_click_count = ttk.Combobox(tab_misc, values=LIST_CLICKS, state="")
  val_click_count.current(0)
  val_click_count.config(width=5)
  val_click_count.place(x=75, y=80)

  global lbl_misc
  lbl_misc = Label(tab_misc, text="Action: --")
  lbl_misc.place(x=160, y=80)

  frame_root.mainloop()

# GENERATE MAIN
generate_gui()
