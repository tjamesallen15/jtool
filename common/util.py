import math
import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

pynboard = Controller()

# GLOBAL VARIABLES
val_select = 'z'
val_dash = '1'
val_fade = '2'
val_attack = ['3', '4', '5']
val_veradrix  = '6'
val_loot = '7'
val_fury = '8'
val_pots = '9'
val_bm_aura = '0'
val_bm3_atk = '-'
val_bm3 = '='
val_interval_range = 0.3
val_interval_melee = 0.8
val_deselect = Key.esc
loot_space = Key.space

# GLOBAL VARIABLES
cabal_window = []
frame_root = []
lbl_current_run = []
lbl_macro = []
lbl_run_time = []

macro = True
is_battle_mode = False
trigger_reset_dungeon = False

battle_mode = 0
is_buffs_allowed = 1
is_short_buffs_allowed = 1
is_veradrix_allowed = 0
is_veradrix_needed = 0
aura_counter = 0
val_runs = 1
val_run_restart = 0
val_run_restart_stack = 0
val_pword = 'default'
val_pin = '123'
val_resolution = '0'
val_load_time = 0
val_default_interval = 0.3
val_time = 0
val_leader = 0
val_member = 0
val_char_class = 'BL'
val_access = 'Free'

region_normal_bar = []
region_mode_bar = []
region_screen = []
region_full_normal_bar = []
region_full_mode_bar = []
region_notification = []
region_dialog = []
region_sub_screen = []
region_train_screen = []

# CONSTANT UI VARIABLES
APP_FONT = "Tahoma 10"
APP_FRAME_SIZE = "330x280"
APP_NAME = "Cabal JTool"
APP_VERSION = "5.85"
APP_FULL_NAME = APP_NAME + " " + APP_VERSION
HOTKEY_TERMINATE = "ctrl+r"
HOTKEY_PAUSE = "ctrl+g"
LIST_CLASS = ["BL", "FB", "WA", "GL", "FS", "FA", "FG", "DM"]

# CONSTANT MESSAGES
MSG_START_DG = "Starting Dungeon"
MSG_END_DG = "End Dungeon"
MSG_EXIT = "Macro Exit"
MSG_PAUSE = "Pause for 15 seconds"
MSG_TERMINATE ="Macro Terminate"
MSG_PATH_FIND = "Pathfind, "
MSG_ATTACK_MOBS = "Attack, "
MSG_ATTACK_BOSS = "Boss Attack"
MSG_MOBS_FOUND = "Mobs Found, "
MSG_BOSS_FOUND = "Boss Found"
MSG_BOSS_KILLED = "Boss Killed"
MSG_NO_MOBS_FOUND = "No Mobs Found"
MSG_NO_BOSS_FOUND = "No Boss Found"
MSG_BLOCKER_FOUND = "Blocker Found"
MSG_NO_BLOCKER_FOUND = "No Blocker Found"
MSG_MOBS_CLEARED = "Mobs Cleared"
MSG_MOB_CLEARED = "Mob Cleared"
MSG_CHECK_BOSS = "Checking Boss"
MSG_CHECK_BOX = "Checking Box"
MSG_BOX_FOUND = "Box Found"
MSG_NO_BOX_FOUND = "No Box Found"
MSG_LOOTING_DROP = "Looting Drops"
MSG_PATH_STOP = "Pathing stop, attacking"
MSG_MOVE_STOP = "Moving stop, proceeding"
MSG_CHECK_END_DG = "Check End Dungeon"
MSG_NOTIFICATION_FOUND = "Notification Found"
MSG_NO_NOTIFICATION_FOUND = "No Notification Found"
MSG_ACTION = ""
MSG_RUN_NUMBER =  "Run #: "
MSG_CLICK = "Click #: "
MSG_BACKTRACK = "Backtrack #: "
MSG_CHALLENGE_DG = "Challenge Dungeon"
MSG_ENTER_DG = "Enter Dungeon"
MSG_BUTTON_FOUND = "Button Found"
MSG_NO_BUTTON_FOUND = "No Button Found"
MSG_BUFFS = "Buffing"
MSG_SHORT_BUFFS = "Buffing Shorts"
MSG_BATTLE_MODE = "Doing Mode II"
MSG_DICE_ROLL = "Check Dice Roll"
MSG_DICE_ROLL_OKAY = "Check Dice Roll Okay"
MSG_CHECK_DIALOG_FOUND =  "Check Dialog Found"
MSG_NO_CHECK_DIALOG_FOUND = "No Check Dialog Found"
MSG_GATE_FOUND = "Gate Found "
MSG_NO_GATE_FOUND = "No Gate Found"
MSG_WAIT = "Waiting"
MSG_MOVING_POSITION = "Moving to position"
MSG_ROLL_EQUIPMENT = "Rolling Equipment"
MSG_NO_ROLL_EQUIPMENT_FOUND = "No Roll Equipment Found"
MSG_CHECK_UMPRA_WEAK = "Checking Umpra The Weak"
MSG_UMPRA_WEAK_FOUND = "Umpra The Weak Found"
MSG_NO_UMPRA_WEAK_FOUND = "No Umpra The Weak Found"
MSG_CHECK_SIENA_BOX = "Checking Siena Box"
MSG_SIENA_BOX_FOUND = "Found Siena Box"
MSG_NO_SIENA_BOX_FOUND = "No Siena Box Found"
MSG_CHECKING_SUB_PASS = "Checking Sub Pass"
MSG_CABAL_WINDOW_FOUND = "Cabal Window Found"
MSG_NO_CABAL_WINDOW_FOUND = "No Cabal Window Found"
MSG_LAUNCHER_LOAD = "Launcher Loading"
MSG_NO_LAUNCHER_LOAD = "Fail Launcher Loading"
MSG_PLAY_BTN_FOUND = "Play Button Found"
MSG_NO_PLAY_BTN_FOUND = "No Play Button Found"
MSG_CHECK_BEAD_WINDOW = "Checking Bead Window"
MSG_BEAD_WINDOW_FOUND = "Bead Window Found"
MSG_NO_BEAD_WINDOW_FOUND = "No Bead Window Found"
MSG_SUB_PASS_FOUND = "Sub Password Found"
MSG_NO_SUB_PASS_FOUND = "No Sub Password Found"
MSG_COUNTDOWN = "Countdown, "
MSG_OPEN_APPLICATION = "Opening application"
MSG_CLOSE_APPLICATION = "Closing application"
MSG_TYPE_PASSWORD = "Typing password"
MSG_TYPE_PIN = "Typing pin"
MSG_CHECK_RECONNECT = "Check reconnecting status"
MSG_CLEARING_WINDOWS = "Clearing windows"
MSG_ENTER_WORLD = "Entering world"
MSG_MOVE_BEAD = "Moving bead window"
MSG_MOVE_APPLICATION = "Moving application window"
MSG_SELECT_TASK_BAR = "Selecting taskbar"
MSG_DUNGEON_RESTART = "Restarting before automation"
MSG_PET_SKILL_FOUND = "Pet Skill Found"
MSG_PET_SKILL_FOUND = "Pet Skill Not Found"

