import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

import common.guard as guard
import common.config as config
import common.util as util

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

LIST_DUNGEON = []

LIST_RUN = [1, 5, 10, 20, 30, 40, 50, 100, 150, 200]
LIST_RUN_RESTART = [0, 30, 40, 50, 75, 100]
LIST_CLICKS = [10, 20, 30, 40, 50, 100, 200, 300, 500]
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

val_config_data = {}
val_node_data = []

def start():
  cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  choice = list_dg.get()
  runs = int(val_run_count.get())
  mode = val_mode.get()
  buff = val_buffs.get()
  short = val_shorts.get()
  atk_type = val_atk_type.get()
  vera = val_vera.get()
  run_restart = val_run_restart.get()
  pword = val_pword.get()
  pin = val_pin.get()
  reso = val_resolution.get()
  load_time = int(val_load_time.get().split(' ')[0])
  dungeon_restart = val_dungeon_restart.get()

  save_data()
  util.initialize(cabal_window, frame_root, lbl_macro, lbl_current_run)
  util.initialize_region()
  util.set_variables(mode, buff, short, atk_type, vera, runs, run_restart, pword, pin, reso, load_time)

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

def get_dungeon_list():
  global LIST_DUNGEON
  if get_level() == 'FREE':
    LIST_DUNGEON = [
      "Hazardous Valley (Awakened)",
      "Hazardous Valley (Hard)",
      "Hazardous Valley (Medium)",
      "Hazardous Valley (Easy)"
    ]
  elif get_level() == 'PRO':
    LIST_DUNGEON = [
      "Hazardous Valley (Awakened)",
      "Hazardous Valley (Hard)",
      "Hazardous Valley (Medium)",
      "Hazardous Valley (Easy)",
      "Steamer Crazy (Awakened)",
      "Catacomb Frost (Awakened)",
      "Lava Hellfire (Awakened)"
    ]
  elif get_level() == 'PREMIUM':
    LIST_DUNGEON = [
      "Hazardous Valley (Awakened)",
      "Hazardous Valley (Hard)",
      "Hazardous Valley (Medium)",
      "Hazardous Valley (Easy)",
      "Steamer Crazy (Awakened)",
      "Catacomb Frost (Awakened)",
      "Lava Hellfire (Awakened)",
      "Holy Windmill",
      "Holy Keldrasil",
    ]
  elif get_level() == 'SUPER':
    LIST_DUNGEON = [
      "Hazardous Valley (Awakened)",
      "Hazardous Valley (Hard)",
      "Hazardous Valley (Medium)",
      "Hazardous Valley (Easy)",
      "Steamer Crazy (Awakened)",
      "Catacomb Frost (Awakened)",
      "Lava Hellfire (Awakened)",
      "Panic Cave (Awakened)",
      "Holy Windmill",
      "Holy Keldrasil",
      "Terminus Machina",
      "Altar of Siena B1F (Prideus)"
    ]

def get_access(feature):
  match feature:
    case util.DATA_DUNGEON:
      return util.STATE_NORMAL
    case util.DATA_CONNECTION:
      if get_level() == util.ACCESS_FREE or get_level() == util.ACCESS_PRO:
        return util.STATE_DISABLED
      else:
        return util.STATE_NORMAL
    case util.DATA_OTHERS:
      if get_level() == util.ACCESS_FREE:
        return util.STATE_DISABLED
      else:
        return util.STATE_NORMAL
    case util.DATA_MODE:
      if get_level() == util.ACCESS_FREE:
        return util.STATE_DISABLED
      else:
        return util.STATE_NORMAL
    case util.DATA_BUFFS:
      return util.STATE_NORMAL
    case util.DATA_SHORTS:
      if get_level() == util.ACCESS_FREE:
        return util.STATE_DISABLED
      else:
        return util.STATE_NORMAL
    case util.DATA_RANGE:
      return util.STATE_NORMAL
    case util.DATA_VERADRIX:
      if get_level() == util.ACCESS_FREE or get_level() == util.ACCESS_PRO:
        return util.STATE_DISABLED
      else:
        return util.STATE_NORMAL

