from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

import os
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
from macro.rh import RadiantHall

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
    "Hazardous Valley (Veradrix)",
    "Radiant Hall"
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
  btn_misc_test = []
  btn_misc_click = []
  btn_divide_one = []
  chkbtn_leader = []
  chkbtn_member = []
  lbl_macro = []
  lbl_misc = []
  lbl_current_run = []
  lbl_run_time = []
  lbl_restart_note = []
  lbl_pet_action = []
  text_features = []
  frame_root = []
  val_run_count = []
  val_char_class = []
  val_run_restart = []
  val_click_count = []
  val_pword = []
  val_pin = []

  val_leader = 0
  val_member = 0
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
  val_eva = 0

  val_x_coords = []
  val_y_coords = []
  val_misc_x_coords = []
  val_misc_y_coords = []

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
    choice = self.list_dg.get()
    runs = int(self.val_run_count.get())
    access_level = self.get_level()
    char_class = self.val_char_class.get()
    mode = self.val_mode.get()
    leader = self.val_leader.get()
    member = self.val_member.get()
    buff = self.val_buffs.get()
    short = self.val_shorts.get()
    vera = self.val_vera.get()
    run_restart = self.val_run_restart.get()
    pword = self.val_pword.get()
    pin = self.val_pin.get()
    reso = self.val_resolution.get()
    load_time = int(self.val_load_time.get().split(' ')[0])
    dungeon_restart = self.val_dungeon_restart.get()

    self.lbl_run_time.config(text=util.LBL_RUN_TIME_EMPTY)
    if int(run_restart) > 0:
      val_restart_note = util.LBL_RUN_RESTART + util.LBL_RESTART_NOTE_PREFIX + str(run_restart) + util.LBL_RESTART_NOTE_SUFFIX
      self.lbl_restart_note.config(text=val_restart_note)
    else:
      val_restart_note = util.LBL_RUN_RESTART + util.STATE_NA
      self.lbl_restart_note.config(text=val_restart_note)

    self.save_data()
    util.initialize(cabal_window, self.frame_root, self.lbl_macro, self.lbl_current_run, self.lbl_run_time)
    util.initialize_region()
    util.set_variables(access_level, char_class, mode, leader, member, buff, short, vera, runs, run_restart, pword, pin, reso, load_time)

    if dungeon_restart == util.STATE_ONE:
      self.restart_cabal_application()

    if choice == self.LIST_MASTER[0]:
      HazardousValleyAwakened().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[1] or choice == self.LIST_MASTER[2] or choice == self.LIST_MASTER[3]:
      HazardousValley().initialize(self.frame_root, self.btn_start, runs, choice)
    elif choice == self.LIST_MASTER[4]:
      SteamerCrazyAwakened().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[5]:
      CatacombsFrostAwakened().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[6]:
      LavaHellfireAwakened().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[7]:
      HolyWindmill().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[8]:
      TerminusMachina().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[9]:
      PanicCaveAwakened().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[10]:
      HolyKeldrasil().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[11]:
      SienaB1FPrideus().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[12]:
      ChaosInfinity().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[13]:
      HazardousValleyVeradrix().initialize(self.frame_root, self.btn_start, runs)
    elif choice == self.LIST_MASTER[14]:
      RadiantHall().initialize(self.frame_root, self.btn_start, runs)

  def get_dungeon_list(self):
    if self.get_level() == util.ACCESS_FREE:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)"
      ]
    elif self.get_level() == util.ACCESS_PRO:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)",
        "Steamer Crazy (Awakened)",
        "Catacomb Frost (Awakened)",
        "Lava Hellfire (Awakened)"
      ]
    elif self.get_level() == util.ACCESS_PREMIUM:
      self.LIST_DUNGEON = [
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
      self.LIST_DUNGEON = [
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
        "Chaos Infinity"
      ]
    elif self.get_level() == util.ACCESS_TESTER_II:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Steamer Crazy (Awakened)",
        "Catacomb Frost (Awakened)",
        "Lava Hellfire (Awakened)",
        "Holy Keldrasil",
        "Chaos Infinity"
      ]
    elif self.get_level() == util.ACCESS_SUPER:
      self.LIST_DUNGEON = [
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
        "Hazardous Valley (Veradrix)",
        "Radiant Hall"
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
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_PREMIUM or self.get_level() == util.ACCESS_TESTER_II:
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
      case util.DATA_LEADER:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_PREMIUM:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL
      case util.DATA_MEMBER:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_PREMIUM:
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
      case util.DATA_VERADRIX:
        if self.get_level() == util.ACCESS_FREE or self.get_level() == util.ACCESS_PRO or self.get_level() == util.ACCESS_TESTER_II:
          return util.STATE_DISABLED
        else:
          return util.STATE_NORMAL

  def load_node(self):
    self.val_node_data = guard.get_user_value()

  def get_level(self):
    return self.val_node_data[0]

  def get_account(self):
    val_account = str(self.get_level())
    if self.val_node_data[2] != None:
      val_account += util.LBL_HYPHEN
      val_account += self.val_node_data[2]

    return val_account

  def get_license(self):
    return util.LBL_LICENSE + str(self.get_account())

  def get_expiration(self):
    return self.val_node_data[1]

  def get_expiration_status(self):
    if self.val_node_data[1] == None:
      return util.LBL_EXPIRATION_NA
    else:
      return util.LBL_EXPIRATION + str(self.get_expiration().strftime("%B %d, %Y"))

  def load_data(self):
    self.val_config_data = config.load_data()

  def get_data(self, name):
    match name:
      case util.DATA_DUNGEON:
        if self.val_config_data[name] > len(self.LIST_DUNGEON) - 1:
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

    return self.val_config_data[name]

  def save_data(self):
    self.val_config_data[util.DATA_DUNGEON] = self.LIST_DUNGEON.index(self.list_dg.get())
    self.val_config_data[util.DATA_CLASS] = util.LIST_CLASS.index(self.val_char_class.get())
    self.val_config_data[util.DATA_MODE] = self.val_mode.get()
    self.val_config_data[util.DATA_BUFFS] = self.val_buffs.get()
    self.val_config_data[util.DATA_SHORTS] = self.val_shorts.get()
    self.val_config_data[util.DATA_VERADRIX] = self.val_vera.get()
    self.val_config_data[util.DATA_PWORD] = self.val_pword.get()
    self.val_config_data[util.DATA_PIN] = self.val_pin.get()
    self.val_config_data[util.DATA_RESOLUTION] = self.LIST_RESOLUTION.index(self.val_resolution.get())
    self.val_config_data[util.DATA_LOAD] = self.LIST_LOAD_TIME.index(self.val_load_time.get())
    config.save_data(self.val_config_data)

  def enable_party_features(self, args):
    choice = self.list_dg.get()
    if choice == self.LIST_MASTER[12]:
      self.chkbtn_leader.config(state=util.STATE_NORMAL)
      self.chkbtn_member.config(state=util.STATE_NORMAL)
    else:
      self.val_leader.set(0)
      self.val_member.set(0)
      self.chkbtn_leader.config(state=util.STATE_DISABLED)
      self.chkbtn_member.config(state=util.STATE_DISABLED)

  def check_party_leader_state(self):
    self.val_member.set(0)

  def check_party_member_state(self):
    self.val_leader.set(0)

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
    self.btn_train.config(state=util.STATE_DISABLED)
    self.btn_test.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_x_coords.get())
    coor_y = int(self.val_y_coords.get())
    leash.click_test_npc(coor_x, coor_y)

    self.btn_train.config(state=util.STATE_NORMAL)
    self.btn_test.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def pet_train(self):
    self.btn_train.config(state=util.STATE_DISABLED)
    self.btn_test.config(state=util.STATE_DISABLED)
    self.lbl_pet_action.config(text=util.LBL_STATUS_TRAINING)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_x_coords.get())
    coor_y = int(self.val_y_coords.get())
    mcr = self.val_mcr.get()
    crt = self.val_crt.get()
    cdi = self.val_cdi.get()
    crr = self.val_crr.get()
    eva = self.val_eva.get()
    leash.pet_train(coor_x, coor_y, mcr, crt, cdi, crr, eva)

    self.btn_train.config(state=util.STATE_NORMAL)
    self.btn_test.config(state=util.STATE_NORMAL)
    self.lbl_pet_action.config(text=util.LBL_STATUS_IDLE)
    self.frame_root.update()

  def buy_fury(self):
    self.btn_fury.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(125, 205)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_fury.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def buy_upgrade(self):
    self.btn_upgrade.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(15, 180)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_upgrade.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def buy_force(self):
    self.btn_force.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(45, 180)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_force.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def get_mails(self):
    self.btn_mails.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(510, 310, 0.5)
      util.move_click(510, 525, 0.5)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_mails.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def test_custom_clicks(self):
    self.btn_misc_test.config(state=util.STATE_DISABLED)
    self.btn_misc_click.config(state=util.STATE_DISABLED)
    self.btn_divide_one.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    util.move(coor_x, coor_y)

    self.btn_misc_test.config(state=util.STATE_NORMAL)
    self.btn_misc_click.config(state=util.STATE_NORMAL)
    self.btn_divide_one.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def custom_clicks(self):
    self.btn_misc_test.config(state=util.STATE_DISABLED)
    self.btn_misc_click.config(state=util.STATE_DISABLED)
    self.btn_divide_one.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    for x in range(int(self.val_click_count.get())):
      util.move_click(coor_x, coor_y)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_misc_test.config(state=util.STATE_NORMAL)
    self.btn_misc_click.config(state=util.STATE_NORMAL)
    self.btn_divide_one.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def divide_one(self):
    self.btn_misc_test.config(state=util.STATE_DISABLED)
    self.btn_misc_click.config(state=util.STATE_DISABLED)
    self.btn_divide_one.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(util.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    util.move(coor_x, coor_y)

    for x in range(int(self.val_click_count.get())):
      pynboard.press(Key.shift_l)
      time.sleep(0.15)
      pyauto.click(button='right')
      pynboard.release(Key.shift_l)
      time.sleep(0.15)
      pynboard.press('1')
      pynboard.release('1')
      time.sleep(0.15)
      pynboard.press(Key.enter)
      pynboard.release(Key.enter)
      self.log_misc_action(util.MSG_CLICK + str(x+1))

    self.btn_misc_test.config(state=util.STATE_NORMAL)
    self.btn_misc_click.config(state=util.STATE_NORMAL)
    self.btn_divide_one.config(state=util.STATE_NORMAL)
    self.frame_root.update()


  def get_features_free(self):
    self.text_features.configure(state=util.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(util.ACCESS_FREE))
    self.text_features.configure(state=util.STATE_DISABLED)

  def get_features_pro(self):
    self.text_features.configure(state=util.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(util.ACCESS_PRO))
    self.text_features.configure(state=util.STATE_DISABLED)

  def get_features_premium(self):
    self.text_features.configure(state=util.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(util.ACCESS_PREMIUM))
    self.text_features.configure(state=util.STATE_DISABLED)

  def get_changelogs(self):
    self.text_features.configure(state=util.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    text_file = open(util.FILE_CHANGELOG, util.FILE_READ)
    self.text_features.insert(END, text_file.read())

    text_file.close()
    self.text_features.configure(state=util.STATE_DISABLED)

  def log_misc_action(self, message):
    msg_builder = StringVar()
    msg_builder = util.MSG_ACTION + message
    print(msg_builder)
    self.lbl_misc.config(text=msg_builder)
    self.frame_root.update()

  def generate_gui(self):
    # CREATE FRAME
    self.frame_root = Tk()
    self.frame_root.title(util.APP_FULL_NAME)
    self.frame_root.resizable(0, 0)
    self.frame_root.geometry(util.APP_FRAME_SIZE)

    img_photo = PhotoImage(file = util.IMG_APP_ICON)
    self.frame_root.iconphoto(False, img_photo)

    self.frame_root.option_add("*TCombobox*Listbox.font", util.APP_FONT)
    self.frame_root.option_add("*Font", util.APP_FONT)

    tab_control = ttk.Notebook(self.frame_root)
    tab_dungeon = ttk.Frame(tab_control)
    tab_connection = ttk.Frame(tab_control)
    tab_pet = ttk.Frame(tab_control)
    tab_misc = ttk.Frame(tab_control)
    tab_pricing = ttk.Frame(tab_control)
    tab_control.add(tab_dungeon, text=util.TAB_DUNGEON, state=self.get_access(util.DATA_DUNGEON))
    tab_control.add(tab_connection, text=util.TAB_CONNECTION, state=self.get_access(util.DATA_CONNECTION))
    tab_control.add(tab_pet, text=util.TAB_PET, state=self.get_access(util.DATA_PET))
    tab_control.add(tab_misc, text=util.TAB_OTHERS, state=self.get_access(util.DATA_OTHERS))
    tab_control.add(tab_pricing, text=util.TAB_PRICING)
    tab_control.pack(expand=1, fill="both")

    # Tab Dungeon
    lbl_dungeon_list = Label(tab_dungeon, text=util.LBL_DUNGEON)
    lbl_dungeon_list.place(x=10, y=10)

    self.list_dg = ttk.Combobox(tab_dungeon, values=self.LIST_DUNGEON, state=util.STATE_READONLY)
    self.list_dg.current(self.get_data(util.DATA_DUNGEON))
    self.list_dg.config(width=30)
    self.list_dg.place(x=75, y=10)
    self.list_dg.bind("<<ComboboxSelected>>", self.enable_party_features)

    lbl_runs = Label(tab_dungeon, text=util.LBL_RUNS)
    lbl_runs.place(x=10, y=43)

    self.val_run_count = ttk.Combobox(tab_dungeon, values=self.LIST_RUN, state=util.STATE_NORMAL)
    self.val_run_count.current(0)
    self.val_run_count.config(width=5)
    self.val_run_count.place(x=75, y=43)

    lbl_vera = Label(tab_dungeon, text=util.LBL_VERADRIX, state=self.get_access(util.DATA_VERADRIX))
    lbl_vera.place(x=145, y=43)

    self.val_vera = IntVar(value=self.get_data(util.DATA_VERADRIX))
    chkbtn_vera = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_vera, state=self.get_access(util.DATA_VERADRIX))
    chkbtn_vera.place(x=210, y=44)

    self.btn_start = Button(tab_dungeon, text=util.BTN_START, command=self.start)
    self.btn_start.config(width=6)
    self.btn_start.place(x=255, y=40)

    self.lbl_current_run = Label(tab_dungeon, text=util.LBL_CURRENT_RUN)
    self.lbl_current_run.place(x=145, y=75)

    self.lbl_run_time = Label(tab_dungeon, text=util.LBL_RUN_TIME_EMPTY)
    self.lbl_run_time.place(x=145, y=105)

    lbl_class = Label(tab_dungeon, text=util.LBL_CLASS, state=self.get_access(util.DATA_MODE))
    lbl_class.place(x=10, y=73)

    self.val_char_class = ttk.Combobox(tab_dungeon, values=util.LIST_CLASS, state=util.STATE_READONLY)
    self.val_char_class.current(self.get_data(util.DATA_CLASS))
    self.val_char_class.config(width=5)
    self.val_char_class.place(x=75, y=73)

    lbl_mode = Label(tab_dungeon, text=util.LBL_MODE, state=self.get_access(util.DATA_MODE))
    lbl_mode.place(x=10, y=105)

    self.val_mode = IntVar(value=self.get_data(util.DATA_MODE))
    chkbtn_mode = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_mode, state=self.get_access(util.DATA_MODE))
    chkbtn_mode.place(x=75, y=106)

    lbl_buffs = Label(tab_dungeon, text=util.LBL_BUFFS, state=self.get_access(util.DATA_BUFFS))
    lbl_buffs.place(x=10, y=135)

    self.val_buffs = IntVar(value=self.get_data(util.DATA_BUFFS))
    chkbtn_buffs = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_buffs, state=self.get_access(util.DATA_BUFFS))
    chkbtn_buffs.place(x=75, y=136)

    lbl_shorts = Label(tab_dungeon, text=util.LBL_SHORTS, state=self.get_access(util.DATA_SHORTS))
    lbl_shorts.place(x=10, y=165)

    self.val_shorts = IntVar(value=self.get_data(util.DATA_SHORTS))
    chkbtn_shorts = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_shorts, state=self.get_access(util.DATA_SHORTS))
    chkbtn_shorts.place(x=75, y=166)

    lbl_leader = Label(tab_dungeon, text=util.LBL_LEADER, state=self.get_access(util.DATA_LEADER))
    lbl_leader.place(x=10, y=195)

    self.val_leader = IntVar(value=0)
    self.chkbtn_leader = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_leader, command=self.check_party_leader_state, state=self.get_access(util.DATA_LEADER))
    self.chkbtn_leader.place(x=75, y=196)

    lbl_member = Label(tab_dungeon, text=util.LBL_MEMBER, state=self.get_access(util.DATA_MEMBER))
    lbl_member.place(x=10, y=225)

    self.val_member = IntVar(value=0)
    self.chkbtn_member = ttk.Checkbutton(tab_dungeon, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_member, command=self.check_party_member_state, state=self.get_access(util.DATA_MEMBER))
    self.chkbtn_member.place(x=75, y=226)

    self.lbl_restart_note = Label(tab_dungeon, text=util.LBL_RUN_RESTART_EMPTY)
    self.lbl_restart_note.place(x=145, y=135)

    lbl_license = Label(tab_dungeon, text=self.get_license())
    lbl_license.place(x=145, y=165)

    lbl_expiration = Label(tab_dungeon, text=self.get_expiration_status())
    lbl_expiration.place(x=145, y=195)

    self.lbl_macro = Label(tab_dungeon, text=util.LBL_MACRO)
    self.lbl_macro.place(x=145, y=225)

    # Tab Connection
    lbl_run_restart = Label(tab_connection, text=util.LBL_RUN_RESTART)
    lbl_run_restart.place(x=10, y=10)

    self.val_run_restart = ttk.Combobox(tab_connection, values=self.LIST_RUN_RESTART)
    self.val_run_restart.current(0)
    self.val_run_restart.config(width=5)
    self.val_run_restart.place(x=92, y=10)

    lbl_run_restart_note = Label(tab_connection, text=util.LBL_RUN_RESTART_NOTE)
    lbl_run_restart_note.place(x=155, y=10)

    lbl_dungeon_restart = Label(tab_connection, text=util.LBL_DG_RESTART)
    lbl_dungeon_restart.place(x=10, y=43)

    self.val_dungeon_restart = IntVar(value=0)
    chkbtn_dungeon_restart = ttk.Checkbutton(tab_connection, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_dungeon_restart)
    chkbtn_dungeon_restart.place(x=90, y=43)

    lbl_dungeon_restart_note = Label(tab_connection, text=util.LBL_DG_RESTART_NOTE)
    lbl_dungeon_restart_note.place(x=155, y=43)

    lbl_pword = Label(tab_connection, text=util.LBL_PWORD)
    lbl_pword.place(x=10, y=75)

    self.val_pword = StringVar()
    self.val_pword.set(self.get_data(util.DATA_PWORD))
    entry_pword = Entry(tab_connection, show="*", textvariable=self.val_pword, width=15)
    entry_pword.place(x=85, y=75)

    lbl_pin = Label(tab_connection, text=util.LBL_PIN)
    lbl_pin.place(x=205, y=75)

    self.val_pin = StringVar()
    self.val_pin.set(self.get_data(util.DATA_PIN))
    entry_pin = Entry(tab_connection, show="*", textvariable=self.val_pin, width=10)
    entry_pin.place(x=240, y=75)

    lbl_resolution = Label(tab_connection, text=util.LBL_RESOLUTION)
    lbl_resolution.place(x=10, y=105)

    self.val_resolution = ttk.Combobox(tab_connection, values=self.LIST_RESOLUTION, state=util.STATE_READONLY)
    self.val_resolution.current(self.get_data(util.DATA_RESOLUTION))
    self.val_resolution.config(width=12)
    self.val_resolution.place(x=85, y=105)

    lbl_resolution_note = Label(tab_connection, text=util.LBL_RESOLUTION_NOTE)
    lbl_resolution_note.place(x=10, y=135)

    lbl_load_time = Label(tab_connection, text=util.LBL_LOAD_TIME)
    lbl_load_time.place(x=10, y=165)

    self.val_load_time = ttk.Combobox(tab_connection, values=self.LIST_LOAD_TIME, state=util.STATE_READONLY)
    self.val_load_time.current(self.get_data(util.DATA_LOAD))
    self.val_load_time.config(width=12)
    self.val_load_time.place(x=85, y=165)

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

    self.val_x_coords = StringVar()
    self.val_x_coords.set(self.val_def_x)
    entry_x_coords = Entry(tab_pet, textvariable=self.val_x_coords, justify='center', width=5)
    entry_x_coords.place(x=62, y=105)

    lbl_y_coords = Label(tab_pet, text=util.LBL_NPC_Y)
    lbl_y_coords.place(x=110, y=103)

    self.val_y_coords = StringVar()
    self.val_y_coords.set(self.val_def_y)
    entry_y_coords = Entry(tab_pet, textvariable=self.val_y_coords, justify='center', width=5)
    entry_y_coords.place(x=162, y=105)

    self.btn_test = Button(tab_pet, text=util.BTN_TEST, command=self.pet_test)
    self.btn_test.config(width=5)
    self.btn_test.place(x=210, y=100)

    self.btn_train = Button(tab_pet, text=util.BTN_TRAIN, command=self.pet_train)
    self.btn_train.config(width=6)
    self.btn_train.place(x=260, y=100)

    lbl_pet_note_4 = Label(tab_pet, text=util.LBL_PET_NOTE_4)
    lbl_pet_note_4.place(x=10, y=135)

    lbl_mcr = Label(tab_pet, text=util.LBL_MCR)
    lbl_mcr.place(x=10, y=165)

    self.val_mcr = IntVar(value=1)
    chkbtn_mcr = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_mcr, state=util.NORMAL)
    chkbtn_mcr.place(x=45, y=166)

    lbl_crt = Label(tab_pet, text=util.LBL_CRT)
    lbl_crt.place(x=70, y=165)

    self.val_crt = IntVar(value=0)
    chkbtn_crt = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_crt, state=util.NORMAL)
    chkbtn_crt.place(x=105, y=166)

    lbl_cdi = Label(tab_pet, text=util.LBL_CDI)
    lbl_cdi.place(x=130, y=165)

    self.val_cdi = IntVar(value=0)
    chkbtn_cdi = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_cdi, state=util.NORMAL)
    chkbtn_cdi.place(x=165, y=166)

    lbl_crr = Label(tab_pet, text=util.LBL_CRR)
    lbl_crr.place(x=190, y=165)

    self.val_crr = IntVar(value=0)
    chkbtn_crr = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_crr, state=util.NORMAL)
    chkbtn_crr.place(x=225, y=166)

    lbl_eva = Label(tab_pet, text=util.LBL_EVA)
    lbl_eva.place(x=250, y=165)

    self.val_eva = IntVar(value=0)
    chkbtn_eva = ttk.Checkbutton(tab_pet, text=util.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_eva, state=util.NORMAL)
    chkbtn_eva.place(x=285, y=166)

    lbl_pet_note_5 = Label(tab_pet, text=util.LBL_PET_NOTE_5)
    lbl_pet_note_5.place(x=10, y=195)

    self.lbl_pet_action = Label(tab_pet, text=util.LBL_STATUS_IDLE)
    self.lbl_pet_action.place(x=10, y=225)

    # Tab Misc
    lbl_store_note = Label(tab_misc, text=util.LBL_STORE_NOTE)
    lbl_store_note.place(x=10, y=10)

    self.btn_fury = Button(tab_misc, text=util.BTN_FURY, command=self.buy_fury)
    self.btn_fury.config(width=8)
    self.btn_fury.place(x=10, y=40)

    self.btn_upgrade = Button(tab_misc, text=util.BTN_UPGRADE, command=self.buy_upgrade)
    self.btn_upgrade.config(width=8)
    self.btn_upgrade.place(x=85, y=40)

    self.btn_force = Button(tab_misc, text=util.BTN_FORCE, command=self.buy_force)
    self.btn_force.config(width=8)
    self.btn_force.place(x=160, y=40)

    lbl_mail_note = Label(tab_misc, text=util.LBL_MAIL_NOTE)
    lbl_mail_note.place(x=10, y=80)

    self.btn_mails = Button(tab_misc, text=util.BTN_MAILS, command=self.get_mails)
    self.btn_mails.config(width=8)
    self.btn_mails.place(x=235, y=40)

    lbl_misc_x_coords = Label(tab_misc, text=util.LBL_NPC_X)
    lbl_misc_x_coords.place(x=10, y=113)

    self.val_misc_x_coords = StringVar()
    self.val_misc_x_coords.set('1050')
    entry_x_coords = Entry(tab_misc, textvariable=self.val_misc_x_coords, justify='center', width=5)
    entry_x_coords.place(x=62, y=115)

    lbl_misc_y_coords = Label(tab_misc, text=util.LBL_NPC_Y)
    lbl_misc_y_coords.place(x=110, y=113)

    self.val_misc_y_coords = StringVar()
    self.val_misc_y_coords.set('375')
    entry_y_coords = Entry(tab_misc, textvariable=self.val_misc_y_coords, justify='center', width=5)
    entry_y_coords.place(x=162, y=115)

    self.btn_misc_test = Button(tab_misc, text=util.BTN_TEST, command=self.test_custom_clicks)
    self.btn_misc_test.config(width=5)
    self.btn_misc_test.place(x=10, y=150)

    self.btn_misc_click = Button(tab_misc, text=util.BTN_CLICK, command=self.custom_clicks)
    self.btn_misc_click.config(width=6)
    self.btn_misc_click.place(x=60, y=150)

    self.btn_divide_one = Button(tab_misc, text=util.BTN_DIVIDE_ONE, command=self.divide_one)
    self.btn_divide_one.config(width=9)
    self.btn_divide_one.place(x=118, y=150)

    lbl_misc_custom_note = Label(tab_misc, text=util.LBL_CUSTON_CLICK_NOTE)
    lbl_misc_custom_note.place(x=10, y=190)

    lbl_misc_clicks = Label(tab_misc, text=util.LBL_CLICKS)
    lbl_misc_clicks.place(x=10, y=220)

    self.val_click_count = ttk.Combobox(tab_misc, values=self.LIST_CLICKS, state=util.STATE_NORMAL)
    self.val_click_count.current(0)
    self.val_click_count.config(width=5)
    self.val_click_count.place(x=75, y=220)

    self.lbl_misc = Label(tab_misc, text=util.LBL_CLICK)
    self.lbl_misc.place(x=160, y=220)

    # Tab Pricing
    frame_btn = Frame(tab_pricing)
    frame_btn.pack(anchor="w")

    scroll_features = Scrollbar(tab_pricing)
    scroll_features.pack(side=RIGHT, fill=Y)

    self.text_features = Text(tab_pricing, yscrollcommand=scroll_features.set)
    self.text_features.pack()
    self.get_features_free()

    btn_free = Button(frame_btn, text=util.BTN_FREE, command=self.get_features_free)
    btn_free.pack(side=LEFT)

    btn_pro = Button(frame_btn, text=util.BTN_PRO, command=self.get_features_pro)
    btn_pro.pack(side=LEFT)

    btn_premium = Button(frame_btn, text=util.BTN_PREMIUM, command=self.get_features_premium)
    btn_premium.pack(side=LEFT)

    btn_changelogs = Button(frame_btn, text=util.BTN_CHANGELOG, command=self.get_changelogs)
    btn_changelogs.pack(side=LEFT)

    self.enable_party_features(None)
    self.frame_root.mainloop()

# GENERATE MAIN
JTool().initialize()