# CONSTANT IMAGES
IMG_APP_ICON = "img/icon.png"
IMG_ZERO = "img/0.jpg"
IMG_ONE = "img/1.jpg"
IMG_TWO = "img/2.jpg"
IMG_THREE = "img/3.jpg"
IMG_FOUR = "img/4.jpg"
IMG_FIVE = "img/5.jpg"
IMG_SIX = "img/6.jpg"
IMG_SEVEN = "img/7.jpg"
IMG_EIGHT = "img/8.jpg"
IMG_NINE = "img/9.jpg"
IMG_START_WINDOWS = "img/startwindows.jpg"
IMG_CABAL_WINDOW = "img/cabalwindow.jpg"
IMG_CHALLENGE_DG = "img/challengedg.jpg"
IMG_DUNGEON = "img/dungeon.jpg"
IMG_ENTER_DG = "img/enterdg.jpg"
IMG_END_DG = "img/enddg.jpg"
IMG_EXIT_DG = "img/exitdg.jpg"
IMG_LAUCHER_LOAD = "img/launcherloading.jpg"
IMG_LAUNCHER_PLAY = "img/launcherplay.jpg"
IMG_SUB_PASS = "img/subpass.jpg"
IMG_DUAL_BOSS = "img/dualboss.jpg"
IMG_BOSS = "img/boss.jpg"
IMG_SEMI_BOSS = "img/semiboss.jpg"
IMG_MOBS = "img/mobs.jpg"
IMG_DICE_ROLL = "img/rolladice.jpg"
IMG_DICE_OKAY = "img/diceokay.jpg"
IMG_DICE_EQUIP = "img/rollequip.jpg"
IMG_CHECK_NOTIF = "img/checknotif.jpg"
IMG_CLOSE_NOTIF = "img/closenotif.jpg"
IMG_CHECK_DIALOG = "img/checkdialog.jpg"
IMG_BOX = "img/box.jpg"
IMG_GATE = "img/gate.jpg"
IMG_HOLY_BOX = "img/holybox.jpg"
IMG_LAVA_GATE = "img/lava-gate.jpg"
IMG_FIRE_GUARD = "img/fire-guard.jpg"
IMG_GATEKEEPER = "img/gatekeeper.jpg"
IMG_SHOWORAI = "img/showorai.jpg"
IMG_OWLBEAR = "img/owlbear.jpg"
IMG_OWLBEAR_L = "img/owlbear-2.jpg"
IMG_VAOUR = "img/vaour.jpg"
IMG_VAOUR_L = "img/vaour-2.jpg"
IMG_HATCHLING = "img/hatchling.jpg"
IMG_HATCHLING_L = "img/hatchling-2.jpg"
IMG_AREIHORN = "img/areihorn.jpg"
IMG_PHIXIA = "img/phixia.jpg"
IMG_SIENA = "img/siena.jpg"
IMG_UMPRA_WEAK = "img/umpra-w.jpg"
IMG_MAX_CRIT_RATE = "img/max-crit-rate.jpg"
IMG_CRIT_RATE = "img/crit-rate.jpg"
IMG_CRIT_DAMAGE = "img/crit-dmg.jpg"
IMG_CRIT_RESIST = "img/resist-rate.jpg"
IMG_EVA = "img/evasion.jpg"
IMG_CHAOS_GATE = "img/chaosgate.jpg"

# FILE
FILE_CHANGELOG = "CHANGELOG.md"
FILE_READ = "r"