def load_node():
  global val_node_data
  val_node_data = guard.get_user_value()

def get_level():
  return val_node_data[0]

def get_level_status():
  return util.LBL_STATUS + str(get_level())

def get_expiration():
  return val_node_data[1]

def get_expiration_status():
  if val_node_data[1] == None:
    return util.LBL_EXPIRATION_NA
  else:
    return util.LBL_EXPIRATION + str(get_expiration().strftime("%B %d, %Y"))

def load_data():
  global val_config_data
  val_config_data = config.load_data()

def get_data(name):
  match name:
    case util.DATA_DUNGEON:
      if val_config_data[name] > len(LIST_DUNGEON) - 1:
        return util.STATE_ZERO
    case util.DATA_MODE:
      if get_level() == util.ACCESS_FREE:
        return util.STATE_ZERO
    case util.DATA_SHORTS:
      if get_level() == util.ACCESS_FREE:
        return util.STATE_ZERO
    case util.DATA_VERADRIX:
      if get_level() == util.ACCESS_FREE or get_level() == util.ACCESS_PRO:
        return util.STATE_ZERO

  return val_config_data[name]

def save_data():
  val_config_data[util.DATA_DUNGEON] = LIST_DUNGEON.index(list_dg.get())
  val_config_data[util.DATA_MODE] = val_mode.get()
  val_config_data[util.DATA_BUFFS] = val_buffs.get()
  val_config_data[util.DATA_SHORTS] = val_shorts.get()
  val_config_data[util.DATA_RANGE] = val_atk_type.get()
  val_config_data[util.DATA_VERADRIX] = val_vera.get()
  val_config_data[util.DATA_PWORD] = val_pword.get()
  val_config_data[util.DATA_PIN] = val_pin.get()
  val_config_data[util.DATA_RESOLUTION] = LIST_RESOLUTION.index(val_resolution.get())
  val_config_data[util.DATA_LOAD] = LIST_LOAD_TIME.index(val_load_time.get())
  config.save_data(val_config_data)

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
  btn_fury.config(state=util.STATE_DISABLED)
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(125, 205)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_fury.config(state=util.STATE_NORMAL)
  frame_root.update()

