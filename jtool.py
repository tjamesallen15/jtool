import time
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

import common.guard as guard
import common.config as config
import common.features as features
import common.leash as leash
import common.constants as consts
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
from macro.potf import PurifierOfTheForest
from macro.mi import MirageIsland
from macro.scp import SteamerCrazyPremium
from macro.cls import Celestia

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
    "Purifier of the Forest",
    "Mirage Island",
    "Steamer Crazy (Premium)",
    "Celestia"
  ]

  LIST_DUNGEON = []
  LIST_RUN = [1, 5, 10, 20, 30, 40, 50, 100, 150, 200]
  LIST_RUN_RESTART = [0, 10, 20, 30, 40, 50, 75, 100]
  LIST_CLICKS = [10, 20, 30, 40, 50, 100, 200, 300, 500]
  LIST_RESOLUTION = ["2560x1440", "1920x1080"]
  LIST_LOAD_TIME = ["30 seconds", "45 seconds", "60 seconds", "75 seconds", "90 seconds", "105 seconds", "120 seconds"]
  LIST_CHANNEL = [1, 2, 3, 4]

  list_dg = []
  btn_start = []
  btn_fury = []
  btn_force = []
  btn_upgrade = []
  btn_mails = []
  btn_test = []
  btn_train = []
  btn_misc_test = []
  btn_misc_click = []
  btn_join_war = []
  btn_move_window = []
  btn_divide_one = []
  btn_transfer = []
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
  val_cancel_buffs = 0
  val_debuffs = 0
  val_hard_debuffs = 0
  val_shorts = 1
  val_hard_shorts = 0
  val_atk_type = 0
  val_vera = 0
  val_close_app = 0
  val_archer = 0
  val_resolution = 0
  val_load_time = 0
  val_channel = 4
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

  def join_war(self):
    cabal_window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()
    i = 0
    while i <= 25:
      util.move_click(1235, 585)
      util.move_click(630, 440)
      i += 1

  def move_app(self):
    cabal_window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    resolution = self.val_resolution.get()
    coords = util.get_window_coordinates(resolution)
    application = pyauto.getActiveWindow()
    application.moveTo(coords[0], coords[1])

  def start(self):
    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    selected_dungeon = self.list_dg.get()

    variable_args = {
      consts.DATA_ACCESS_LEVEL: self.get_level(),
      consts.DATA_LEADER: self.val_leader.get(),
      consts.DATA_MEMBER: self.val_member.get(),
      consts.DATA_CHAR_CLASS: self.val_char_class.get(),
      consts.DATA_MODE: self.val_mode.get(),
      consts.DATA_BUFFS: self.val_buffs.get(),
      consts.DATA_CANCEL_BUFFS: self.val_cancel_buffs.get(),
      consts.DATA_DEBUFFS: self.val_debuffs.get(),
      consts.DATA_HARD_DEBUFFS: self.val_hard_debuffs.get(),
      consts.DATA_SHORTS: self.val_shorts.get(),
      consts.DATA_HARD_SHORTS: self.val_hard_shorts.get(),
      consts.DATA_VERADRIX: self.val_vera.get(),
      consts.DATA_RUNS: int(self.val_run_count.get()),
      consts.DATA_RUN_RESTART: self.val_run_restart.get(),
      consts.DATA_CLOSE_APP: self.val_close_app.get(),
      consts.DATA_PWORD: self.val_pword.get(),
      consts.DATA_PIN: self.val_pin.get(),
      consts.DATA_RESOLUTION: self.val_resolution.get(),
      consts.DATA_CHANNEL: int(self.val_channel.get()),
      consts.DATA_LOAD: int(self.val_load_time.get().split(' ')[0])
    }

    dungeon_args = {
      consts.DATA_FRAME: self.frame_root,
      consts.DATA_BUTTON: self.btn_start,
      consts.DATA_RUNS: variable_args[consts.DATA_RUNS],
      consts.DATA_DUNGEON: selected_dungeon
    }

    runs = variable_args[consts.DATA_RUNS]
    run_restart = variable_args[consts.DATA_RUN_RESTART]
    dungeon_restart = self.val_dungeon_restart.get()

    self.lbl_run_time.config(text=consts.LBL_RUN_TIME_EMPTY)
    if int(run_restart) > 0:
      val_restart_note = consts.LBL_RUN_RESTART + consts.LBL_RESTART_NOTE_PREFIX + str(run_restart) + consts.LBL_RESTART_NOTE_SUFFIX
      self.lbl_restart_note.config(text=val_restart_note)
    else:
      val_restart_note = consts.LBL_RUN_RESTART + consts.STATE_NA
      self.lbl_restart_note.config(text=val_restart_note)

    self.save_data()
    util.initialize(cabal_window, self.frame_root, self.lbl_macro, self.lbl_current_run, self.lbl_run_time)
    util.initialize_region()
    util.set_variables(variable_args)

    if dungeon_restart == consts.STATE_ONE:
      self.restart_application()

    match selected_dungeon:
      case consts.DG_HVA: HazardousValleyAwakened().initialize(dungeon_args)
      case consts.DG_HVH: HazardousValley().initialize(dungeon_args)
      case consts.DG_HVM: HazardousValley().initialize(dungeon_args)
      case consts.DG_HVE: HazardousValley().initialize(dungeon_args)
      case consts.DG_SCA: SteamerCrazyAwakened().initialize(dungeon_args)
      case consts.DG_CFA: CatacombsFrostAwakened().initialize(dungeon_args)
      case consts.DG_LHA: LavaHellfireAwakened().initialize(dungeon_args)
      case consts.DG_HW: HolyWindmill().initialize(dungeon_args)
      case consts.DG_TM: TerminusMachina().initialize(dungeon_args)
      case consts.DG_PCA: PanicCaveAwakened().initialize(dungeon_args)
      case consts.DG_HK: HolyKeldrasil().initialize(dungeon_args)
      case consts.DG_S1P: SienaB1FPrideus().initialize(dungeon_args)
      case consts.DG_CI: ChaosInfinity().initialize(dungeon_args)
      case consts.DG_HVV: HazardousValleyVeradrix().initialize(dungeon_args)
      case consts.DG_POTF: PurifierOfTheForest().initialize(dungeon_args)
      case consts.DG_SCP: SteamerCrazyPremium().initialize(dungeon_args)
      case consts.DG_MI: MirageIsland().initialize(dungeon_args)
      case consts.DG_CLS: Celestia().initialize(dungeon_args)

  def get_dungeon_list(self):
    if self.get_level() == consts.ACCESS_FREE:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)"
      ]
    elif self.get_level() == consts.ACCESS_PRO:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)",
        "Steamer Crazy (Awakened)",
        "Catacomb Frost (Awakened)",
        "Lava Hellfire (Awakened)"
      ]
    elif self.get_level() == consts.ACCESS_PREMIUM:
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
    elif self.get_level() == consts.ACCESS_TESTER:
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
        "Chaos Infinity",
        "Mirage Island"
      ]
    elif self.get_level() == consts.ACCESS_TESTER_II:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Steamer Crazy (Awakened)",
        "Catacomb Frost (Awakened)",
        "Lava Hellfire (Awakened)",
        "Holy Keldrasil",
        "Chaos Infinity"
      ]
    elif self.get_level() == consts.ACCESS_SUPER:
      self.LIST_DUNGEON = [
        "Hazardous Valley (Awakened)",
        "Hazardous Valley (Hard)",
        "Hazardous Valley (Medium)",
        "Hazardous Valley (Easy)",
        "Steamer Crazy (Premium)",
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
        "Mirage Island",
        "Celestia",
        "Purifier of the Forest"
      ]

  def get_access(self, feature):
    match feature:
      case consts.DATA_DUNGEON:
        return consts.STATE_NORMAL
      case consts.DATA_CONNECTION:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_PET:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM or self.get_level() == consts.ACCESS_TESTER_II: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_OTHERS:
        if self.get_level() == consts.ACCESS_FREE: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_MODE:
        if self.get_level() == consts.ACCESS_FREE: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_LEADER:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_MEMBER:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_BUFFS:
        return consts.STATE_NORMAL
      case consts.DATA_DEBUFFS:
        if self.get_level() != consts.ACCESS_SUPER: return consts.STATE_DISABLED
      case consts.DATA_HARD_DEBUFFS:
        if self.get_level() != consts.ACCESS_SUPER: return consts.STATE_DISABLED
      case consts.DATA_SHORTS:
        if self.get_level() == consts.ACCESS_FREE: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_HARD_SHORTS:
        if self.get_level() == consts.ACCESS_FREE: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_VERADRIX:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_TESTER_II: return consts.STATE_DISABLED
        else: return consts.STATE_NORMAL
      case consts.DATA_JOIN_WAR:
        if self.get_level() == consts.ACCESS_SUPER: return consts.STATE_NORMAL
        else: return consts.STATE_DISABLED
      case _:
        return consts.STATE_DISABLED

  def load_node(self):
    self.val_node_data = guard.get_user_value()

  def get_level(self):
    return self.val_node_data[0]

  def get_account(self):
    val_account = str(self.get_level())
    if self.val_node_data[2] != None:
      val_account += consts.LBL_HYPHEN
      val_account += self.val_node_data[2]

    return val_account

  def get_license(self):
    return consts.LBL_LICENSE + str(self.get_account())

  def get_expiration(self):
    return self.val_node_data[1]

  def get_expiration_status(self):
    if self.val_node_data[1] == None:
      return consts.LBL_EXPIRATION_NA
    else:
      return consts.LBL_EXPIRATION + str(self.get_expiration().strftime("%B %d, %Y"))

  def load_data(self):
    self.val_config_data = config.load_data()

  def get_data(self, name):
    match name:
      case consts.DATA_DUNGEON:
        if self.val_config_data[name] > len(self.LIST_DUNGEON) - 1:
          return consts.STATE_ZERO
      case consts.DATA_MODE:
        if self.get_level() == consts.ACCESS_FREE:
          return consts.STATE_ZERO
      case consts.DATA_DEBUFFS:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM or self.get_level() == consts.ACCESS_TESTER or self.get_level() == consts.ACCESS_TESTER_II:
          return consts.STATE_ZERO
      case consts.DATA_HARD_DEBUFFS:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM or self.get_level() == consts.ACCESS_TESTER or self.get_level() == consts.ACCESS_TESTER_II:
          return consts.STATE_ZERO
      case consts.DATA_SHORTS:
        if self.get_level() == consts.ACCESS_FREE:
          return consts.STATE_ZERO
      case consts.DATA_HARD_SHORTS:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO or self.get_level() == consts.ACCESS_PREMIUM or self.get_level() == consts.ACCESS_TESTER or self.get_level() == consts.ACCESS_TESTER_II:
          return consts.STATE_ZERO
      case consts.DATA_VERADRIX:
        if self.get_level() == consts.ACCESS_FREE or self.get_level() == consts.ACCESS_PRO:
          return consts.STATE_ZERO

    return self.val_config_data[name]

  def save_data(self):
    self.val_config_data[consts.DATA_DUNGEON] = self.LIST_DUNGEON.index(self.list_dg.get())
    self.val_config_data[consts.DATA_CLASS] = consts.LIST_CLASS.index(self.val_char_class.get())
    self.val_config_data[consts.DATA_MODE] = self.val_mode.get()
    self.val_config_data[consts.DATA_BUFFS] = self.val_buffs.get()
    self.val_config_data[consts.DATA_DEBUFFS] = self.val_debuffs.get()
    self.val_config_data[consts.DATA_HARD_DEBUFFS] = self.val_hard_debuffs.get()
    self.val_config_data[consts.DATA_SHORTS] = self.val_shorts.get()
    self.val_config_data[consts.DATA_HARD_SHORTS] = self.val_hard_shorts.get()
    self.val_config_data[consts.DATA_VERADRIX] = self.val_vera.get()
    self.val_config_data[consts.DATA_PWORD] = self.val_pword.get()
    self.val_config_data[consts.DATA_PIN] = self.val_pin.get()
    self.val_config_data[consts.DATA_RESOLUTION] = self.LIST_RESOLUTION.index(self.val_resolution.get())
    self.val_config_data[consts.DATA_CHANNEL] = self.LIST_CHANNEL.index(int(self.val_channel.get()))
    self.val_config_data[consts.DATA_LOAD] = self.LIST_LOAD_TIME.index(self.val_load_time.get())
    config.save_data(self.val_config_data)

  def enable_dungeon_features(self, args):
    selected_dungeon = self.list_dg.get()

    if selected_dungeon == consts.DG_TM:
      self.chkbtn_leader.config(state=consts.STATE_NORMAL)
      self.chkbtn_member.config(state=consts.STATE_NORMAL)
    elif selected_dungeon == consts.DG_CI:
      self.chkbtn_leader.config(state=consts.STATE_NORMAL)
      self.chkbtn_member.config(state=consts.STATE_NORMAL)
    elif selected_dungeon == consts.DG_POTF:
      self.chkbtn_leader.config(state=consts.STATE_NORMAL)
      self.chkbtn_member.config(state=consts.STATE_NORMAL)
    elif selected_dungeon == consts.DG_MI:
      self.chkbtn_leader.config(state=consts.STATE_NORMAL)
      self.chkbtn_member.config(state=consts.STATE_NORMAL)
    elif selected_dungeon == consts.DG_CLS:
      self.chkbtn_leader.config(state=consts.STATE_NORMAL)
      self.chkbtn_member.config(state=consts.STATE_NORMAL)
    else:
      self.val_leader.set(0)
      self.val_member.set(0)
      self.chkbtn_leader.config(state=consts.STATE_DISABLED)
      self.chkbtn_member.config(state=consts.STATE_DISABLED)

  def check_party_leader_state(self):
    self.val_member.set(0)

  def check_party_member_state(self):
    self.val_leader.set(0)

  def restart_application(self):
    util.log_action(consts.MSG_DUNGEON_RESTART)
    util.restart_application()

  def generate_matrix(self):
    leash.generate_matrix()

  def pet_test(self):
    self.btn_train.config(state=consts.STATE_DISABLED)
    self.btn_test.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_x_coords.get())
    coor_y = int(self.val_y_coords.get())
    leash.click_test_npc(coor_x, coor_y)

    self.btn_train.config(state=consts.STATE_NORMAL)
    self.btn_test.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def pet_train(self):
    self.btn_train.config(state=consts.STATE_DISABLED)
    self.btn_test.config(state=consts.STATE_DISABLED)
    self.lbl_pet_action.config(text=consts.LBL_STATUS_TRAINING)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
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

    self.btn_train.config(state=consts.STATE_NORMAL)
    self.btn_test.config(state=consts.STATE_NORMAL)
    self.lbl_pet_action.config(text=consts.LBL_STATUS_IDLE)
    self.frame_root.update()

  def buy_fury(self):
    self.btn_fury.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(125, 205)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_fury.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def buy_upgrade(self):
    self.btn_upgrade.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(15, 180)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_upgrade.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def buy_force(self):
    self.btn_force.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(45, 180)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_force.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def get_mails(self):
    self.btn_mails.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    for x in range(int(self.val_click_count.get())):
      util.move_click(510, 310, 0.5)
      util.move_click(510, 525, 0.5)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_mails.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def test_custom_clicks(self):
    self.btn_misc_test.config(state=consts.STATE_DISABLED)
    self.btn_misc_click.config(state=consts.STATE_DISABLED)
    self.btn_divide_one.config(state=consts.STATE_DISABLED)
    self.btn_transfer.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    util.move(coor_x, coor_y)

    self.btn_misc_test.config(state=consts.STATE_NORMAL)
    self.btn_misc_click.config(state=consts.STATE_NORMAL)
    self.btn_divide_one.config(state=consts.STATE_NORMAL)
    self.btn_transfer.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def custom_clicks(self):
    self.btn_misc_test.config(state=consts.STATE_DISABLED)
    self.btn_misc_click.config(state=consts.STATE_DISABLED)
    self.btn_divide_one.config(state=consts.STATE_DISABLED)
    self.btn_transfer.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    for x in range(int(self.val_click_count.get())):
      util.move_click(coor_x, coor_y)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_misc_test.config(state=consts.STATE_NORMAL)
    self.btn_misc_click.config(state=consts.STATE_NORMAL)
    self.btn_divide_one.config(state=consts.STATE_NORMAL)
    self.btn_transfer.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def divide_one(self):
    self.btn_misc_test.config(state=consts.STATE_DISABLED)
    self.btn_misc_click.config(state=consts.STATE_DISABLED)
    self.btn_divide_one.config(state=consts.STATE_DISABLED)
    self.btn_transfer.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    coor_x = int(self.val_misc_x_coords.get())
    coor_y = int(self.val_misc_y_coords.get())

    util.move(coor_x, coor_y)

    for x in range(int(self.val_click_count.get())):
      util.click_press_combo(Key.shift_l, '1', True)
      util.press_release(Key.enter)
      self.log_misc_action(consts.MSG_CLICK + str(x+1))

    self.btn_misc_test.config(state=consts.STATE_NORMAL)
    self.btn_misc_click.config(state=consts.STATE_NORMAL)
    self.btn_divide_one.config(state=consts.STATE_NORMAL)
    self.btn_transfer.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def transfer(self):
    self.btn_misc_test.config(state=consts.STATE_DISABLED)
    self.btn_misc_click.config(state=consts.STATE_DISABLED)
    self.btn_divide_one.config(state=consts.STATE_DISABLED)
    self.btn_transfer.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    click_count = int(self.val_click_count.get())

    cabal_window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()

    transferring = True
    index = 0
    while transferring:
      if index >= 64 or index >= click_count:
        transferring = False

      if transferring == False:
        break

      util.move(leash.get_inventory_matrix()[index][0], leash.get_inventory_matrix()[index][1], 0.1)
      util.click_press_combo(Key.ctrl, consts.STATE_EMPTY, False)
      self.log_misc_action(consts.MSG_CLICK + str(index+1))
      index += 1

    self.btn_misc_test.config(state=consts.STATE_NORMAL)
    self.btn_misc_click.config(state=consts.STATE_NORMAL)
    self.btn_divide_one.config(state=consts.STATE_NORMAL)
    self.btn_transfer.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  def get_features_free(self):
    self.text_features.configure(state=consts.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(consts.ACCESS_FREE))
    self.text_features.configure(state=consts.STATE_DISABLED)

  def get_features_pro(self):
    self.text_features.configure(state=consts.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(consts.ACCESS_PRO))
    self.text_features.configure(state=consts.STATE_DISABLED)

  def get_features_premium(self):
    self.text_features.configure(state=consts.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    self.text_features.insert(END, features.get_features(consts.ACCESS_PREMIUM))
    self.text_features.configure(state=consts.STATE_DISABLED)

  def get_changelogs(self):
    self.text_features.configure(state=consts.STATE_NORMAL)
    self.text_features.delete('1.0', END)
    text_file = open(util.FILE_CHANGELOG, util.FILE_READ)
    self.text_features.insert(END, text_file.read())

    text_file.close()
    self.text_features.configure(state=consts.STATE_DISABLED)

  def log_misc_action(self, message):
    msg_builder = StringVar()
    msg_builder = consts.MSG_ACTION + message
    print(msg_builder)
    self.lbl_misc.config(text=msg_builder)
    self.frame_root.update()

  def generate_gui(self):
    # CREATE FRAME
    self.frame_root = Tk()
    self.frame_root.title(consts.APP_FULL_NAME)
    self.frame_root.resizable(0, 0)
    self.frame_root.geometry(consts.APP_FRAME_SIZE)

    img_photo = PhotoImage(file = consts.IMG_APP_ICON)
    self.frame_root.iconphoto(False, img_photo)

    self.frame_root.option_add("*TCombobox*Listbox.font", consts.APP_FONT)
    self.frame_root.option_add("*Font", consts.APP_FONT)

    tab_control = ttk.Notebook(self.frame_root)
    tab_dungeon = ttk.Frame(tab_control)
    tab_connection = ttk.Frame(tab_control)
    tab_pet = ttk.Frame(tab_control)
    tab_misc = ttk.Frame(tab_control)
    tab_pricing = ttk.Frame(tab_control)
    tab_control.add(tab_dungeon, text=consts.TAB_DUNGEON, state=self.get_access(consts.DATA_DUNGEON))
    tab_control.add(tab_connection, text=consts.TAB_CONNECTION, state=self.get_access(consts.DATA_CONNECTION))
    tab_control.add(tab_pet, text=consts.TAB_PET, state=self.get_access(consts.DATA_PET))
    tab_control.add(tab_misc, text=consts.TAB_OTHERS, state=self.get_access(consts.DATA_OTHERS))
    tab_control.add(tab_pricing, text=consts.TAB_PRICING)
    tab_control.pack(expand=1, fill="both")

    # Tab Dungeon
    lbl_dungeon_list = Label(tab_dungeon, text=consts.LBL_DUNGEON)
    lbl_dungeon_list.place(x=10, y=10)

    self.list_dg = ttk.Combobox(tab_dungeon, values=self.LIST_DUNGEON, justify=consts.STATE_CENTER, state=consts.STATE_READONLY)
    self.list_dg.current(self.get_data(consts.DATA_DUNGEON))
    self.list_dg.config(width=30)
    self.list_dg.place(x=75, y=10)
    self.list_dg.bind("<<ComboboxSelected>>", self.enable_dungeon_features)

    lbl_runs = Label(tab_dungeon, text=consts.LBL_RUNS)
    lbl_runs.place(x=10, y=43)

    self.val_run_count = ttk.Combobox(tab_dungeon, justify=consts.STATE_CENTER, values=self.LIST_RUN, state=consts.STATE_NORMAL)
    self.val_run_count.current(0)
    self.val_run_count.config(width=5)
    self.val_run_count.place(x=75, y=43)

    lbl_vera = Label(tab_dungeon, text=consts.LBL_VERADRIX, state=self.get_access(consts.DATA_VERADRIX))
    lbl_vera.place(x=145, y=43)

    self.val_vera = IntVar(value=self.get_data(consts.DATA_VERADRIX))
    chkbtn_vera = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_vera, state=self.get_access(consts.DATA_VERADRIX))
    chkbtn_vera.place(x=210, y=44)

    self.btn_start = Button(tab_dungeon, text=consts.BTN_START, command=self.start)
    self.btn_start.config(width=6)
    self.btn_start.place(x=255, y=40)

    self.lbl_current_run = Label(tab_dungeon, text=consts.LBL_CURRENT_RUN)
    self.lbl_current_run.place(x=145, y=105)

    self.lbl_run_time = Label(tab_dungeon, text=consts.LBL_RUN_TIME_EMPTY)
    self.lbl_run_time.place(x=145, y=135)

    lbl_class = Label(tab_dungeon, text=consts.LBL_CLASS, state=self.get_access(consts.DATA_MODE))
    lbl_class.place(x=10, y=73)

    self.val_char_class = ttk.Combobox(tab_dungeon, justify=consts.STATE_CENTER, values=consts.LIST_CLASS, state=consts.STATE_READONLY)
    self.val_char_class.current(self.get_data(consts.DATA_CLASS))
    self.val_char_class.config(width=5)
    self.val_char_class.place(x=75, y=73)

    lbl_mode = Label(tab_dungeon, text=consts.LBL_MODE, state=self.get_access(consts.DATA_MODE))
    lbl_mode.place(x=10, y=105)

    self.val_mode = IntVar(value=self.get_data(consts.DATA_MODE))
    chkbtn_mode = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_mode, state=self.get_access(consts.DATA_MODE))
    chkbtn_mode.place(x=75, y=106)

    lbl_buffs = Label(tab_dungeon, text=consts.LBL_BUFFS, state=self.get_access(consts.DATA_BUFFS))
    lbl_buffs.place(x=10, y=135)

    self.val_buffs = IntVar(value=self.get_data(consts.DATA_BUFFS))
    chkbtn_buffs = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_buffs, state=self.get_access(consts.DATA_BUFFS))
    chkbtn_buffs.place(x=75, y=136)

    self.val_cancel_buffs = IntVar(value=0)
    chkbtn_cancel_buffs = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_cancel_buffs, state=self.get_access(consts.DATA_BUFFS))
    chkbtn_cancel_buffs.place(x=95, y=136)

    lbl_shorts = Label(tab_dungeon, text=consts.LBL_SHORTS, state=self.get_access(consts.DATA_SHORTS))
    lbl_shorts.place(x=10, y=165)

    self.val_shorts = IntVar(value=self.get_data(consts.DATA_SHORTS))
    chkbtn_shorts = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_shorts, state=self.get_access(consts.DATA_SHORTS))
    chkbtn_shorts.place(x=75, y=166)

    self.val_hard_shorts = IntVar(value=self.get_data(consts.DATA_HARD_SHORTS))
    chkbtn_hard_shorts = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_hard_shorts, state=self.get_access(consts.DATA_HARD_SHORTS))
    chkbtn_hard_shorts.place(x=95, y=166)

    lbl_debuffs = Label(tab_dungeon, text=consts.LBL_DEBUFFS, state=self.get_access(consts.DATA_BUFFS))
    lbl_debuffs.place(x=10, y=195)

    self.val_debuffs = IntVar(value=self.get_data(consts.DATA_DEBUFFS))
    chkbtn_debuffs = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_debuffs, state=self.get_access(consts.DATA_DEBUFFS))
    chkbtn_debuffs.place(x=75, y=196)

    self.val_hard_debuffs = IntVar(value=self.get_data(consts.DATA_HARD_DEBUFFS))
    chkbtn_hard_debuffs = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_hard_debuffs, state=self.get_access(consts.DATA_HARD_DEBUFFS))
    chkbtn_hard_debuffs.place(x=95, y=196)

    lbl_leader = Label(tab_dungeon, text=consts.LBL_LEADER, state=self.get_access(consts.DATA_LEADER))
    lbl_leader.place(x=10, y=225)

    self.val_leader = IntVar(value=0)
    self.chkbtn_leader = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_leader, command=self.check_party_leader_state, state=self.get_access(consts.DATA_LEADER))
    self.chkbtn_leader.place(x=75, y=226)

    lbl_member = Label(tab_dungeon, text=consts.LBL_MEMBER, state=self.get_access(consts.DATA_MEMBER))
    lbl_member.place(x=10, y=255)

    self.val_member = IntVar(value=0)
    self.chkbtn_member = ttk.Checkbutton(tab_dungeon, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_member, command=self.check_party_member_state, state=self.get_access(consts.DATA_MEMBER))
    self.chkbtn_member.place(x=75, y=256)

    self.lbl_restart_note = Label(tab_dungeon, text=consts.LBL_RUN_RESTART_EMPTY)
    self.lbl_restart_note.place(x=145, y=165)

    lbl_license = Label(tab_dungeon, text=self.get_license())
    lbl_license.place(x=145, y=195)

    lbl_expiration = Label(tab_dungeon, text=self.get_expiration_status())
    lbl_expiration.place(x=145, y=225)

    self.lbl_macro = Label(tab_dungeon, text=consts.LBL_MACRO)
    self.lbl_macro.place(x=145, y=255)

    # Tab Connection
    lbl_run_restart = Label(tab_connection, text=consts.LBL_RUN_RESTART)
    lbl_run_restart.place(x=10, y=10)

    self.val_run_restart = ttk.Combobox(tab_connection, justify=consts.STATE_CENTER, values=self.LIST_RUN_RESTART)
    self.val_run_restart.current(0)
    self.val_run_restart.config(width=5)
    self.val_run_restart.place(x=92, y=10)

    lbl_run_restart_note = Label(tab_connection, text=consts.LBL_RUN_RESTART_NOTE)
    lbl_run_restart_note.place(x=155, y=10)

    lbl_dungeon_restart = Label(tab_connection, text=consts.LBL_DG_RESTART)
    lbl_dungeon_restart.place(x=10, y=43)

    self.val_dungeon_restart = IntVar(value=0)
    chkbtn_dungeon_restart = ttk.Checkbutton(tab_connection, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_dungeon_restart)
    chkbtn_dungeon_restart.place(x=90, y=43)

    lbl_dungeon_restart_note = Label(tab_connection, text=consts.LBL_DG_RESTART_NOTE)
    lbl_dungeon_restart_note.place(x=155, y=43)

    lbl_close_app = Label(tab_connection, text=consts.LBL_CLOSE_APP)
    lbl_close_app.place(x=10, y=73)

    self.val_close_app = IntVar(value=0)
    chkbtn_close_app = ttk.Checkbutton(tab_connection, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_close_app)
    chkbtn_close_app.place(x=90, y=74)

    lbl_close_app_note = Label(tab_connection, text=consts.LBL_CLOSE_APP_NOTE)
    lbl_close_app_note.place(x=155, y=73)

    lbl_pword = Label(tab_connection, text=consts.LBL_PWORD)
    lbl_pword.place(x=10, y=105)

    self.val_pword = StringVar()
    self.val_pword.set(self.get_data(consts.DATA_PWORD))
    entry_pword = Entry(tab_connection, show="*", textvariable=self.val_pword, width=15)
    entry_pword.place(x=85, y=105)

    lbl_pin = Label(tab_connection, text=consts.LBL_PIN)
    lbl_pin.place(x=205, y=105)

    self.val_pin = StringVar()
    self.val_pin.set(self.get_data(consts.DATA_PIN))
    entry_pin = Entry(tab_connection, show="*", textvariable=self.val_pin, width=10)
    entry_pin.place(x=240, y=105)

    lbl_resolution = Label(tab_connection, text=consts.LBL_RESOLUTION)
    lbl_resolution.place(x=10, y=135)

    self.val_resolution = ttk.Combobox(tab_connection, justify=consts.STATE_CENTER, values=self.LIST_RESOLUTION, state=consts.STATE_READONLY)
    self.val_resolution.current(self.get_data(consts.DATA_RESOLUTION))
    self.val_resolution.config(width=12)
    self.val_resolution.place(x=85, y=135)

    lbl_channel = Label(tab_connection, text=consts.LBL_CHANNEL)
    lbl_channel.place(x=205, y=135)

    self.val_channel = ttk.Combobox(tab_connection, justify=consts.STATE_CENTER, values=self.LIST_CHANNEL, state=consts.STATE_READONLY)
    self.val_channel.current(self.get_data(consts.DATA_CHANNEL))
    self.val_channel.config(width=7)
    self.val_channel.place(x=240, y=135)

    lbl_resolution_note = Label(tab_connection, text=consts.LBL_RESOLUTION_NOTE)
    lbl_resolution_note.place(x=10, y=165)

    lbl_load_time = Label(tab_connection, text=consts.LBL_LOAD_TIME)
    lbl_load_time.place(x=10, y=195)

    self.val_load_time = ttk.Combobox(tab_connection, justify=consts.STATE_CENTER, values=self.LIST_LOAD_TIME, state=consts.STATE_READONLY)
    self.val_load_time.current(self.get_data(consts.DATA_LOAD))
    self.val_load_time.config(width=12)
    self.val_load_time.place(x=85, y=195)

    lbl_load_time_note = Label(tab_connection, text=consts.LBL_LOAD_TIME_NOTE)
    lbl_load_time_note.place(x=10, y=225)

    lbl_cabal_note = Label(tab_connection, text=consts.LBL_CABAL_NOTE)
    lbl_cabal_note.place(x=10, y=255)

    # Tab Pet
    lbl_pet_note_1 = Label(tab_pet, text=consts.LBL_PET_NOTE_1)
    lbl_pet_note_1.place(x=10, y=10)

    lbl_pet_note_2 = Label(tab_pet, text=consts.LBL_PET_NOTE_2)
    lbl_pet_note_2.place(x=10, y=40)

    lbl_pet_note_3 = Label(tab_pet, text=consts.LBL_PET_NOTE_3)
    lbl_pet_note_3.place(x=10, y=70)

    lbl_x_coords = Label(tab_pet, text=consts.LBL_NPC_X)
    lbl_x_coords.place(x=10, y=103)

    self.val_x_coords = StringVar()
    self.val_x_coords.set(self.val_def_x)
    entry_x_coords = Entry(tab_pet, textvariable=self.val_x_coords, justify='center', width=5)
    entry_x_coords.place(x=62, y=105)

    lbl_y_coords = Label(tab_pet, text=consts.LBL_NPC_Y)
    lbl_y_coords.place(x=110, y=103)

    self.val_y_coords = StringVar()
    self.val_y_coords.set(self.val_def_y)
    entry_y_coords = Entry(tab_pet, textvariable=self.val_y_coords, justify='center', width=5)
    entry_y_coords.place(x=162, y=105)

    self.btn_test = Button(tab_pet, text=consts.BTN_TEST, command=self.pet_test)
    self.btn_test.config(width=5)
    self.btn_test.place(x=210, y=100)

    self.btn_train = Button(tab_pet, text=consts.BTN_TRAIN, command=self.pet_train)
    self.btn_train.config(width=6)
    self.btn_train.place(x=260, y=100)

    lbl_pet_note_4 = Label(tab_pet, text=consts.LBL_PET_NOTE_4)
    lbl_pet_note_4.place(x=10, y=135)

    lbl_mcr = Label(tab_pet, text=consts.LBL_MCR)
    lbl_mcr.place(x=10, y=165)

    self.val_mcr = IntVar(value=1)
    chkbtn_mcr = ttk.Checkbutton(tab_pet, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_mcr, state=util.NORMAL)
    chkbtn_mcr.place(x=45, y=166)

    lbl_crt = Label(tab_pet, text=consts.LBL_CRT)
    lbl_crt.place(x=70, y=165)

    self.val_crt = IntVar(value=0)
    chkbtn_crt = ttk.Checkbutton(tab_pet, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_crt, state=util.NORMAL)
    chkbtn_crt.place(x=105, y=166)

    lbl_cdi = Label(tab_pet, text=consts.LBL_CDI)
    lbl_cdi.place(x=130, y=165)

    self.val_cdi = IntVar(value=0)
    chkbtn_cdi = ttk.Checkbutton(tab_pet, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_cdi, state=util.NORMAL)
    chkbtn_cdi.place(x=165, y=166)

    lbl_crr = Label(tab_pet, text=consts.LBL_CRR)
    lbl_crr.place(x=190, y=165)

    self.val_crr = IntVar(value=0)
    chkbtn_crr = ttk.Checkbutton(tab_pet, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_crr, state=util.NORMAL)
    chkbtn_crr.place(x=225, y=166)

    lbl_eva = Label(tab_pet, text=consts.LBL_EVA)
    lbl_eva.place(x=250, y=165)

    self.val_eva = IntVar(value=0)
    chkbtn_eva = ttk.Checkbutton(tab_pet, text=consts.LBL_EMPTY, onvalue=1, offvalue=0, variable=self.val_eva, state=util.NORMAL)
    chkbtn_eva.place(x=285, y=166)

    lbl_pet_note_5 = Label(tab_pet, text=consts.LBL_PET_NOTE_5)
    lbl_pet_note_5.place(x=10, y=195)

    self.lbl_pet_action = Label(tab_pet, text=consts.LBL_STATUS_IDLE)
    self.lbl_pet_action.place(x=10, y=225)

    # Tab Misc
    lbl_store_note = Label(tab_misc, text=consts.LBL_STORE_NOTE)
    lbl_store_note.place(x=10, y=10)

    self.btn_fury = Button(tab_misc, text=consts.BTN_FURY, command=self.buy_fury)
    self.btn_fury.config(width=8)
    self.btn_fury.place(x=10, y=40)

    self.btn_upgrade = Button(tab_misc, text=consts.BTN_UPGRADE, command=self.buy_upgrade)
    self.btn_upgrade.config(width=8)
    self.btn_upgrade.place(x=85, y=40)

    self.btn_force = Button(tab_misc, text=consts.BTN_FORCE, command=self.buy_force)
    self.btn_force.config(width=8)
    self.btn_force.place(x=160, y=40)

    lbl_mail_note = Label(tab_misc, text=consts.LBL_MAIL_NOTE)
    lbl_mail_note.place(x=10, y=80)

    self.btn_mails = Button(tab_misc, text=consts.BTN_MAILS, command=self.get_mails)
    self.btn_mails.config(width=8)
    self.btn_mails.place(x=235, y=40)

    lbl_misc_x_coords = Label(tab_misc, text=consts.LBL_NPC_X)
    lbl_misc_x_coords.place(x=10, y=113)

    self.val_misc_x_coords = StringVar()
    self.val_misc_x_coords.set('1050')
    entry_x_coords = Entry(tab_misc, textvariable=self.val_misc_x_coords, justify='center', width=5)
    entry_x_coords.place(x=62, y=115)

    lbl_misc_y_coords = Label(tab_misc, text=consts.LBL_NPC_Y)
    lbl_misc_y_coords.place(x=110, y=113)

    self.val_misc_y_coords = StringVar()
    self.val_misc_y_coords.set('375')
    entry_y_coords = Entry(tab_misc, textvariable=self.val_misc_y_coords, justify='center', width=5)
    entry_y_coords.place(x=162, y=115)

    self.btn_misc_test = Button(tab_misc, text=consts.BTN_TEST, command=self.test_custom_clicks)
    self.btn_misc_test.config(width=5)
    self.btn_misc_test.place(x=10, y=150)

    self.btn_misc_click = Button(tab_misc, text=consts.BTN_CLICK, command=self.custom_clicks)
    self.btn_misc_click.config(width=6)
    self.btn_misc_click.place(x=60, y=150)

    self.btn_divide_one = Button(tab_misc, text=consts.BTN_DIVIDE_ONE, command=self.divide_one)
    self.btn_divide_one.config(width=9)
    self.btn_divide_one.place(x=118, y=150)

    self.btn_transfer = Button(tab_misc, text=consts.BTN_TRANSFER, command=self.transfer)
    self.btn_transfer.config(width=9)
    self.btn_transfer.place(x=198, y=150)

    lbl_misc_custom_note = Label(tab_misc, text=consts.LBL_CUSTON_CLICK_NOTE)
    lbl_misc_custom_note.place(x=10, y=190)

    lbl_misc_clicks = Label(tab_misc, text=consts.LBL_CLICKS)
    lbl_misc_clicks.place(x=10, y=220)

    self.val_click_count = ttk.Combobox(tab_misc, justify=consts.STATE_CENTER, values=self.LIST_CLICKS, state=consts.STATE_NORMAL)
    self.val_click_count.current(0)
    self.val_click_count.config(width=5)
    self.val_click_count.place(x=75, y=220)

    self.lbl_misc = Label(tab_misc, text=consts.LBL_CLICK)
    self.lbl_misc.place(x=160, y=220)

    self.btn_join_war = Button(tab_misc, text=consts.BTN_JOIN_WAR, state=self.get_access(consts.DATA_JOIN_WAR), command=self.join_war)
    self.btn_join_war.config(width=9)
    self.btn_join_war.place(x=10, y=250)

    self.btn_move_window = Button(tab_misc, text=consts.BTN_MOVE_WINDOW, command=self.move_app)
    self.btn_move_window.config(width=12)
    self.btn_move_window.place(x=90, y=250)

    # Tab Pricing
    frame_btn = Frame(tab_pricing)
    frame_btn.pack(anchor="w")

    scroll_features = Scrollbar(tab_pricing)
    scroll_features.pack(side=RIGHT, fill=Y)

    self.text_features = Text(tab_pricing, yscrollcommand=scroll_features.set)
    self.text_features.pack()
    self.get_features_free()

    btn_free = Button(frame_btn, text=consts.BTN_FREE, command=self.get_features_free)
    btn_free.pack(side=LEFT)

    btn_pro = Button(frame_btn, text=consts.BTN_PRO, command=self.get_features_pro)
    btn_pro.pack(side=LEFT)

    btn_premium = Button(frame_btn, text=consts.BTN_PREMIUM, command=self.get_features_premium)
    btn_premium.pack(side=LEFT)

    btn_changelogs = Button(frame_btn, text=consts.BTN_CHANGELOG, command=self.get_changelogs)
    btn_changelogs.pack(side=LEFT)

    self.enable_dungeon_features(None)
    self.frame_root.mainloop()

# GENERATE MAIN
JTool().initialize()