# CONSTANT UNITS
UNIT_BLANK = "--"
UNIT_BLOCKER = "Blocker"
UNIT_MUSH_FLOWER = "Mushed and Ectoflower"
UNIT_MOSS_TOAD = "Mossite and Toad"
UNIT_LUMBER_DORIGO = "Lumber and Dorigo"
UNIT_CUTTER_TOAD = "Moscutter and Toad"
UNIT_BOAR_SNAKE = "Boars and Snake"
UNIT_WHITE_SNAKE = "White Snake"
UNIT_ORPHIDIA = "Orphidia"
UNIT_MECHAPE = "Mechape"
UNIT_ARMUN = "Armun"
UNIT_TRICUS = "Tricus"
UNIT_GATE = "Gate"
UNIT_GATE_ONE = "Gate One"
UNIT_GATE_TWO = "Gate Two"
UNIT_GATE_THREE = "Gate Three"
UNIT_GATE_FOUR = "Gate Four"
UNIT_LEGRIN = "Legrin of Wind"
UNIT_LEO = "Leo of Wind"
UNIT_ESPI = "Espi of Wind"
UNIT_DRACO = "Draco of Wind"
UNIT_SPECTOR = "Spector"
UNIT_ICE_BLOCK = "Ice Block"
UNIT_FIRE_GUARD = "Fire Guard"
UNIT_GATEKEEPER_JASON = "Gatekeeper Jason"
UNIT_LAVA_GATE = "Lava Gate"
UNIT_MECH_LION = "Mech Lion"
UNIT_MECH_LIHONAR = "Mech Lihonar"
UNIT_ESPADA_1 = "Espada"
UNIT_ESPADA_2 = "Espada II"
UNIT_ESPADA_3 = "Espada III"
UNIT_POERTE = "Poerte"
UNIT_REDONNO = "Redonno"
UNIT_POWER_SUPPLY = "Power Supply"
UNIT_SHOWORAI_F = "Showorai [F]"
UNIT_SHOWORAI_R = "Showorai [R]"
UNIT_SHOWORAI_M = "Showorai [M]"
UNIT_GHOST = "Ghost"
UNIT_AREIHORN_GROUP = "Arehorn's Group"
UNIT_HUMMING_BIRD = "Hummingbird"
UNIT_HATCHLING = "Hatchling"
UNIT_PHIXIA = "Phixia"
UNIT_AREIHORN = "Areihorn"
UNIT_OWL_BEAR = "Owl Bear"
UNIT_VAOUR = "Vaour"
UNIT_KNIGHT = "Knight of Wind"
UNIT_SHIRDRAHN = "Shirdrahn"
UNIT_UMPRA_WEAK = "Umpra The Weak"
UNIT_SIENA_BOX = "Siena Box"
UNIT_BOX = "Box"
UNIT_ARENA_MOBS = "Arena Monsters"

# JSON DATA
DATA_JSON = "data/config.json"
DATA_DUNGEON = "dungeon"
DATA_RUNS = "runs"
DATA_MODE = "mode"
DATA_LEADER = "leader"
DATA_MEMBER = "member"
DATA_BUFFS = "buffs"
DATA_SHORTS = "shorts"
DATA_CLASS = "class"
DATA_VERADRIX = "veradrix"
DATA_PWORD = "pword"
DATA_PIN = "pin"
DATA_RESOLUTION = "resolution"
DATA_LOAD = "load"
DATA_CONNECTION = "connection"
DATA_PET = "pet"
DATA_OTHERS = "others"

# ACCESS LEVEL
ACCESS_FREE = "Free"
ACCESS_PRO = "Pro"
ACCESS_PREMIUM = "Premium"
ACCESS_TESTER = "Tester"
ACCESS_TESTER_II = "Tester II"
ACCESS_SUPER = "Super"

# STATES
STATE_SPACE = " "
STATE_EMPTY = ""
STATE_NA = "N/A"
STRING_HOUR = "h "
STRING_MIN = "m "
STRING_SEC = "s"
STATE_ONE = 1
STATE_ZERO = 0
STATE_DISABLED = "disabled"
STATE_NORMAL = "normal"
STATE_READONLY = "readonly"

# STATE LABEL
LBL_LICENSE = "License: "
LBL_EXPIRATION_NA = "Expiration: N/A"
LBL_EXPIRATION = "Expiration: "
LBL_OPEN_SECTION = " ("
LBL_CLOSE_SECTION = ")"
LBL_HYPHEN = " | "

# LABELS
BTN_START = "Start"
BTN_SOLO = "Solo"
BTN_MEMBER = "Member"
BTN_LEADER = "Leader"
BTN_TRAIN = "Train"
BTN_CLICK = "Click"
BTN_TEST = "Test"
LBL_EMPTY = ""
LBL_DUNGEON = "Dungeon: "
LBL_RUNS = "Runs: "
LBL_CLASS = "Class: "
LBL_MODE = "Mode II: "
LBL_BUFFS = "Buffs: "
LBL_SHORTS = "Shorts: "
LBL_LEADER = "Leader: "
LBL_MEMBER = "Member: "
LBL_VERADRIX = "Veradrix: "
LBL_CLICK = "Click #: N/A"
LBL_MACRO = "Idle"
LBL_CURRENT_RUN = "Run #: --"
LBL_RUN_TIME = "Run Time: "
LBL_RUN_TIME_EMPTY = "Run Time: --"
LBL_STATUS_TRAINING = "Status: Training"
LBL_STATUS_IDLE = "Status: Idle"
LBL_RESTART_NOTE_PREFIX = "Every "
LBL_RESTART_NOTE_SUFFIX = " runs"

LBL_RUN_RESTART = "Run Restart: "
LBL_RUN_RESTART_EMPTY = "Run Restart: --"
LBL_RUN_RESTART_NOTE = "Restart every run specified."
LBL_DG_RESTART = "DG Restart"
LBL_DG_RESTART_NOTE = "Restart first before auto."
LBL_PWORD = "Password: "
LBL_PIN = "PIN: "
LBL_RESOLUTION = "Resolution: "
LBL_RESOLUTION_NOTE = "Only listed resolution above are supported."
LBL_LOAD_TIME = "Load Time: "
LBL_LOAD_TIME_NOTE = "Adjust based on application load for login screen."
LBL_CABAL_NOTE = "Make sure Cabal World is available in start menu."

LBL_PET_NOTE_1 = "Inventory Tab must only have pet, kit and cores."
LBL_PET_NOTE_2 = "Pet in Slot 1, Kit in Slot 2 and rest cores."
LBL_PET_NOTE_3 = "Pet should have remove one skill before start."
LBL_PET_NOTE_4 = "NPC should be beside of player, camera zoomed in."
LBL_PET_NOTE_5 = "Auto train will check the skills marked above."