def buy_upgrade():
  btn_upgrade.config(state=util.STATE_DISABLED)
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(15, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_upgrade.config(state=util.STATE_NORMAL)
  frame_root.update()

def buy_force():
  btn_force.config(state=util.STATE_DISABLED)
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(45, 180)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_force.config(state=util.STATE_NORMAL)
  frame_root.update()

def get_mails():
  btn_mails.config(state=util.STATE_DISABLED)
  frame_root.update()
  window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
  util.set_cabal_window(window)
  util.go_cabal_window()

  for x in range(int(val_click_count.get())):
    util.move_click(510, 310, 0.5)
    util.move_click(510, 525, 0.5)
    log_misc_action(util.MSG_CLICK + str(x+1))

  btn_mails.config(state=util.STATE_NORMAL)
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
  tab_connection = ttk.Frame(tab_control)
  tab_misc = ttk.Frame(tab_control)
  tab_control.add(tab_dungeon, text=util.TAB_DUNGEON, state=get_access(util.DATA_DUNGEON))
  tab_control.add(tab_connection, text=util.TAB_CONNECTION, state=get_access(util.DATA_CONNECTION))
  tab_control.add(tab_misc, text=util.TAB_OTHERS, state=get_access(util.DATA_OTHERS))
  tab_control.pack(expand=1, fill="both")

  # Tab Dungeon
  lbl_dungeon_list = Label(tab_dungeon, text=util.LBL_DUNGEON)
  lbl_dungeon_list.place(x=10, y=10)

  global list_dg
  list_dg = ttk.Combobox(tab_dungeon, values=LIST_DUNGEON, state=util.STATE_READONLY)
  list_dg.current(get_data(util.DATA_DUNGEON))
  list_dg.config(width=30)
  list_dg.place(x=75, y=10)

  lbl_runs = Label(tab_dungeon, text="Runs: ")
  lbl_runs.place(x=10, y=43)

  global val_run_count
  val_run_count = ttk.Combobox(tab_dungeon, values=LIST_RUN, state=util.STATE_NORMAL)
  val_run_count.current(0)
  val_run_count.config(width=5)
  val_run_count.place(x=75, y=43)

  global btn_start
  btn_start = Button(tab_dungeon, text=util.BTN_START, command=start)
  btn_start.config(width=10)
  btn_start.place(x=230, y=40)

  global lbl_current_run
  lbl_current_run = Label(tab_dungeon, text=util.LBL_CURRENT_RUN)
  lbl_current_run.place(x=140, y=105)

  lbl_mode = Label(tab_dungeon, text=util.LBL_MODE, state=get_access(util.DATA_MODE))
  lbl_mode.place(x=10, y=75)

  global val_mode
  val_mode = IntVar(value=get_data(util.DATA_MODE))
  chkbtn_mode = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_mode, state=get_access(util.DATA_MODE))
  chkbtn_mode.place(x=75, y=76)

  lbl_license = Label(tab_dungeon, text=get_level_status())
  lbl_license.place(x=140, y=135)

  lbl_buffs = Label(tab_dungeon, text=util.LBL_BUFFS, state=get_access(util.DATA_BUFFS))
  lbl_buffs.place(x=10, y=105)

  global val_buffs
  val_buffs = IntVar(value=get_data(util.DATA_BUFFS))
  chkbtn_buffs = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_buffs, state=get_access(util.DATA_BUFFS))
  chkbtn_buffs.place(x=75, y=106)

  lbl_expiration = Label(tab_dungeon, text=get_expiration_status())
  lbl_expiration.place(x=140, y=165)

  lbl_shorts = Label(tab_dungeon, text=util.LBL_SHORTS, state=get_access(util.DATA_SHORTS))
  lbl_shorts.place(x=10, y=135)

  global val_shorts
  val_shorts = IntVar(value=get_data(util.DATA_SHORTS))
  chkbtn_shorts = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_shorts, state=get_access(util.DATA_SHORTS))
  chkbtn_shorts.place(x=75, y=136)

  global lbl_macro
  lbl_macro = Label(tab_dungeon, text=util.LBL_ACTION)
  lbl_macro.place(x=140, y=195)

  lbl_atk_type = Label(tab_dungeon, text=util.LBL_RANGE)
  lbl_atk_type.place(x=10, y=165)

  global val_atk_type
  val_atk_type = IntVar(value=get_data(util.DATA_RANGE))
  chkbtn_atk_type = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0,
    variable=val_atk_type)
  chkbtn_atk_type.place(x=75, y=166)

  lbl_vera = Label(tab_dungeon, text=util.LBL_VERADRIX, state=get_access(util.DATA_VERADRIX))
  lbl_vera.place(x=10, y=195)

  global val_vera
  val_vera = IntVar(value=get_data(util.DATA_VERADRIX))
  chkbtn_vera = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_vera, state=get_access(util.DATA_VERADRIX))
  chkbtn_vera.place(x=75, y=196)

  # Tab Premium
  lbl_run_restart = Label(tab_connection, text=util.LBL_RUN_RESTART)
  lbl_run_restart.place(x=10, y=10)

  global val_run_restart
  val_run_restart = ttk.Combobox(tab_connection, values=LIST_RUN_RESTART)
  val_run_restart.current(0)
  val_run_restart.config(width=5)
  val_run_restart.place(x=92, y=10)

  lbl_run_restart_note = Label(tab_connection, text=util.LBL_RUN_RESTART_NOTE)
  lbl_run_restart_note.place(x=155, y=10)

  lbl_dungeon_restart = Label(tab_connection, text=util.LBL_DG_RESTART)
  lbl_dungeon_restart.place(x=10, y=43)

  global val_dungeon_restart
  val_dungeon_restart = IntVar(value=0)
  chkbtn_dungeon_restart = ttk.Checkbutton(tab_connection, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_dungeon_restart)
  chkbtn_dungeon_restart.place(x=90, y=43)

  lbl_dungeon_restart_note = Label(tab_connection, text=util.LBL_DG_RESTART_NOTE)
  lbl_dungeon_restart_note.place(x=155, y=43)

  lbl_pword = Label(tab_connection, text=util.LBL_PWORD)
  lbl_pword.place(x=10, y=75)

  global val_pword
  val_pword = StringVar()
  val_pword.set(get_data(util.DATA_PWORD))
  entry_pword = Entry(tab_connection, show="*", textvariable=val_pword, width=15)
  entry_pword.place(x=85, y=75)

  lbl_pin = Label(tab_connection, text=util.LBL_PIN)
  lbl_pin.place(x=205, y=75)

  global val_pin
  val_pin = StringVar()
  val_pin.set(get_data(util.DATA_PIN))
  entry_pin = Entry(tab_connection, show="*", textvariable=val_pin, width=10)
  entry_pin.place(x=240, y=75)

  lbl_resolution = Label(tab_connection, text=util.LBL_RESOLUTION)
  lbl_resolution.place(x=10, y=105)

  global val_resolution
  val_resolution = ttk.Combobox(tab_connection, values=LIST_RESOLUTION, state=util.STATE_READONLY)
  val_resolution.current(get_data(util.DATA_RESOLUTION))
  val_resolution.config(width=12)
  val_resolution.place(x=85, y=105)

  lbl_resolution_note = Label(tab_connection, text=util.LBL_RESOLUTION_NOTE)
  lbl_resolution_note.place(x=10, y=135)

  lbl_load_time = Label(tab_connection, text=util.LBL_LOAD_TIME)
  lbl_load_time.place(x=10, y=165)

  global val_load_time
  val_load_time = ttk.Combobox(tab_connection, values=LIST_LOAD_TIME, state=util.STATE_READONLY)
  val_load_time.current(get_data(util.DATA_LOAD))
  val_load_time.config(width=12)
  val_load_time.place(x=85, y=165)

  lbl_load_time_note = Label(tab_connection, text=util.LBL_LOAD_TIME_NOTE)
  lbl_load_time_note.place(x=10, y=195)

  # Tab Misc
  lbl_store_note = Label(tab_misc, text=util.LBL_STORE_NOTE)
  lbl_store_note.place(x=10, y=10)

  global btn_fury
  btn_fury = Button(tab_misc, text=util.BTN_FURY, command=buy_fury)
  btn_fury.config(width=8)
  btn_fury.place(x=10, y=40)

  global btn_upgrade
  btn_upgrade = Button(tab_misc, text=util.BTN_UPGRADE, command=buy_upgrade)
  btn_upgrade.config(width=8)
  btn_upgrade.place(x=85, y=40)

  global btn_force
  btn_force = Button(tab_misc, text=util.BTN_FORCE, command=buy_force)
  btn_force.config(width=8)
  btn_force.place(x=160, y=40)

  global btn_mails
  btn_mails = Button(tab_misc, text=util.BTN_MAILS, command=get_mails)
  btn_mails.config(width=8)
  btn_mails.place(x=235, y=40)

  lbl_misc_clicks = Label(tab_misc, text=util.LBL_CLICKS)
  lbl_misc_clicks.place(x=10, y=80)

  global val_click_count
  val_click_count = ttk.Combobox(tab_misc, values=LIST_CLICKS, state=util.STATE_NORMAL)
  val_click_count.current(0)
  val_click_count.config(width=5)
  val_click_count.place(x=75, y=80)

  global lbl_misc
  lbl_misc = Label(tab_misc, text=util.LBL_ACTION)
  lbl_misc.place(x=160, y=80)

  frame_root.mainloop()

# GENERATE MAIN
load_node()
get_dungeon_list()
load_data()
generate_gui()
