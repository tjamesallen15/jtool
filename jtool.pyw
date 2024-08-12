from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

import common.guard as guard
import common.config as config
import common.features as features
import common.leash as leash
import common.util as util

from macro.hva import HazardousValleyAwakened
from macro.hvenh import HazardousValley
from macro.sca import SteamerCrazyAwakened
from macro.hw import HolyWindmill
from macro.cfa import CatacombsFrostAwakened
from macro.lha import LavaHellfireAwakened
from macro.tm import TerminusMachina
from macro.pca import PanicCaveAwakened
from macro.hk import HolyKeldrasil
from macro.s1p import SienaB1FPrideus
from macro.ci import ChaosInfinity
from macro.hvv import HazardousValleyVeradrix

pynboard = Controller()
class JTool():

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
    "Altar of Siena B1F (Prideus)",
    "Chaos Infinity",
    "Hazardous Valley (Veradrix)"
  ]

  LIST_DUNGEON = []

  LIST_RUN = [1, 5, 10, 20, 30, 40, 50, 100, 150, 200]
  LIST_RUN_RESTART = [0, 10, 20, 30, 40, 50, 75, 100]
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
  btn_test = []
  btn_train = []
  lbl_macro = []
  lbl_misc = []
  lbl_current_run = []
  lbl_run_time = []
  lbl_restart_note = []
  lbl_pet_action = []
  text_features = []
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
  val_archer = 0
  val_resolution = 0
  val_load_time = 0
  val_dungeon_restart = 0

  val_def_x = "230"
  val_def_y = "250"
  val_mcr = 0
  val_crt = 0
  val_cdi = 0
  val_crr = 0

  val_x_coords = []
  val_y_coords = []

  val_config_data = {}
  val_node_data = []

  def initialize(self):
    self.load_node()
    self.get_dungeon_list()
    self.load_data()
    self.generate_matrix()
    self.generate_gui()

  def start(self):
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

    if int(run_restart) > 0:
      val_restart_note = util.LBL_RUN_RESTART + util.LBL_RESTART_NOTE_PREFIX + str(run_restart) + util.LBL_RESTART_NOTE_SUFFIX
      lbl_restart_note.config(text=val_restart_note)
    else:
      val_restart_note = util.LBL_RUN_RESTART + util.STATE_NA
      lbl_restart_note.config(text=val_restart_note)

    self.save_data()
    util.initialize(cabal_window, frame_root, lbl_macro, lbl_current_run, lbl_run_time)
    util.initialize_region()
    util.set_variables(mode, buff, short, atk_type, vera, runs, run_restart, pword, pin, reso, load_time)

    if dungeon_restart == 1:
      self.restart_cabal_application()

    if choice == self.LIST_MASTER[0]:
      HazardousValleyAwakened().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[1] or choice == self.LIST_MASTER[2] or choice == self.LIST_MASTER[3]:
      HazardousValley().initialize(frame_root, btn_start, runs, choice)
    elif choice == self.LIST_MASTER[4]:
      SteamerCrazyAwakened().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[5]:
      CatacombsFrostAwakened().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[6]:
      LavaHellfireAwakened().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[7]:
      HolyWindmill().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[8]:
      TerminusMachina().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[9]:
      PanicCaveAwakened().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[10]:
      HolyKeldrasil().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[11]:
      SienaB1FPrideus().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[12]:
      ChaosInfinity().initialize(frame_root, btn_start, runs)
    elif choice == self.LIST_MASTER[13]:
      HazardousValleyVeradrix().initialize(frame_root, btn_start, runs)

  def get_dungeon_list(self):
    global LIST_DUNGEON
    if self.get_level() == util.ACCESS_FREE:
      LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)"
      ]
    elif self.get_level() == util.ACCESS_PRO:
      LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)",
        "Steamer Crazy (Awakened)",
        "Catacomb Frost (Awakened)",
        "Lava Hellfire (Awakened)"
      ]
    elif self.get_level() == util.ACCESS_PREMIUM:
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
    elif self.get_level() == util.ACCESS_TESTER:
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
        "Terminus Machina",
      ]
    elif self.get_level() == util.ACCESS_SUPER:
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
        "Chaos Infinity",
        "Altar of Siena B1F (Prideus)",
        "Hazardous Valley (Veradrix)"
      ]

  def get_access(self, feature):
    match feature:
      case util.DATA_DUNGEON:
        return util.STATE_NORMAL
      case util.DATA_CONNECTION:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_TESTER:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_PET:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_PREMIUM or self.get_level() == util.ACCESS_TESTER:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_OTHERS:
        if self.get_level() == util.ACCESS_FREE:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_MODE:
        if self.get_level() == util.ACCESS_FREE:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_BUFFS:
        return util.STATE_NORMAL
      case util.DATA_SHORTS:
        if self.get_level() == util.ACCESS_FREE:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_RANGE:
        return util.STATE_NORMAL
      case util.DATA_VERADRIX:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL

  def load_node(self):
    global val_node_data
    val_node_data = guard.get_user_value()

  def get_level(self):
    return val_node_data[0]

  def get_account(self):
    val_account = str(self.get_level())
    if val_node_data[2] != None:
      val_account += util.LBL_OPEN_SECTION
      val_account += val_node_data[2]
      val_account += util.LBL_CLOSE_SECTION

    return val_account

  def get_license(self):
    return util.LBL_LICENSE + str(self.get_account())

  def get_expiration(self):
    return val_node_data[1]

  def get_expiration_status(self):
    if val_node_data[1] == None:
      return util.LBL_EXPIRATION_NA
    else:
      return util.LBL_EXPIRATION + str(self.get_expiration().strftime("%B %d, %Y"))

  def load_data(self):
    global val_config_data
    val_config_data = config.load_data()

  def get_data(self, name):
    match name:
      case util.DATA_DUNGEON:
        if val_config_data[name] > len(LIST_DUNGEON) - 1:
          return util.STATE_ZERO
      case util.DATA_MODE:
        if self.get_level() == util.ACCESS_FREE:
          return util.STATE_ZERO
      case util.DATA_SHORTS:
        if self.get_level() == util.ACCESS_FREE:
          return util.STATE_ZERO
      case util.DATA_VERADRIX:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO:
          return util.STATE_ZERO

    return val_config_data[name]

  def save_data(self):
    val_config_data[util.DATA_DUNGEON] = LIST_DUNGEON.index(list_dg.get())
    val_config_data[util.DATA_MODE] = val_mode.get()
    val_config_data[util.DATA_BUFFS] = val_buffs.get()
    val_config_data[util.DATA_SHORTS] = val_shorts.get()
    val_config_data[util.DATA_RANGE] = val_atk_type.get()
    val_config_data[util.DATA_VERADRIX] = val_vera.get()
    val_config_data[util.DATA_PWORD] = val_pword.get()
    val_config_data[util.DATA_PIN] = val_pin.get()
    val_config_data[util.DATA_RESOLUTION] = self.LIST_RESOLUTION.index(val_resolution.get())
    val_config_data[util.DATA_LOAD] = self.LIST_LOAD_TIME.index(val_load_time.get())
    config.save_data(val_config_data)

  def restart_cabal_application(self):
    util.log_action(util.MSG_DUNGEON_RESTART)
    util.exit_cabal_application()
    util.select_task_bar()
    util.open_cabal_application()
    util.move_cabal_application()
    util.type_pword()
    util.enter_cabal_world()
    util.move_bead_window()

  def generate_matrix(self):
    leash.generate_matrix()

  def pet_test(self):
    btn_train.config(state=util.STATE_DISABLED)
    btn_test.config(state=util.STATE_DISABLED)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(val_x_coords.get())
    coor_y = int(val_y_coords.get())
    leash.click_test_npc(coor_x, coor_y)

    btn_train.config(state=util.STATE_NORMAL)
    btn_test.config(state=util.STATE_NORMAL)
    frame_root.update()

  def pet_train(self):
    btn_train.config(state=util.STATE_DISABLED)
    btn_test.config(state=util.STATE_DISABLED)
    lbl_pet_action.config(text=util.LBL_STATUS_TRAINING)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(val_x_coords.get())
    coor_y = int(val_y_coords.get())
    mcr = val_mcr.get()
    crt = val_crt.get()
    cdi = val_cdi.get()
    crr = val_crr.get()
    leash.pet_train(coor_x, coor_y, mcr, crt, cdi, crr)

    btn_train.config(state=util.STATE_NORMAL)
    btn_test.config(state=util.STATE_NORMAL)
    lbl_pet_action.config(text=util.LBL_STATUS_IDLE)
    frame_root.update()

  def buy_fury(self):
    btn_fury.config(state=util.STATE_DISABLED)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(val_click_count.get())):
      util.move_click(125, 205)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    btn_fury.config(state=util.STATE_NORMAL)
    frame_root.update()

  def buy_upgrade(self):
    btn_upgrade.config(state=util.STATE_DISABLED)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(val_click_count.get())):
      util.move_click(15, 180)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    btn_upgrade.config(state=util.STATE_NORMAL)
    frame_root.update()

  def buy_force(self):
    btn_force.config(state=util.STATE_DISABLED)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(val_click_count.get())):
      util.move_click(45, 180)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    btn_force.config(state=util.STATE_NORMAL)
    frame_root.update()

  def get_mails(self):
    btn_mails.config(state=util.STATE_DISABLED)
    frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(val_click_count.get())):
      util.move_click(510, 310, 0.5)
      util.move_click(510, 525, 0.5)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    btn_mails.config(state=util.STATE_NORMAL)
    frame_root.update()

  def get_features_free(self):
    text_features.configure(state=util.STATE_NORMAL)
    text_features.delete('1.0', END)
    text_features.insert(END, features.get_features(util.ACCESS_FREE))
    text_features.configure(state=util.STATE_DISABLED)

  def get_features_pro(self):
    text_features.configure(state=util.STATE_NORMAL)
    text_features.delete('1.0', END)
    text_features.insert(END, features.get_features(util.ACCESS_PRO))
    text_features.configure(state=util.STATE_DISABLED)

  def get_features_premium(self):
    text_features.configure(state=util.STATE_NORMAL)
    text_features.delete('1.0', END)
    text_features.insert(END, features.get_features(util.ACCESS_PREMIUM))
    text_features.configure(state=util.STATE_DISABLED)

  def log_misc_action(self, message):
    msgBuilder = StringVar()
    msgBuilder = util.MSG_ACTION + message
    print(msgBuilder)
    lbl_misc.config(text=msgBuilder)
    frame_root.update()

  def generate_gui(self):
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
    tab_pet = ttk.Frame(tab_control)
    tab_misc = ttk.Frame(tab_control)
    tab_pricing = ttk.Frame(tab_control)
    tab_control.add(tab_dungeon, text=util.TAB_DUNGEON, state=self.get_access(util.DATA_DUNGEON))
    tab_control.add(tab_connection, text=util.TAB_CONNECTION, state=self.get_access(util.DATA_CONNECTION))
    tab_control.add(tab_pet, text=util.TAB_PET, state=self.get_access(util.DATA_CONNECTION))
    tab_control.add(tab_misc, text=util.TAB_OTHERS, state=self.get_access(util.DATA_OTHERS))
    tab_control.add(tab_pricing, text=util.TAB_PRICING)
    tab_control.pack(expand=1, fill="both")

    # Tab Dungeon
    lbl_dungeon_list = Label(tab_dungeon, text=util.LBL_DUNGEON)
    lbl_dungeon_list.place(x=10, y=10)

    global list_dg
    list_dg = ttk.Combobox(tab_dungeon, values=LIST_DUNGEON, state=util.STATE_READONLY)
    list_dg.current(self.get_data(util.DATA_DUNGEON))
    list_dg.config(width=30)
    list_dg.place(x=75, y=10)

    lbl_runs = Label(tab_dungeon, text=util.LBL_RUNS)
    lbl_runs.place(x=10, y=43)

    global val_run_count
    val_run_count = ttk.Combobox(tab_dungeon, values=self.LIST_RUN, state=util.STATE_NORMAL)
    val_run_count.current(0)
    val_run_count.config(width=5)
    val_run_count.place(x=75, y=43)

    global btn_start
    btn_start = Button(tab_dungeon, text=util.BTN_START, command=self.start)
    btn_start.config(width=10)
    btn_start.place(x=230, y=40)

    global lbl_current_run
    lbl_current_run = Label(tab_dungeon, text=util.LBL_CURRENT_RUN)
    lbl_current_run.place(x=140, y=75)

    lbl_mode = Label(tab_dungeon, text=util.LBL_MODE, state=self.get_access(util.DATA_MODE))
    lbl_mode.place(x=10, y=75)

    global lbl_run_time
    lbl_run_time = Label(tab_dungeon, text=util.LBL_RUN_TIME)
    lbl_run_time.place(x=140, y=105)

    global val_mode
    val_mode = IntVar(value=self.get_data(util.DATA_MODE))
    chkbtn_mode = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_mode, state=self.get_access(util.DATA_MODE))
    chkbtn_mode.place(x=75, y=76)

    global lbl_restart_note
    lbl_restart_note = Label(tab_dungeon, text=util.LBL_RUN_RESTART)
    lbl_restart_note.place(x=140, y=135)

    lbl_license = Label(tab_dungeon, text=self.get_license())
    lbl_license.place(x=140, y=165)

    lbl_buffs = Label(tab_dungeon, text=util.LBL_BUFFS, state=self.get_access(util.DATA_BUFFS))
    lbl_buffs.place(x=10, y=105)

    global val_buffs
    val_buffs = IntVar(value=self.get_data(util.DATA_BUFFS))
    chkbtn_buffs = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_buffs, state=self.get_access(util.DATA_BUFFS))
    chkbtn_buffs.place(x=75, y=106)

    lbl_expiration = Label(tab_dungeon, text=self.get_expiration_status())
    lbl_expiration.place(x=140, y=195)

    lbl_shorts = Label(tab_dungeon, text=util.LBL_SHORTS, state=self.get_access(util.DATA_SHORTS))
    lbl_shorts.place(x=10, y=135)

    global val_shorts
    val_shorts = IntVar(value=self.get_data(util.DATA_SHORTS))
    chkbtn_shorts = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_shorts, state=self.get_access(util.DATA_SHORTS))
    chkbtn_shorts.place(x=75, y=136)

    global lbl_macro
    lbl_macro = Label(tab_dungeon, text=util.LBL_MACRO)
    lbl_macro.place(x=140, y=225)

    lbl_atk_type = Label(tab_dungeon, text=util.LBL_RANGE)
    lbl_atk_type.place(x=10, y=165)

    global val_atk_type
    val_atk_type = IntVar(value=self.get_data(util.DATA_RANGE))
    chkbtn_atk_type = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0,
      variable=val_atk_type)
    chkbtn_atk_type.place(x=75, y=166)

    lbl_archer = Label(tab_dungeon, text=util.LBL_ARCHER, state=self.get_access(util.DATA_VERADRIX))
    lbl_archer.place(x=10, y=195)

    global val_archer
    val_archer = IntVar(value=0)
    chkbtn_archer = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_archer, state=self.get_access(util.DATA_VERADRIX))
    chkbtn_archer.place(x=75, y=196)

    lbl_vera = Label(tab_dungeon, text=util.LBL_VERADRIX, state=self.get_access(util.DATA_VERADRIX))
    lbl_vera.place(x=10, y=225)

    global val_vera
    val_vera = IntVar(value=self.get_data(util.DATA_VERADRIX))
    chkbtn_vera = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_vera, state=self.get_access(util.DATA_VERADRIX))
    chkbtn_vera.place(x=75, y=226)

    # Tab Connection
    lbl_run_restart = Label(tab_connection, text=util.LBL_RUN_RESTART)
    lbl_run_restart.place(x=10, y=10)

    global val_run_restart
    val_run_restart = ttk.Combobox(tab_connection, values=self.LIST_RUN_RESTART)
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
    val_pword.set(self.get_data(util.DATA_PWORD))
    entry_pword = Entry(tab_connection, show="*", textvariable=val_pword, width=15)
    entry_pword.place(x=85, y=75)

    lbl_pin = Label(tab_connection, text=util.LBL_PIN)
    lbl_pin.place(x=205, y=75)

    global val_pin
    val_pin = StringVar()
    val_pin.set(self.get_data(util.DATA_PIN))
    entry_pin = Entry(tab_connection, show="*", textvariable=val_pin, width=10)
    entry_pin.place(x=240, y=75)

    lbl_resolution = Label(tab_connection, text=util.LBL_RESOLUTION)
    lbl_resolution.place(x=10, y=105)

    global val_resolution
    val_resolution = ttk.Combobox(tab_connection, values=self.LIST_RESOLUTION, state=util.STATE_READONLY)
    val_resolution.current(self.get_data(util.DATA_RESOLUTION))
    val_resolution.config(width=12)
    val_resolution.place(x=85, y=105)

    lbl_resolution_note = Label(tab_connection, text=util.LBL_RESOLUTION_NOTE)
    lbl_resolution_note.place(x=10, y=135)

    lbl_load_time = Label(tab_connection, text=util.LBL_LOAD_TIME)
    lbl_load_time.place(x=10, y=165)

    global val_load_time
    val_load_time = ttk.Combobox(tab_connection, values=self.LIST_LOAD_TIME, state=util.STATE_READONLY)
    val_load_time.current(self.get_data(util.DATA_LOAD))
    val_load_time.config(width=12)
    val_load_time.place(x=85, y=165)

    lbl_load_time_note = Label(tab_connection, text=util.LBL_LOAD_TIME_NOTE)
    lbl_load_time_note.place(x=10, y=195)

    lbl_cabal_note = Label(tab_connection, text=util.LBL_CABAL_NOTE)
    lbl_cabal_note.place(x=10, y=225)

    # Tab Pet
    lbl_pet_note_1 = Label(tab_pet, text=util.LBL_PET_NOTE_1)
    lbl_pet_note_1.place(x=10, y=10)

    lbl_pet_note_2 = Label(tab_pet, text=util.LBL_PET_NOTE_2)
    lbl_pet_note_2.place(x=10, y=40)

    lbl_pet_note_3 = Label(tab_pet, text=util.LBL_PET_NOTE_3)
    lbl_pet_note_3.place(x=10, y=70)

    lbl_x_coords = Label(tab_pet, text=util.LBL_NPC_X)
    lbl_x_coords.place(x=10, y=103)

    global val_x_coords
    val_x_coords = StringVar()
    val_x_coords.set(self.val_def_x)
    entry_x_coords = Entry(tab_pet, textvariable=val_x_coords, width=5)
    entry_x_coords.place(x=62, y=105)

    lbl_y_coords = Label(tab_pet, text=util.LBL_NPC_Y)
    lbl_y_coords.place(x=110, y=103)

    global val_y_coords
    val_y_coords = StringVar()
    val_y_coords.set(self.val_def_y)
    entry_y_coords = Entry(tab_pet, textvariable=val_y_coords, width=5)
    entry_y_coords.place(x=162, y=105)

    global btn_test
    btn_test = Button(tab_pet, text=util.BTN_TEST, command=self.pet_test)
    btn_test.config(width=5)
    btn_test.place(x=210, y=100)

    global btn_train
    btn_train = Button(tab_pet, text=util.BTN_TRAIN, command=self.pet_train)
    btn_train.config(width=6)
    btn_train.place(x=260, y=100)

    lbl_pet_note_4 = Label(tab_pet, text=util.LBL_PET_NOTE_4)
    lbl_pet_note_4.place(x=10, y=135)

    lbl_mcr = Label(tab_pet, text=util.LBL_MCR)
    lbl_mcr.place(x=10, y=165)

    global val_mcr
    val_mcr = IntVar(value=1)
    chkbtn_mcr = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_mcr, state=util.NORMAL)
    chkbtn_mcr.place(x=50, y=167)

    lbl_crt = Label(tab_pet, text=util.LBL_CRT)
    lbl_crt.place(x=80, y=165)

    global val_crt
    val_crt = IntVar(value=0)
    chkbtn_crt = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_crt, state=util.NORMAL)
    chkbtn_crt.place(x=120, y=167)

    lbl_cdi = Label(tab_pet, text=util.LBL_CDI)
    lbl_cdi.place(x=150, y=165)

    global val_cdi
    val_cdi = IntVar(value=0)
    chkbtn_cdi = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_cdi, state=util.NORMAL)
    chkbtn_cdi.place(x=190, y=167)

    lbl_crr = Label(tab_pet, text=util.LBL_CRR)
    lbl_crr.place(x=220, y=165)

    global val_crr
    val_crr = IntVar(value=0)
    chkbtn_crr = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=val_crr, state=util.NORMAL)
    chkbtn_crr.place(x=260, y=167)

    lbl_pet_note_5 = Label(tab_pet, text=util.LBL_PET_NOTE_5)
    lbl_pet_note_5.place(x=10, y=195)

    global lbl_pet_action
    lbl_pet_action = Label(tab_pet, text=util.LBL_STATUS_IDLE)
    lbl_pet_action.place(x=10, y=225)

    # Tab Misc
    lbl_store_note = Label(tab_misc, text=util.LBL_STORE_NOTE)
    lbl_store_note.place(x=10, y=10)

    global btn_fury
    btn_fury = Button(tab_misc, text=util.BTN_FURY, command=self.buy_fury)
    btn_fury.config(width=8)
    btn_fury.place(x=10, y=40)

    global btn_upgrade
    btn_upgrade = Button(tab_misc, text=util.BTN_UPGRADE, command=self.buy_upgrade)
    btn_upgrade.config(width=8)
    btn_upgrade.place(x=85, y=40)

    global btn_force
    btn_force = Button(tab_misc, text=util.BTN_FORCE, command=self.buy_force)
    btn_force.config(width=8)
    btn_force.place(x=160, y=40)

    lbl_mail_note = Label(tab_misc, text=util.LBL_MAIL_NOTE)
    lbl_mail_note.place(x=10, y=80)

    global btn_mails
    btn_mails = Button(tab_misc, text=util.BTN_MAILS, command=self.get_mails)
    btn_mails.config(width=8)
    btn_mails.place(x=10, y=110)

    lbl_misc_clicks = Label(tab_misc, text=util.LBL_CLICKS)
    lbl_misc_clicks.place(x=10, y=150)

    global val_click_count
    val_click_count = ttk.Combobox(tab_misc, values=self.LIST_CLICKS, state=util.STATE_NORMAL)
    val_click_count.current(0)
    val_click_count.config(width=5)
    val_click_count.place(x=75, y=150)

    global lbl_misc
    lbl_misc = Label(tab_misc, text=util.LBL_CLICK)
    lbl_misc.place(x=160, y=150)

    # Tab Pricing
    frame_btn = Frame(tab_pricing)
    frame_btn.pack(anchor="w")

    scroll_features = Scrollbar(tab_pricing)
    scroll_features.pack(side=RIGHT, fill=Y)

    global text_features
    text_features = Text(tab_pricing, yscrollcommand=scroll_features.set)
    text_features.pack()
    self.get_features_free()

    btn_free = Button(frame_btn, text=util.BTN_FREE, command=self.get_features_free)
    btn_free.pack(side=LEFT)

    btn_pro = Button(frame_btn, text=util.BTN_PRO, command=self.get_features_pro)
    btn_pro.pack(side=LEFT)

    btn_premium = Button(frame_btn, text=util.BTN_PREMIUM, command=self.get_features_premium)
    btn_premium.pack(side=LEFT)

    frame_root.mainloop()

# GENERATE MAIN
JTool().initialize()