LBL_NPC_X = "NPC X: "
LBL_NPC_Y = "NPC Y: "
LBL_MCR = "MCR: "
LBL_CRT = "CRT: "
LBL_CDI = "CDI: "
LBL_CRR = "CRR: "
LBL_EVA = "EVA: "

LBL_STORE_NOTE = "Open NPC store first before clicking the buttons."
LBL_MAIL_NOTE = "Open first mail before clicking the button."
BTN_FURY = "Fury"
BTN_UPGRADE = "Upgrade"
BTN_FORCE = "Force"
BTN_MAILS = "Mails"
LBL_CUSTON_CLICK_NOTE = "Use custom x and y for other items in store."

LBL_CLICKS = "Clicks: "

BTN_FREE = "Free"
BTN_PRO = "Pro"
BTN_PREMIUM = "Premium"
BTN_CHANGELOG = "Changelog"

TAB_DUNGEON = "Dungeon"
TAB_CONNECTION = "Connection"
TAB_PET = "Pet"
TAB_OTHERS = "Others"
TAB_PRICING = "Pricing"

VAL_MELEE = 0
VAL_RANGE = 1
VAL_CLASS_FA = 'FA'
VAL_CLASS_FG = 'FG'
VAL_CLASS_DM = 'DM'
VAL_CLASS_BL = 'BL'

def initialize(window, frame, mlbl, rlbl, lrt):
  global macro
  macro = True

  global cabal_window
  cabal_window = window

  global frame_root
  frame_root = frame

  global lbl_macro
  lbl_macro = mlbl

  global lbl_current_run
  lbl_current_run = rlbl

  global lbl_run_time
  lbl_run_time = lrt

  global val_time
  val_time = time.time()

def set_variables(access_level, char_class=0, mode=0, leader=0, member=0, buff=1, sbuffs=1, vera=0, runs=1, run_restart=0, pword='default', pin='123', resolution='0', load_time=0):
  global val_access_level
  val_access_level = access_level

  global val_char_class
  val_char_class = char_class

  global battle_mode
  battle_mode = int(mode)

  global is_battle_mode
  is_battle_mode = False

  global val_leader
  val_leader = leader

  global val_member
  val_member = member

  global is_buffs_allowed
  is_buffs_allowed = int(buff)

  global is_short_buffs_allowed
  is_short_buffs_allowed = int(sbuffs)

  global is_veradrix_allowed
  is_veradrix_allowed = vera

  global val_runs
  val_runs = runs

  global val_run_restart
  val_run_restart = int(run_restart)

  global val_pword
  val_pword = pword

  global val_pin
  val_pin = pin

  global val_resolution
  val_resolution = resolution

  global val_load_time
  val_load_time = load_time

def initialize_region():
  global region_normal_bar
  region_normal_bar = (int(cabal_window[0] + 475), int(cabal_window[1] + 25), 45, 30)

  global region_mode_bar
  region_mode_bar = (int(cabal_window[0] + 350), int(cabal_window[1] + 25), 325, 30)

  global region_screen
  region_screen = (int(cabal_window[0]), int(cabal_window[1]) + 20, 1265, 720)

  global region_full_normal_bar
  region_full_normal_bar = (int(cabal_window[0] + 477), int(cabal_window[1] + 25), 283, 30)

  global region_full_mode_bar
  region_full_mode_bar = (int(cabal_window[0] + 354), int(cabal_window[1] + 25), 565, 30)

  global region_notification
  region_notification = (int(cabal_window[0]) + 1235, int(cabal_window[1]) + 270, 30, 400)

  global region_dialog
  region_dialog = (int(cabal_window[0]) + 5, int(cabal_window[1]) + 270, 30, 400)

  global region_sub_screen
  region_sub_screen = (int(cabal_window[0]) + 475, int(cabal_window[1] + 280), 300, 300)

  global region_train_screen
  region_train_screen = (int(cabal_window[0]) + 5, int(cabal_window[1]) + 280, 50, 55)

def set_cabal_window(window):
  global cabal_window
  cabal_window = window

def go_cabal_window():
  move_click(50, 15)

def move(x, y, sec=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)

  if sec != 0:
    time.sleep(sec)

def move_rel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)

  if sec != 0:
    time.sleep(sec)

def move_click(x, y, sec=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)
  pyauto.click(cabal_window[0] + x, cabal_window[1] + y)

  if sec != 0:
    time.sleep(sec)

def move_right_click(x, y, sec=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)
  pyauto.click(cabal_window[0] + x, cabal_window[1] + y, button="RIGHT")

  if sec != 0:
    time.sleep(sec)

  if sec != 0:
    time.sleep(sec)

def move_click_rel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)
  pyauto.click(ref[0] + x, ref[1] + y)

  if sec != 0:
    time.sleep(sec)

def move_scroll(x1, y1, x2, y2, sec=0):
  move(x1, y1)
  pyauto.mouseDown(button="right")

  move(x2, y2)
  pyauto.mouseUp(button="right")
  pyauto.scroll(-10000)

  if sec != 0:
    time.sleep(sec)

def wait(sec=1):
  log_action(MSG_WAIT)
  time.sleep(sec)

def log_run(run_number, fail_run_count=0):
  if fail_run_count == STATE_ZERO:
    run_builder = MSG_RUN_NUMBER + str(run_number) + LBL_HYPHEN + str(get_total_run_count())
  else:
    run_builder = MSG_RUN_NUMBER + str(run_number) + LBL_HYPHEN + str(get_total_run_count()) + LBL_OPEN_SECTION + str(fail_run_count) + LBL_CLOSE_SECTION

  lbl_current_run.config(text=run_builder)

  print(run_builder)
  frame_root.update()

def log_action(message):
  msg_builder = MSG_ACTION + message
  lbl_macro.config(text=msg_builder)

  print(msg_builder)
  frame_root.update()

def log_time(sec=1.5):
  check_time = time.time()
  sec_difference = math.ceil(check_time - val_time)
  min_difference = math.floor(sec_difference / 60)
  hour_difference = math.floor(min_difference / 60)
  time_difference = STATE_EMPTY

  if hour_difference > 0:
    time_difference += str(hour_difference) + STRING_HOUR

  if min_difference > 0:
    time_difference += str(min_difference - (hour_difference * 60)) + STRING_MIN

  time_difference += str(sec_difference - (min_difference * 60)) + STRING_SEC

  val_time_difference = LBL_RUN_TIME + time_difference
  lbl_run_time.config(text=val_time_difference)
  frame_root.update()

  if sec != 0:
    time.sleep(sec)

def terminate():
  log_action(MSG_EXIT)
  global macro
  macro = False

def pause():
  log_action(MSG_PAUSE)
  wait(15)

def countdown_timer(sec):
  for x in range(sec):
    log_action(MSG_COUNTDOWN + str(x+1))
    time.sleep(1)

def open_cabal_application():
  log_action(MSG_OPEN_APPLICATION)
  check_window = True
  while check_window:
    if check_window == False:
      break

    windows_start = pyauto.locateOnScreen(IMG_START_WINDOWS, grayscale=True, confidence=.8)
    pyauto.moveTo(windows_start[0] + 10, windows_start[1] + 15)
    pyauto.click(windows_start[0] + 10, windows_start[1] + 15)

    wait(1)
    pynboard.press("C")
    pynboard.release("C")
    time.sleep(0.1)
    pynboard.press("A")
    pynboard.release("A")
    time.sleep(0.1)
    pynboard.press("B")
    pynboard.release("B")
    time.sleep(0.1)
    pynboard.press("A")
    pynboard.release("A")
    time.sleep(0.1)
    pynboard.press("L")
    pynboard.release("L")
    time.sleep(0.1)
    pynboard.press(Key.space)
    pynboard.release(Key.space)
    time.sleep(0.1)
    pynboard.press("W")
    pynboard.release("W")
    time.sleep(0.1)
    pynboard.press("O")
    pynboard.release("O")
    time.sleep(0.1)

    wait(1)
    pynboard.press(Key.enter)
    pynboard.release(Key.enter)
    countdown_timer(10)

    try:
      launcher_loading = pyauto.locateOnScreen(IMG_LAUCHER_LOAD, grayscale=False, confidence=.9)
      log_action(MSG_NO_LAUNCHER_LOAD)
      pyauto.moveTo(launcher_loading[0] + 20, launcher_loading[1] + 15)
      continue
    except pyauto.ImageNotFoundException:
      log_action(MSG_LAUNCHER_LOAD)

    try:
      launcher_play = pyauto.locateOnScreen(IMG_LAUNCHER_PLAY, grayscale=False, confidence=.9)
      log_action(MSG_PLAY_BTN_FOUND)
      pyauto.moveTo(launcher_play[0] + 20, launcher_play[1] + 15)
      pyauto.click(launcher_play[0] + 20, launcher_play[1] + 15)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_PLAY_BTN_FOUND)
      continue

    try:
      countdown_timer(val_load_time)
      window = pyauto.locateOnScreen(IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
      log_action(MSG_CABAL_WINDOW_FOUND)
      set_cabal_window(window)
      initialize_region()
      check_window = False
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_CABAL_WINDOW_FOUND)

  countdown_timer(2)

def move_cabal_application():
  log_action(MSG_MOVE_APPLICATION)
  go_cabal_window()

  application = pyauto.getActiveWindow()

  if val_resolution == "2560x1440":
    application.moveTo(1260, 360)
  elif val_resolution == "1920x1080":
    application.moveTo(630, 150)

  window = pyauto.locateOnScreen(IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
  set_cabal_window(window)
  initialize_region()

  countdown_timer(2)

def type_pword():
  log_action(MSG_TYPE_PASSWORD)
  for x in val_pword:
    pynboard.press(x)
    pynboard.release(x)
    time.sleep(0.1)

def type_pin():
  log_action(MSG_TYPE_PIN)
  for x in val_pin:
    if x == "1":
      pin_number = pyauto.locateOnScreen(IMG_ONE, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "2":
      pin_number = pyauto.locateOnScreen(IMG_TWO, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "3":
      pin_number = pyauto.locateOnScreen(IMG_THREE, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "4":
      pin_number = pyauto.locateOnScreen(IMG_FOUR, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "5":
      pin_number = pyauto.locateOnScreen(IMG_FIVE, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "6":
      pin_number = pyauto.locateOnScreen(IMG_SIX, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "7":
      pin_number = pyauto.locateOnScreen(IMG_SEVEN, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "8":
      pin_number = pyauto.locateOnScreen(IMG_EIGHT, grayscale=False, confidence=.8, region=get_sub_screen_region())
    elif x == "9":
      pin_number = pyauto.locateOnScreen(IMG_NINE, grayscale=False, confidence=.8, region=get_sub_screen_region())
    else:
      pin_number = pyauto.locateOnScreen(IMG_ZERO, grayscale=False, confidence=.8, region=get_sub_screen_region())

    pyauto.moveTo(pin_number[0] + 10, pin_number[1] + 15)
    time.sleep(0.5)
    pyauto.click(pin_number[0] + 10, pin_number[1] + 15)
    time.sleep(0.5)

  move(580, 530)
  move_click(580, 530)

def enter_cabal_world():
  log_action(MSG_ENTER_WORLD)
  pynboard.press(Key.enter)
  pynboard.release(Key.enter)
  wait(5)

  pynboard.press(Key.right)
  pynboard.release(Key.right)
  time.sleep(0.1)

  pynboard.press(Key.down)
  pynboard.release(Key.down)
  time.sleep(0.1)
  pynboard.press(Key.down)
  pynboard.release(Key.down)
  time.sleep(0.1)

  pynboard.press(Key.enter)
  pynboard.release(Key.enter)
  time.sleep(5)

  try:
    pynboard.press(Key.enter)
    pynboard.release(Key.enter)
    countdown_timer(5)
    log_action(MSG_CHECKING_SUB_PASS)
    sub_pass = pyauto.locateOnScreen(IMG_SUB_PASS, grayscale=False, confidence=.8, region=get_sub_screen_region())
    log_action(MSG_SUB_PASS_FOUND)
    type_pin()
    wait(2)

    pynboard.press(Key.enter)
    pynboard.release(Key.enter)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_SUB_PASS_FOUND)

  wait(10)
  log_action(MSG_CLEARING_WINDOWS)
  pynboard.press(Key.esc)
  pynboard.release(Key.esc)

  pynboard.press(Key.esc)
  pynboard.release(Key.esc)

  pynboard.press(Key.esc)
  pynboard.release(Key.esc)
  wait(3)

def move_bead_window():
  try:
    log_action(MSG_MOVE_BEAD)
    bead_window = pyauto.locateOnScreen("img/bead.jpg", grayscale=False, confidence=.8, region=get_screen_region())
    pyauto.moveTo(bead_window[0] + 10, bead_window[1] + 10)

    pyauto.mouseDown(button="left")
    move(100, 700)
    pyauto.mouseUp(button="left")
    countdown_timer(2)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_BEAD_WINDOW_FOUND)

def select_task_bar():
  log_action(MSG_SELECT_TASK_BAR)
  coords = val_resolution.split('x')
  x = int(coords[0]) / 2
  y = int(coords[1]) - 20

  for i in range(3):
    pyauto.moveTo(x, y)
    pyauto.click(x, y)

def exit_cabal_application():
  log_action(MSG_CLOSE_APPLICATION)
  go_cabal_window()

  move(1260, 15)
  move_click(1260, 15)

  pynboard.press(Key.enter)
  pynboard.release(Key.enter)
  countdown_timer(5)

def check_run_restart(run_count):
  global val_run_restart_stack
  if val_run_restart > 0:
    log_action(MSG_CHECK_RECONNECT)
    if val_run_restart == (run_count - val_run_restart_stack):
      exit_cabal_application()
      select_task_bar()
      open_cabal_application()
      move_cabal_application()
      type_pword()
      enter_cabal_world()
      move_bead_window()
      val_run_restart_stack += run_count

def get_region():
  if is_battle_mode and get_attack_type() == STATE_ONE:
    return region_mode_bar
  else:
    return region_normal_bar

def get_full_region():
  if is_battle_mode and get_attack_type() == STATE_ONE:
    return region_full_mode_bar
  else:
    return region_full_normal_bar

def get_screen_region():
  return region_screen

def get_notification_region():
  return region_notification

def get_dialog_region():
  return region_dialog

def get_sub_screen_region():
  return region_sub_screen

def get_train_region():
  return region_train_screen

def get_access_level():
  return val_access_level

def get_char_class():
  return val_char_class

def get_attack_type():
  if get_char_class() == VAL_CLASS_FA or get_char_class() == VAL_CLASS_FG or get_char_class() == VAL_CLASS_DM:
    return VAL_RANGE

  return VAL_MELEE

def get_party_status():
  if get_party_leader_status() == STATE_ONE or get_party_member_status() == STATE_ONE:
    return True

  return False

def get_party_leader_status():
  return val_leader

def get_party_member_status():
  return val_member

def get_battle_mode():
  return battle_mode

def get_battle_mode_status():
  return is_battle_mode

def get_reset_status():
  return trigger_reset_dungeon

def set_reset_status(val=False):
  if val != False:
    reset_battle_mode(1.2)

  global trigger_reset_dungeon
  trigger_reset_dungeon = val

def get_macro_state():
  return macro

def get_total_run_count():
  return val_runs

def get_veradrix_status():
  return is_veradrix_allowed

def get_buffs_status():
  return is_buffs_allowed

def get_shorts_status():
  return is_short_buffs_allowed

def get_interval_melee():
  return val_interval_melee

def get_interval_range():
  return val_interval_range

def force_exit_dungeon():
  check_notifications()
  time.sleep(2)

  move_click(830, 710)
  time.sleep(0.5)

  move_click(850, 430)
  time.sleep(0.5)

  move_click(1030, 485)
  time.sleep(1)

  move_click(620, 440)
  time.sleep(3)

def go_skill_slot(sec=0):
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

  if sec != 0:
    time.sleep(sec)

def set_battle_mode(val, cancel=1):
  if cancel == STATE_ONE:
    cancel_aura(1.2)

  if get_battle_mode() == STATE_ONE:
    global is_battle_mode
    is_battle_mode = val

def reset_battle_mode(sec=0):
  cancel_aura(sec)

  if get_battle_mode() == STATE_ONE:
    global is_battle_mode
    is_battle_mode = False

def do_battle_mode(sec=5, cancel=1):
  if get_battle_mode() == STATE_ONE:
    log_action(MSG_BATTLE_MODE)
    set_battle_mode(True, cancel)

    move(790, 670)
    pyauto.click(button="right")

    move(790, 670)
    pyauto.click(button="right")

    for x in range(sec):
      do_essentials()
      time.sleep(1.2)

    pynboard.press(val_bm_aura)
    pynboard.release(val_bm_aura)
    time.sleep(1)

def do_veradrix():
  if get_veradrix_status() == STATE_ONE:
    pynboard.press(val_veradrix)
    pynboard.release(val_veradrix)

def do_cont_battle_mode():
  move(790, 670)
  pyauto.click(button="right")

  do_veradrix()
  global aura_counter
  aura_counter += 1
  if aura_counter > 45:
    do_aura()
    aura_counter = 0

def do_buffs():
  if get_buffs_status() == STATE_ONE:
    log_action(MSG_BUFFS)
    move(400, 670)
    pyauto.click(button="right")
    time.sleep(0.6)

    move(430, 670)
    pyauto.click(button="right")
    time.sleep(1)

def do_short_buffs():
  if get_shorts_status() == STATE_ONE:
    log_action(MSG_SHORT_BUFFS)
    move(470, 670)
    pyauto.click(button="right")
    time.sleep(0.2)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.2)

    if get_char_class() == VAL_CLASS_BL:
      move(540, 670)
      pyauto.click(button="right")
      time.sleep(0.5)

      move(570, 670)
      pyauto.click(button="right")
      time.sleep(0.5)

def force_short_buffs():
    log_action(MSG_SHORT_BUFFS)
    move(470, 670)
    pyauto.click(button="right")
    time.sleep(0.2)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.2)

    if get_char_class() == VAL_CLASS_BL:
      move(540, 670)
      pyauto.click(button="right")
      time.sleep(0.5)

      move(570, 670)
      pyauto.click(button="right")
      time.sleep(0.5)

def cancel_aura(sec=0):
  move(175, 100)
  pyauto.click(button="right")

  if sec != 0:
    time.sleep(sec)

def do_dash(sec=1.0):
  pynboard.press(val_dash)
  pynboard.release(val_dash)

  if sec != 0:
    time.sleep(sec)

def do_fade(sec=0.5):
  pynboard.press(val_fade)
  pynboard.release(val_fade)

  if sec != 0:
    time.sleep(sec)

def do_select(sec=0):
  pynboard.press(val_select)
  pynboard.release(val_select)

  if sec != 0:
    time.sleep(sec)

def do_deselect(sec=0):
  pynboard.press(val_deselect)
  pynboard.release(val_deselect)

  if sec != 0:
    time.sleep(sec)

def do_deselect_pack():
  do_deselect()
  do_deselect(0.1)
  do_deselect(0.1)

def plunder_box(select=1, reps=4, loot=1, sec=0.5):
  log_action(MSG_CHECK_BOX)

  if sec != 0:
    wait(sec)

  if select == STATE_ONE:
    do_select(0.1)

  checking = True
  while checking:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
      do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      log_action(MSG_NO_BOX_FOUND)

  if loot == STATE_ONE:
    do_plunder(reps)

def plunder_final_box(select=1, reps=5, loot=1):
  log_action(MSG_CHECK_BOX)
  wait(1)
  if select == STATE_ONE:
    do_select(0.1)

  checking = True
  while checking:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
      do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      log_action(MSG_NO_BOX_FOUND)

  if loot == STATE_ONE:
    do_plunder(reps)

def plunder_ref_box(select=1, reps=4, ref=IMG_BOX):
  log_action(MSG_CHECK_BOX)
  wait(1)
  if select == STATE_ONE:
    do_select(0.1)

  checking = True
  while checking:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(ref, grayscale=False, confidence=.8, region=get_full_region())
      log_action(MSG_BOX_FOUND)
      do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      log_action(MSG_NO_BOX_FOUND)

  do_plunder(reps)

def do_plunder(reps=4):
  for x in range(reps):
    log_action(MSG_LOOTING_DROP)
    pynboard.press(val_loot)
    pynboard.release(val_loot)
    time.sleep(0.3)
    pynboard.press(loot_space)
    pynboard.release(loot_space)
    time.sleep(0.3)

def do_fast_plunder():
    pynboard.press(val_loot)
    pynboard.release(val_loot)
    pynboard.press(loot_space)
    pynboard.release(loot_space)

def do_essentials():
  pynboard.press(loot_space)
  pynboard.release(loot_space)
  pynboard.press(val_fury)
  pynboard.release(val_fury)
  pynboard.press(val_pots)
  pynboard.release(val_pots)
  pynboard.press(val_loot)
  pynboard.release(val_loot)
  do_veradrix()

  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

def release_keys(sec=0):
  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

  if sec != 0:
    time.sleep(sec)

def do_aura(sec=0):
  pynboard.press(val_bm_aura)
  pynboard.release(val_bm_aura)

  if sec != 0:
    time.sleep(sec)

def do_final_mode(sec=0):
  if get_battle_mode_status() == False:
    pynboard.press(val_bm3)
    pynboard.release(val_bm3)

    if sec != 0:
      time.sleep(sec)

def do_attack(sec=0, strict=0, cont=1):
  do_veradrix()

  if get_battle_mode_status():
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    if strict == STATE_ZERO:
      do_essentials()

    if cont == STATE_ONE:
      do_cont_battle_mode()
  else:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(val_attack[0])
    pynboard.release(val_attack[0])

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(val_attack[1])
    pynboard.release(val_attack[1])

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(val_attack[2])
    pynboard.release(val_attack[2])

    if strict == STATE_ZERO:
      do_essentials()

  if sec != 0:
    time.sleep(sec)

def click_portal(x, y):
  portal_found = False

  move_click(x, y)
  try:
    mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
    log_action(MSG_BLOCKER_FOUND)
    focus_mobs(UNIT_BLOCKER, 0, 0, 0)
    wait(1)
    move_click(x, y, 1)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_BLOCKER_FOUND)

  try:
    enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
    portal_found = True
    log_action(MSG_BUTTON_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_BUTTON_FOUND)

  if portal_found == False:
    move_click(x, y)
    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BLOCKER_FOUND)
      focus_mobs(UNIT_BLOCKER, 0, 0, 0)
      wait(1)
      move_click(x, y, 1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BLOCKER_FOUND)

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      portal_found = True
      log_action(MSG_BUTTON_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BUTTON_FOUND)

  if portal_found == False:
    move_click(x, y)
    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BLOCKER_FOUND)
      focus_mobs(UNIT_BLOCKER, 0, 0, 0)
      wait(1)
      move_click(x, y, 1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BLOCKER_FOUND)

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      portal_found = True
      log_action(MSG_BUTTON_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BUTTON_FOUND)

def enter_dungeon(sec=1):
  entering = True
  while entering:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      entering = False

    if entering == False:
      break

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      log_action(MSG_BUTTON_FOUND)
      move_click_rel(15, 15, enterdg, 1)
      entering = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BUTTON_FOUND)

  wait(sec)

def challenge_dungeon(sec=0):
  challenging = True
  while challenging:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      challenging = False

    if challenging == False:
      break

    if get_party_member_status() == STATE_ZERO:
      try:
        challengedg = pyauto.locateOnScreen(IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
        log_action(MSG_BUTTON_FOUND)
        move_click_rel(15, 15, challengedg, 0.2)
        challenging = False
        break
      except pyauto.ImageNotFoundException:
        log_action(MSG_NO_BUTTON_FOUND)
    else:
      try:
        challengedg = pyauto.locateOnScreen(IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
        log_action(MSG_BUTTON_FOUND)
      except pyauto.ImageNotFoundException:
        log_action(MSG_NO_BUTTON_FOUND)
        challenging = False
        break

  if sec != 0:
    wait(sec)

def check_notifications():
  try:
    check_notify = pyauto.locateOnScreen(IMG_CHECK_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_NOTIFICATION_FOUND)

  time.sleep(0.2)

  try:
    check_notify = pyauto.locateOnScreen(IMG_CLOSE_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_NOTIFICATION_FOUND)

  time.sleep(0.2)

def end_dungeon():
  ending = True
  end_check_track = 0
  while ending:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      ending = False

    if ending == False:
      break

    end_check_track += 1
    if (end_check_track >= 100):
      ending = False
      break

    try:
      ending_dungeon = pyauto.locateOnScreen(IMG_END_DG, grayscale=False, confidence=.9)
      move_click_rel(50, 15, ending_dungeon, 0.2)
      ending = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_CHECK_END_DG)

def dice_dungeon():
  dicing = True
  while dicing:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      dicing = False

    if dicing == False:
        break

    try:
      dice_roll = pyauto.locateOnScreen(IMG_DICE_ROLL, grayscale=False, confidence=.9)
      move_click_rel(50, 15, dice_roll, 0.2)
      dicing = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_DICE_ROLL)

  confirming = True
  while confirming:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      confirming = False

    if confirming == False:
        break

    try:
      dice_confirm = pyauto.locateOnScreen(IMG_DICE_OKAY, grayscale=False, confidence=.9)
      move_click_rel(10, 5, dice_confirm, 0.2)
      confirming = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_DICE_ROLL_OKAY)

def focus_gate(unit=UNIT_BLANK, select=1):
  combo = True

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    try:
      gate = pyauto.locateOnScreen(IMG_GATE, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.3)
      do_attack(0.3)
    except pyauto.ImageNotFoundException:
      combo = False
      log_action(MSG_MOBS_CLEARED)
      break

def focus_mobs(unit=UNIT_BLANK, select=1, aura=1, sidestep=1):
  combo = True
  fade_count = 0

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    if sidestep == STATE_ONE:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_MOB_CLEARED)
      combo = False

def attack_backtrack(unit=UNIT_BLANK, aura=1, select=1, sidestep=1):
  combo = True
  fade_count = 0

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      sys.exit()

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    if sidestep == STATE_ONE:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    try:
      if select == STATE_ONE:
        do_select(0.1)
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.1)
      do_attack(0.1)

      if select == STATE_ONE:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_MOBS_FOUND)

    try:
      if select == STATE_ONE:
        do_select(0.1)
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
      plunder_box(select, 3)

      if select == STATE_ONE:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BOX_FOUND)
      combo = False
      break

def attack_mobs(unit=UNIT_BLANK, aura=1, interval=val_default_interval, sidestep=1):
  combo = True
  fade_count = 0

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    if sidestep == STATE_ONE:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    do_select(0.1)
    try:
      boss = pyauto.locateOnScreen(IMG_BOSS, grayscale=False, confidence=.9, region=get_region())
      do_deselect_pack()
      log_action(MSG_BOSS_FOUND)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_ATTACK_MOBS + unit)

    if combo == False:
      break

    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)
      do_attack(interval)
      do_attack(interval, 1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_MOBS_CLEARED)
      combo = False
      break

def focus_mob_boss(unit=UNIT_BLANK, select=1, aura=1, strict=0, cont=1):
  combo = True

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.1, strict, cont)
      do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      log_action(MSG_MOB_CLEARED)
      combo = False
      break

def attack_boss(select=1, aura=1, strict=0, cont=1):
  combo = True

  if get_battle_mode_status() and get_char_class() == VAL_CLASS_FA and select == STATE_ONE:
    do_select(0.1)
    do_select(0.1)
  elif select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    try:
      boss = pyauto.locateOnScreen(IMG_BOSS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_BOSS)
      do_attack(0.1, strict, cont)
      do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
      combo = False
      break

def attack_semi_boss(select=1, aura=1, strict=0, cont=1):
  combo = True

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if aura == STATE_ONE:
      do_final_mode()
      do_aura()

    try:
      boss = pyauto.locateOnScreen(IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_BOSS)
      do_attack(0.1, strict, cont)
      do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
      combo = False
      break
