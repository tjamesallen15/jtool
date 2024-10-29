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
KEY_SELECT = 'z'
KEY_DASH = '1'
KEY_FADE = '2'
KEY_ATTACK = ['3', '4', '5']
KEY_VERADRIX  = '6'
KEY_LOOT_ACTION = '7'
KEY_FURY = '8'
KEY_HP = '9'
KEY_AURA = '0'
KEY_BM_ATK = '-'
KEY_BM = '='
KEY_DESELECT = Key.esc
KEY_LOOT_SPACE = Key.space
KEY_BUFF_LONG_1 = '1'
KEY_BUFF_LONG_2 = '2'
KEY_BUFF_SHORT_1 = '3'
KEY_BUFF_SHORT_2 = '4'
KEY_BUFF_NORMAL_1 = '5'
KEY_BUFF_NORMAL_2 = '6'
KEY_DEBUFF_LIGHT = '7'
KEY_DEBUFF_HARD = '8'

# FIXED VARIABLES
val_interval_range = 0.3
val_interval_melee = 0.8

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
val_buffs = 1
val_cancel_buffs = 0
val_shorts = 1
val_hard_shorts = 0
val_debuffs = 0
val_hard_debuffs = 0
val_close_app = 0
val_vera = 0
aura_counter = 0
val_runs = 1
val_run_restart = 0
val_run_restart_stack = 0
val_pword = 'default'
val_pin = '123'
val_resolution = '0'
val_load_time = 0
val_channel = 4
val_default_interval = 0.3
val_time = 0
val_leader = 0
val_member = 0
val_char_class = 'BL'
val_access = 'Free'
val_last_message = ''
val_last_cast_mode = 0

region_normal_bar = []
region_mode_bar = []
region_screen = []
region_full_normal_bar = []
region_full_mode_bar = []
region_notification = []
region_buffs = []
region_middle = []
region_dialog = []
region_sub_screen = []
region_train_screen = []

# CONSTANT UI VARIABLES
APP_FONT = "Tahoma 10"
APP_FRAME_SIZE = "330x310"
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
MSG_PAUSE = "Pause for 15 delayonds"
MSG_TERMINATE ="Macro Terminate"
MSG_PATH_FIND = "Pathfind, "
MSG_ATTACK_MOBS = "Attack, "
MSG_ATTACK_BOSS = "Boss Attack"
MSG_MOBS_FOUND = "Mobs Found, "
MSG_BOSS_FOUND = "Boss Found"
MSG_BOSS_KILLED = "Boss Killed"
MSG_MOBS_NOT_FOUND = "Mobs Not Found"
MSG_BOSS_NOT_FOUND = "Boss Not Found"
MSG_BLOCKER_FOUND = "Blocker Found"
MSG_BLOCKER_NOT_FOUND = "Blocker Not Found"
MSG_MOBS_CLEARED = "Mobs Cleared"
MSG_MOB_CLEARED = "Mob Cleared"
MSG_CHECK_BOSS = "Checking Boss"
MSG_CHECK_BOX = "Checking Box"
MSG_BOX_FOUND = "Box Found"
MSG_BOX_NOT_FOUND = "Box Not Found"
MSG_LOOTING_DROP = "Looting Drops"
MSG_PATH_STOP = "Pathing stop, attacking"
MSG_MOVE_STOP = "Moving stop, proceeding"
MSG_CHECK_END_DG = "Check End Dungeon"
MSG_NOTIFICATION_FOUND = "Notification Found"
MSG_NOTIFICATION_NOT_FOUND = "Notification Not Found"
MSG_ACTION = ""
MSG_RUN_NUMBER =  "Run #: "
MSG_CLICK = "Click #: "
MSG_BACKTRACK = "Backtrack #: "
MSG_CHALLENGE_DG = "Challenge Dungeon"
MSG_ENTER_DG = "Enter Dungeon"
MSG_BUTTON_FOUND = "Button Found"
MSG_BUTTON_NOT_FOUND = "Button Not Found"
MSG_BUFFS = "Buffing"
MSG_SHORT_BUFFS = "Buffing Shorts"
MSG_DEBUFF = "Debuffing"
MSG_DEBUFF_HARD = "Hard Debuffing"
MSG_BATTLE_MODE = "Doing Mode II"
MSG_DICE_ROLL = "Check Dice Roll"
MSG_DICE_ROLL_OKAY = "Check Dice Roll Okay"
MSG_CHECK_DIALOG_FOUND =  "Check Dialog Found"
MSG_CHECK_DIALOG_NOT_FOUND = "Check Dialog Not Found"
MSG_GATE_FOUND = "Gate Found "
MSG_GATE_NOT_FOUND = "Gate Not Found"
MSG_WAIT = "Waiting"
MSG_MOVING_POSITION = "Moving to position"
MSG_ROLL_EQUIPMENT = "Rolling Equipment"
MSG_ROLL_EQUIPMENT_NOT_FOUND = "Roll Equipment Not Found"
MSG_CHECK_UMPRA_WEAK = "Checking Umpra The Weak"
MSG_UMPRA_WEAK_FOUND = "Umpra The Weak Found"
MSG_UMPRA_WEAK_NOT_FOUND = "Umpra The Weak Not Found"
MSG_CHECK_SIENA_BOX = "Checking Siena Box"
MSG_SIENA_BOX_FOUND = "Found Siena Box"
MSG_SIENA_BOX_NOT_FOUND = "Siena Box Not Found"
MSG_CHECKING_SUB_PASS = "Checking Sub Pass"
MSG_CABAL_WINDOW_FOUND = "Cabal Window Found"
MSG_CABAL_WINDOW_NOT_FOUND = "Cabal Window Not Found"
MSG_LAUNCHER_LOAD = "Launcher Loading"
MSG_LAUNCHER_LOAD_COMPLETE = "Launcher Complete"
MSG_LAUNCHER_LOAD_FAIL = "Launcher Fail"
MSG_PLAY_BTN_FOUND = "Play Button Found"
MSG_PLAY_BTN_NOT_FOUND = "Play Button Not Found"
MSG_CHECK_BEAD_WINDOW = "Checking Bead Window"
MSG_BEAD_WINDOW_FOUND = "Bead Window Found"
MSG_BEAD_WINDOW_NOT_FOUND = "Bead Window Not Found"
MSG_SUB_PASS_FOUND = "Sub Password Found"
MSG_SUB_PASS_NOT_FOUND = "Sub Password Not Found"
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
IMG_LOGIN = "img/login.jpg"
IMG_CHALLENGE_DG = "img/challengedg.jpg"
IMG_DUNGEON = "img/dungeon.jpg"
IMG_ENTER_DG = "img/enterdg.jpg"
IMG_END_DG = "img/enddg.jpg"
IMG_EXIT_DG = "img/exitdg.jpg"
IMG_LAUCHER_LOAD = "img/launcher-loading.jpg"
IMG_LAUCHER_COMPLETE = "img/launcher-complete.jpg"
IMG_LAUNCHER_PLAY = "img/launcher-play.jpg"
IMG_CHANNEL_ONE = "img/channel-one.jpg"
IMG_CHANNEL_TWO = "img/channel-two.jpg"
IMG_CHANNEL_THREE = "img/channel-three.jpg"
IMG_CHANNEL_FOUR = "img/channel-four.jpg"
IMG_SELECT_CHARACTER = "img/select-character.jpg"
IMG_TIMEOUT = "img/timeout.jpg"
IMG_TIMEOUT_EXIT = "img/timeout-exit.jpg"
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
IMG_BLOODY_SWEEPER = "img/bloody-sweeper.jpg"
IMG_BLOODY_FANG = "img/bloody-fang.jpg"
IMG_BEELZEBUB = "img/beelzebub.jpg"
IMG_ELECTULA = "img/electula.jpg"
IMG_QUEEN_RIPLEY = "img/queen-ripley.jpg"
IMG_ANT_HILL = "img/ant-hill.jpg"
IMG_BURNING_ANT_HILL = "img/burning-ant-hill.jpg"
IMG_FULL_ANT_HILL = "img/full-ant-hill.jpg"
IMG_WEB_GATE = "img/web-gate.jpg"

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

UNIT_WEB_GATE = "Web Gate"
UNIT_BLOODY_SWEEPER = "Bloody Sweeper"
UNIT_BLOODY_FANG = "Bloody Fang"
UNIT_BEELZEBUB = "Beelzebub"
UNIT_ELECTULA = "Electula"
UNIT_QUEEN_RIPLEY = "Queen Ripley"
UNIT_OMERAI = "Omerai"

UNIT_BLOODY_HORN = "Bloody Horn"
UNIT_KORAIDER = "Koraider"
UNIT_MUTANT_KORAIDER = "Mutang Koraider"
UNIT_ELECTRISHIA = "Electrishia"
UNIT_ANT_HILL = "Ant Hill"

# JSON DATA
DATA_JSON = "data/config.json"
DATA_DUNGEON = "dungeon"
DATA_RUNS = "runs"
DATA_MODE = "mode"
DATA_ACCESS_LEVEL = "access_level"
DATA_CHAR_CLASS = "char_class"
DATA_CHANNEL = "channel"
DATA_LEADER = "leader"
DATA_MEMBER = "member"
DATA_BUFFS = "buffs"
DATA_CANCEL_BUFFS = "cancel_buffs"
DATA_DEBUFFS = "debuffs"
DATA_HARD_DEBUFFS = "hard_debuffs"
DATA_SHORTS = "shorts"
DATA_HARD_SHORTS = "hard_shorts"
DATA_CLASS = "class"
DATA_VERADRIX = "veradrix"
DATA_RUN_RESTART = "run_restart"
DATA_CLOSE_APP = "close_app"
DATA_RUNS = "runs"
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
STATE_TWO = 2
STATE_THREE = 3
STATE_FOUR = 4
STATE_DISABLED = "disabled"
STATE_NORMAL = "normal"
STATE_READONLY = "readonly"
STATE_CENTER = "center"
IS_TRUE = True
IS_FALSE = False
CLICK_LEFT = "left"
CLICK_RIGHT = "right"

# STATE LABEL
LBL_LICENSE = "License: "
LBL_EXPIRATION_NA = "Expiration: N/A"
LBL_EXPIRATION = "Expiration: "
LBL_OPEN_delayTION = " ("
LBL_CLOSE_delayTION = ")"
LBL_HYPHEN = " | "

# LABELS
BTN_START = "Start"
BTN_SOLO = "Solo"
BTN_MEMBER = "Member"
BTN_LEADER = "Leader"
BTN_TRAIN = "Train"
BTN_CLICK = "Click"
BTN_DIVIDE_ONE = "Divide (1)"
BTN_TRANSFER = "Transfer"
BTN_JOIN_WAR = "Join War"
BTN_MOVE_WINDOW = "Move Window"
BTN_TEST = "Test"
LBL_EMPTY = ""
LBL_DUNGEON = "Dungeon: "
LBL_RUNS = "Runs: "
LBL_CLASS = "Class: "
LBL_MODE = "Mode II: "
LBL_BUFFS = "Buffs: "
LBL_DEBUFFS = "Debuffs: "
LBL_SHORTS = "Shorts: "
LBL_LEADER = "Leader: "
LBL_MEMBER = "Member: "
LBL_VERADRIX = "Veradrix: "
LBL_CLOSE_APP = "Exit Cabal: "
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
LBL_DG_RESTART = "DG Restart: "
LBL_DG_RESTART_NOTE = "Restart first before macro."
LBL_CLOSE_APP_NOTE = "Close Cabal after macro."
LBL_PWORD = "Password: "
LBL_PIN = "PIN: "
LBL_RESOLUTION = "Resolution: "
LBL_CHANNEL = "CH: "
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
VAL_CLASS_FB = 'FB'
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

  global val_last_message
  val_last_message = ''

def set_variables(args):
  set_access_level(args[DATA_ACCESS_LEVEL])
  set_char_class(args[DATA_CHAR_CLASS])
  set_initial_battle_mode(int(args[DATA_MODE]))
  set_battle_mode_status(False)
  set_party_leader_status(args[DATA_LEADER])
  set_party_member_status(args[DATA_MEMBER])
  set_buffs_status(args[DATA_BUFFS])
  set_cancel_buffs_status(args[DATA_CANCEL_BUFFS])
  set_debuffs_status(args[DATA_DEBUFFS])
  set_hard_debuffs_status(args[DATA_HARD_DEBUFFS])
  set_shorts_status(args[DATA_SHORTS])
  set_hard_shorts_status(args[DATA_HARD_SHORTS])
  set_veradrix_status(args[DATA_VERADRIX])
  set_total_run_count(args[DATA_RUNS])
  set_run_restart_status(args[DATA_RUN_RESTART])
  set_password(args[DATA_PWORD])
  set_pin(args[DATA_PIN])
  set_resolution(args[DATA_RESOLUTION])
  set_channel(args[DATA_CHANNEL])
  set_load_time(args[DATA_LOAD])
  set_close_app_status(args[DATA_CLOSE_APP])

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

  global region_buffs
  region_buffs = (int(cabal_window[0]) + 1236, int(cabal_window[1]) + 160, 32, 300)

  global region_middle
  region_middle = (int(cabal_window[0]) + 380, int(cabal_window[1]) + 20, 500, 600)

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

def press_combo(key_one, key_two):
  pynboard.press(key_one)
  time.sleep(0.01)
  pynboard.press(key_two)
  pynboard.release(key_two)
  pynboard.release(key_one)

def click_combo(x, y, right=False, delay=0):
  click = CLICK_LEFT if right == IS_FALSE else CLICK_RIGHT
  move(x, y)
  pyauto.click(button=click)

  if delay != 0: time.sleep(delay)

def click_press_combo(key_hold, key_one, right=False):
  click = CLICK_LEFT if right == IS_FALSE else CLICK_RIGHT

  pynboard.press(key_hold)
  time.sleep(0.15)

  pyauto.click(button=click)
  pynboard.release(key_hold)
  time.sleep(0.15)

  if key_one != STATE_EMPTY:
    press_release(key_one)
    time.sleep(0.15)

def press_release(key, delay=0):
  pynboard.press(key)
  pynboard.release(key)

  if delay != 0: time.sleep(delay)

def move(x, y, delay=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)

  if delay != 0: time.sleep(delay)

def move_rel(x, y, ref, delay=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)

  if delay != 0: time.sleep(delay)

def move_click(x, y, delay=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)
  pyauto.click(cabal_window[0] + x, cabal_window[1] + y)

  if delay != 0: time.sleep(delay)

def move_right_click(x, y, delay=0):
  pyauto.moveTo(cabal_window[0] + x, cabal_window[1] + y)
  pyauto.click(cabal_window[0] + x, cabal_window[1] + y, button="RIGHT")

  if delay != 0: time.sleep(delay)

def move_click_rel(x, y, ref, delay=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)
  pyauto.click(ref[0] + x, ref[1] + y)

  if delay != 0: time.sleep(delay)

def move_scroll(x1, y1, x2, y2, delay=0):
  move(x1, y1)
  pyauto.mouseDown(button="right")

  move(x2, y2)
  pyauto.mouseUp(button="right")
  pyauto.scroll(-10000)

  if delay != 0: time.sleep(delay)

def wait(delay=1):
  log_action(MSG_WAIT)
  time.sleep(delay)

def log_run(run_number, fail_run_count=0):
  if fail_run_count == STATE_ZERO:
    run_builder = MSG_RUN_NUMBER + str(run_number) + LBL_HYPHEN + str(get_total_run_count())
  else:
    run_builder = MSG_RUN_NUMBER + str(run_number) + LBL_HYPHEN + str(get_total_run_count()) + LBL_OPEN_delayTION + str(fail_run_count) + LBL_CLOSE_delayTION

  lbl_current_run.config(text=run_builder)

  print(run_builder)
  frame_root.update()

def log_action(message):
  msg_builder = MSG_ACTION + message

  global val_last_message
  if val_last_message != msg_builder:
    val_last_message = msg_builder
    print(msg_builder)

  lbl_macro.config(text=msg_builder)
  frame_root.update()

def log_time(delay=1.5):
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

  if delay != 0: time.sleep(delay)

def terminate():
  log_action(MSG_EXIT)
  global macro
  macro = False

def pause():
  log_action(MSG_PAUSE)
  wait(15)

def countdown_timer(delay):
  total_countdown = delay
  for x in range(delay):
    log_action(MSG_COUNTDOWN + str(total_countdown))
    total_countdown -= 1
    time.sleep(1)

def countdown_rel_timer(rel, conf, delay):
  total_countdown = delay
  for x in range(delay):
    log_action(MSG_COUNTDOWN + str(total_countdown))
    total_countdown -= 1
    time.sleep(1)

    try:
      window = pyauto.locateOnScreen(rel, grayscale=False, confidence=conf)
      break
    except pyauto.ImageNotFoundException:
      pass

def open_app():
  log_action(MSG_OPEN_APPLICATION)
  check_window = True
  keyword = "CABAL W"
  while check_window:
    if check_window == False:
      break

    windows_start = pyauto.locateOnScreen(IMG_START_WINDOWS, grayscale=True, confidence=.8)
    move_click_rel(10, 15, windows_start, 1)

    for key in keyword: press_release(key, 0.1)
    wait(1)
    press_release(Key.enter)
    countdown_timer(10)

    try:
      launch_load = pyauto.locateOnScreen(IMG_LAUCHER_LOAD, grayscale=False, confidence=.9)
      log_action(MSG_LAUNCHER_LOAD_FAIL)
      continue
    except pyauto.ImageNotFoundException:
      log_action(MSG_LAUNCHER_LOAD)

    try:
      launch_complete = pyauto.locateOnScreen(IMG_LAUCHER_COMPLETE, grayscale=False, confidence=.7)
      log_action(MSG_LAUNCHER_LOAD_COMPLETE)
    except pyauto.ImageNotFoundException:
      log_action(MSG_LAUNCHER_LOAD_FAIL)
      continue

    try:
      launch_play = pyauto.locateOnScreen(IMG_LAUNCHER_PLAY, grayscale=False, confidence=.9)
      log_action(MSG_PLAY_BTN_FOUND)
      move_click_rel(20, 15, launch_play)
    except pyauto.ImageNotFoundException:
      log_action(MSG_PLAY_BTN_NOT_FOUND)
      continue

    try:
      countdown_rel_timer(IMG_LOGIN, 0.8, get_load_time())
      window = pyauto.locateOnScreen(IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
      log_action(MSG_CABAL_WINDOW_FOUND)
      set_cabal_window(window)
      initialize_region()
      check_window = False
    except pyauto.ImageNotFoundException:
      log_action(MSG_CABAL_WINDOW_NOT_FOUND)

  countdown_timer(2)

def move_app():
  log_action(MSG_MOVE_APPLICATION)

  go_cabal_window()
  application = pyauto.getActiveWindow()
  if val_resolution == "2560x1440":
    application.moveTo(1260, 360)
  elif val_resolution == "1920x1080":
    application.moveTo(620, 150)

  window = pyauto.locateOnScreen(IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
  set_cabal_window(window)
  initialize_region()

  countdown_timer(2)

def type_password():
  log_action(MSG_TYPE_PASSWORD)
  for key in val_pword: press_release(key, 0.1)

def type_pin():
  log_action(MSG_TYPE_PIN)
  for key in val_pin:
    match key:
      case "1": pin_number = pyauto.locateOnScreen(IMG_ONE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "2": pin_number = pyauto.locateOnScreen(IMG_TWO, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "3": pin_number = pyauto.locateOnScreen(IMG_THREE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "4": pin_number = pyauto.locateOnScreen(IMG_FOUR, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "5": pin_number = pyauto.locateOnScreen(IMG_FIVE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "6": pin_number = pyauto.locateOnScreen(IMG_SIX, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "7": pin_number = pyauto.locateOnScreen(IMG_SEVEN, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "8": pin_number = pyauto.locateOnScreen(IMG_EIGHT, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "9": pin_number = pyauto.locateOnScreen(IMG_NINE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "0": pin_number = pyauto.locateOnScreen(IMG_ZERO, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case _: pin_number = pyauto.locateOnScreen(IMG_ZERO, grayscale=False, confidence=.8, region=get_sub_screen_region())

    move_rel(10, 15, pin_number, 0.2)
    move_click_rel(10, 15, pin_number, 0.2)

  move(580, 530)
  move_click(580, 530, 2)

def enter_world():
  log_action(MSG_ENTER_WORLD)
  press_release(Key.enter, 8)
  press_release(Key.right, 0.5)

  img_channel = IMG_CHANNEL_FOUR
  if get_channel() == STATE_ONE: img_channel = IMG_CHANNEL_ONE
  elif get_channel() == STATE_TWO: img_channel = IMG_CHANNEL_TWO
  elif get_channel() == STATE_THREE: img_channel = IMG_CHANNEL_THREE
  elif get_channel() == STATE_FOUR: img_channel = IMG_CHANNEL_FOUR

  try:
    channel = pyauto.locateOnScreen(img_channel, grayscale=False, confidence=.9, region=get_middle_region())
    move_click_rel(10, 10, channel, 0.2)
    press_release(Key.enter, 8)
  except pyauto.ImageNotFoundException:
    press_release(Key.down, 0.1)
    press_release(Key.down, 0.1)
    press_release(Key.enter, 10)

  check_pass = True
  check_count = 0
  log_action(MSG_CHECKING_SUB_PASS)
  while check_pass:
    if check_count >= 3:
      check_pass = False

    if check_pass == False:
      break

    try:
      press_release(Key.enter, 0.4)
      sub_pass = pyauto.locateOnScreen(IMG_SUB_PASS, grayscale=False, confidence=.8, region=get_sub_screen_region())
      log_action(MSG_SUB_PASS_FOUND)
      check_count += 3
      check_pass = False
      type_pin()
      press_release(Key.enter, 0.4)
      break
    except pyauto.ImageNotFoundException:
      check_count += 1
      log_action(MSG_SUB_PASS_NOT_FOUND)

  countdown_timer(10)
  log_action(MSG_CLEARING_WINDOWS)
  for x in range(3): press_release(Key.esc)

def move_bead_window():
  try:
    log_action(MSG_MOVE_BEAD)
    bead_window = pyauto.locateOnScreen("img/bead.jpg", grayscale=False, confidence=.8, region=get_screen_region())
    move_rel(10, 10, bead_window)
    pyauto.mouseDown(button="left")
    move(100, 700)
    pyauto.mouseUp(button="left")
    countdown_timer(2)
  except pyauto.ImageNotFoundException:
    log_action(MSG_BEAD_WINDOW_NOT_FOUND)

def select_task_bar():
  log_action(MSG_SELECT_TASK_BAR)
  coords = val_resolution.split('x')
  x = int(coords[0]) / 2
  y = int(coords[1]) - 20

  for i in range(3):
    pyauto.moveTo(x, y)
    pyauto.click(x, y)

def exit_app(finish=False):
  log_action(MSG_CLOSE_APPLICATION)
  go_cabal_window()
  move(1260, 15)
  move_click(1260, 15)
  press_release(Key.enter)

  if finish == IS_FALSE: countdown_timer(5)

def check_run_restart(run_count):
  global val_run_restart_stack
  if get_run_restart_status() > 0:
    log_action(MSG_CHECK_RECONNECT)
    if get_run_restart_status() == (run_count - val_run_restart_stack):
      restart_application()
      val_run_restart_stack += run_count

def restart_application():
  exit_app()
  select_task_bar()
  open_app()
  move_app()
  type_password()
  enter_world()

def get_archer_region():
  return region_full_mode_bar

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

def get_buff_region():
  return region_buffs

def get_middle_region():
  return region_middle

def get_dialog_region():
  return region_dialog

def get_sub_screen_region():
  return region_sub_screen

def get_train_region():
  return region_train_screen

def set_access_level(access_level):
  global val_access_level
  val_access_level = access_level

def get_access_level():
  return val_access_level

def set_char_class(char_class):
  global val_char_class
  val_char_class = char_class

def get_char_class():
  return val_char_class

def get_attack_type():
  if get_char_class() == VAL_CLASS_FA or get_char_class() == VAL_CLASS_FG or get_char_class() == VAL_CLASS_DM:
    return VAL_RANGE

  return VAL_MELEE

def set_last_cast_mode(mode):
  global val_last_cast_mode
  val_last_cast_mode = mode

def get_last_cast_mode():
  global val_last_cast_mode
  return val_last_cast_mode

def get_party_status():
  if get_party_leader_status() == STATE_ONE or get_party_member_status() == STATE_ONE:
    return True

  return False

def set_party_leader_status(leader):
  global val_leader
  val_leader = leader

def get_party_leader_status():
  return val_leader

def set_party_member_status(member):
  global val_member
  val_member = member

def get_party_member_status():
  return val_member

def set_initial_battle_mode(mode):
  global battle_mode
  battle_mode = mode

def get_battle_mode():
  return battle_mode

def set_battle_mode_status(status):
  global is_battle_mode
  is_battle_mode = status

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

def set_total_run_count(runs):
  global val_runs
  val_runs = runs

def get_total_run_count():
  return val_runs

def set_veradrix_status(status):
  global val_vera
  val_vera = status

def get_veradrix_status():
  return val_vera

def set_buffs_status(status):
  global val_buffs
  val_buffs = status

def get_buffs_status():
  return val_buffs

def set_debuffs_status(status):
  global val_debuffs
  val_debuffs = status

def get_debuffs_status():
  return val_debuffs

def set_hard_debuffs_status(status):
  global val_hard_debuffs
  val_hard_debuffs = status

def get_hard_debuffs_status():
  return val_hard_debuffs

def set_cancel_buffs_status(status):
  global val_cancel_buffs
  val_cancel_buffs = status

def get_cancel_buffs_status():
  return val_cancel_buffs

def set_shorts_status(status):
  global val_shorts
  val_shorts = status

def get_shorts_status():
  return val_shorts

def set_hard_shorts_status(status):
  global val_hard_shorts
  val_hard_shorts = status

def get_hard_shorts_status():
  return val_hard_shorts

def get_interval_melee():
  return val_interval_melee

def get_interval_range():
  return val_interval_range

def set_run_restart_status(status):
  global val_run_restart
  val_run_restart = int(status)

def get_run_restart_status():
  return val_run_restart

def set_password(pword):
  global val_pword
  val_pword = pword

def get_password():
  return val_pword

def set_pin(pin):
  global val_pin
  val_pin = pin

def get_pin():
  return val_pin

def set_resolution(resolution):
  global val_resolution
  val_resolution = resolution

def get_resolution():
  return val_resolution

def set_channel(channel):
  global val_channel
  val_channel = channel

def get_channel():
  return val_channel

def set_load_time(load_time):
  global val_load_time
  val_load_time = load_time

def get_load_time():
  return val_load_time

def set_close_app_status(status):
  global val_close_app
  val_close_app = status

def get_close_app_status():
  return val_close_app

def do_close_app_status():
  if get_close_app_status() == STATE_ONE:
    exit_app(True)

def force_exit_dungeon():
  check_notifications()
  time.sleep(0.2)

  move_click(830, 710)
  time.sleep(0.2)

  move_click(850, 430)
  time.sleep(0.2)

  move_click(1030, 485)
  time.sleep(0.2)

  move_click(620, 440)
  time.sleep(3)

def timeout_exit_dungeon():
  try:
    timeout = pyauto.locateOnScreen(IMG_TIMEOUT, grayscale=False, confidence=.7, region=get_middle_region())
    timeout_exit = pyauto.locateOnScreen(IMG_TIMEOUT_EXIT, grayscale=False, confidence=.9, region=get_middle_region())
    move_click_rel(10, 10, timeout_exit, 0.2)
  except pyauto.ImageNotFoundException:
    pass

  time.sleep(3)

def go_skill_slot(delay=0):
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

  if delay != 0: time.sleep(delay)

def set_battle_mode(val, cancel=True):
  if cancel == IS_TRUE: cancel_aura(1.2)

  if get_battle_mode() == STATE_ONE:
    global is_battle_mode
    is_battle_mode = val

def reset_battle_mode(delay=0):
  cancel_aura(delay)

  if get_battle_mode() == STATE_ONE:
    global is_battle_mode
    is_battle_mode = False

def do_battle_mode(delay=5, cancel=True, aura=True):
  if get_battle_mode() == STATE_ONE:
    log_action(MSG_BATTLE_MODE)
    set_battle_mode(True, cancel)

    click_combo(790, 670, True)
    click_combo(790, 670, True)

    for x in range(delay):
      do_essentials()
      time.sleep(1)

    if aura == IS_TRUE:
      pynboard.press(KEY_AURA)
      pynboard.release(KEY_AURA)
      time.sleep(1)

def force_battle_mode(delay=5):
  click_combo(790, 670, True)
  click_combo(790, 670, True)

  if get_char_class() == VAL_CLASS_FB:
    delay = 4

  for x in range(delay):
    do_essentials()
    time.sleep(1)

def do_cont_battle_mode():
  move(790, 670)
  pyauto.click(button="right")

  do_veradrix()
  global aura_counter
  aura_counter += 1
  if aura_counter > 45:
    do_aura()
    aura_counter = 0

def check_battle_mode():
  if get_last_cast_mode() == STATE_TWO:
    press_combo(Key.alt, KEY_BM)
  elif get_last_cast_mode() == STATE_THREE:
    do_final_mode()

def do_veradrix():
  if get_veradrix_status() == STATE_ONE: press_release(KEY_VERADRIX)

def force_veradrix():
  press_release(KEY_VERADRIX)

def do_buffs():
  if get_buffs_status() == STATE_ONE:
    log_action(MSG_BUFFS)
    click_combo(400, 670, True, 0.6)
    click_combo(430, 670, True, 1)

def cancel_buffs(reps=8):
  if get_cancel_buffs_status() == STATE_ONE:
    for x in range(reps):
      move(1250, 185)
      pyauto.click(button="right")
      time.sleep(0.2)

def do_short_buffs():
  if get_shorts_status() == STATE_ONE:
    log_action(MSG_SHORT_BUFFS)
    click_combo(470, 670, True, 0.2)
    click_combo(500, 670, True, 0.2)

    do_hard_short_buffs()

def do_hard_short_buffs():
  if get_hard_shorts_status() == STATE_ONE:
    if get_char_class() == VAL_CLASS_BL:
      click_combo(540, 670, True, 0.5)
      click_combo(570, 670, True, 0.5)

def force_short_buffs():
  log_action(MSG_SHORT_BUFFS)
  click_combo(470, 670, True, 0.2)
  click_combo(500, 670, True, 0.2)

  if get_char_class() == VAL_CLASS_BL:
    click_combo(540, 670, True, 0.5)
    click_combo(570, 670, True, 0.5)

def do_debuff(delay=1.5):
  if get_debuffs_status() == STATE_ONE:
    log_action(MSG_DEBUFF)
    click_combo(610, 670, True, delay)

def do_hard_debuff(delay=1.5):
  if get_hard_debuffs_status() == STATE_ONE:
    log_action(MSG_DEBUFF_HARD)
    click_combo(650, 670, True, delay)

def cancel_aura(delay=0):
  click_combo(175, 100, True)

  if delay != 0: time.sleep(delay)

def do_dash(delay=1.0):
  pynboard.press(KEY_DASH)
  pynboard.release(KEY_DASH)

  if delay != 0: time.sleep(delay)

def do_fade(delay=0.5):
  pynboard.press(KEY_FADE)
  pynboard.release(KEY_FADE)

  if delay != 0: time.sleep(delay)

def do_select(delay=0):
  pynboard.press(KEY_SELECT)
  pynboard.release(KEY_SELECT)

  if delay != 0: time.sleep(delay)

def do_deselect(delay=0):
  pynboard.press(KEY_DESELECT)
  pynboard.release(KEY_DESELECT)

  if delay != 0: time.sleep(delay)

def do_deselect_pack():
  do_deselect()
  do_deselect(0.1)
  do_deselect(0.1)

def roll_box():
  if get_party_status() == STATE_ONE:
    try:
      roll = pyauto.locateOnScreen(IMG_DICE_EQUIP, grayscale=False, confidence=.9, region=get_screen_region())
      log_action(MSG_ROLL_EQUIPMENT)
      move_rel(10, 10, roll, 0.2)
      move_click_rel(10, 10, roll, 0.2)
    except pyauto.ImageNotFoundException:
      log_action(MSG_ROLL_EQUIPMENT_NOT_FOUND)

def party_roll_box(reps=4):
  roll_reps = reps * 3
  for x in range(roll_reps):
    roll_box()
    if get_veradrix_status() == STATE_ONE: do_veradrix()
    time.sleep(0.3)

def plunder_box(select=1, reps=4, loot=1, delay=0.5):
  log_action(MSG_CHECK_BOX)

  if delay != 0:
    wait(delay)

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
      log_action(MSG_BOX_NOT_FOUND)

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
      log_action(MSG_BOX_NOT_FOUND)

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
      log_action(MSG_BOX_NOT_FOUND)

  do_plunder(reps)

def do_plunder(reps=4):
  for x in range(reps):
    log_action(MSG_LOOTING_DROP)
    pynboard.press(KEY_LOOT_ACTION)
    pynboard.release(KEY_LOOT_ACTION)
    time.sleep(0.3)
    pynboard.press(KEY_LOOT_SPACE)
    pynboard.release(KEY_LOOT_SPACE)
    time.sleep(0.3)
    roll_box()

def do_fast_plunder():
    pynboard.press(KEY_LOOT_ACTION)
    pynboard.release(KEY_LOOT_ACTION)
    pynboard.press(KEY_LOOT_SPACE)
    pynboard.release(KEY_LOOT_SPACE)

def do_essentials(rel_keys=1):
  pynboard.press(KEY_LOOT_SPACE)
  pynboard.release(KEY_LOOT_SPACE)
  pynboard.press(KEY_FURY)
  pynboard.release(KEY_FURY)
  pynboard.press(KEY_HP)
  pynboard.release(KEY_HP)
  pynboard.press(KEY_LOOT_ACTION)
  pynboard.release(KEY_LOOT_ACTION)
  do_veradrix()

  if rel_keys == 1:
    pynboard.release(Key.shift)
    pynboard.release(Key.alt)
    pynboard.release(Key.ctrl)

def release_keys(delay=0):
  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

  if delay != 0: time.sleep(delay)

def do_aura(delay=0):
  pynboard.press(KEY_AURA)
  pynboard.release(KEY_AURA)

  if delay != 0: time.sleep(delay)

def do_final_mode(delay=0):
  if get_battle_mode_status() == False:
    pynboard.press(KEY_BM)
    pynboard.release(KEY_BM)

    if delay != 0: time.sleep(delay)

def do_attack(delay=0, strict=0, cont=1):
  do_veradrix()

  if get_battle_mode_status():
    pynboard.press(KEY_BM_ATK)
    pynboard.release(KEY_BM_ATK)
    if strict == STATE_ZERO:
      do_essentials()

    if cont == STATE_ONE:
      do_cont_battle_mode()
  else:
    pynboard.press(KEY_BM_ATK)
    pynboard.release(KEY_BM_ATK)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(KEY_BM_ATK)
    pynboard.release(KEY_BM_ATK)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(KEY_BM_ATK)
    pynboard.release(KEY_BM_ATK)

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(KEY_ATTACK[0])
    pynboard.release(KEY_ATTACK[0])

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(KEY_ATTACK[1])
    pynboard.release(KEY_ATTACK[1])

    if strict == STATE_ZERO:
      do_essentials()

    pynboard.press(KEY_ATTACK[2])
    pynboard.release(KEY_ATTACK[2])

    if strict == STATE_ZERO:
      do_essentials()

  if delay != 0: time.sleep(delay)

def do_special_attack(delay=0.1):
  pynboard.press(KEY_BM_ATK)
  pynboard.release(KEY_BM_ATK)

  force_veradrix()
  do_essentials()
  check_battle_mode()

  if delay != 0: time.sleep(delay)

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
    log_action(MSG_BLOCKER_NOT_FOUND)

  try:
    enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
    portal_found = True
    log_action(MSG_BUTTON_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_BUTTON_NOT_FOUND)

  if portal_found == False:
    move_click(x, y)
    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BLOCKER_FOUND)
      focus_mobs(UNIT_BLOCKER, 0, 0, 0)
      wait(1)
      move_click(x, y, 1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BLOCKER_NOT_FOUND)

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      portal_found = True
      log_action(MSG_BUTTON_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BUTTON_NOT_FOUND)

  if portal_found == False:
    move_click(x, y)
    try:
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BLOCKER_FOUND)
      focus_mobs(UNIT_BLOCKER, 0, 0, 0)
      wait(1)
      move_click(x, y, 1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BLOCKER_NOT_FOUND)

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      portal_found = True
      log_action(MSG_BUTTON_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BUTTON_NOT_FOUND)

def enter_dungeon(delay=1):
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
      log_action(MSG_BUTTON_NOT_FOUND)

  wait(delay)

def challenge_dungeon(delay=0):
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
        log_action(MSG_BUTTON_NOT_FOUND)
    else:
      try:
        challengedg = pyauto.locateOnScreen(IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
        log_action(MSG_BUTTON_FOUND)
      except pyauto.ImageNotFoundException:
        log_action(MSG_BUTTON_NOT_FOUND)
        challenging = False
        break

  if delay != 0: wait(delay)

def check_notifications():
  try:
    check_notify = pyauto.locateOnScreen(IMG_CHECK_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NOTIFICATION_NOT_FOUND)

  time.sleep(0.2)

  try:
    check_notify = pyauto.locateOnScreen(IMG_CLOSE_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NOTIFICATION_NOT_FOUND)

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
      ending_dungeon = pyauto.locateOnScreen(IMG_END_DG, grayscale=False, confidence=.9, region=get_middle_region())
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
      dice_roll = pyauto.locateOnScreen(IMG_DICE_ROLL, grayscale=False, confidence=.9, region=get_middle_region())
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
      dice_confirm = pyauto.locateOnScreen(IMG_DICE_OKAY, grayscale=False, confidence=.9, region=get_middle_region())
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

def focus_high_mobs(unit=UNIT_BLANK, select=1):
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
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_archer_region())
      log_action(MSG_ATTACK_MOBS + unit)
      do_special_attack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_MOB_CLEARED)
      combo = False

def focus_high_boss(unit=UNIT_BLANK, select=1, aura=1, type=0):
  combo = True
  cast_mode = True
  mode_time = time.time()
  mode = 2

  if get_last_cast_mode() == STATE_TWO: mode = 3
  elif get_last_cast_mode() == STATE_THREE: mode = 2
  else: mode = 2

  if select == STATE_ONE:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    check_time = time.time()
    sec_difference = math.ceil(check_time - mode_time)

    if sec_difference >= 30 and sec_difference <= 35 and aura == STATE_ONE:
      do_aura(2)
      do_short_buffs()

    if sec_difference % 30 == 0:
      do_hard_debuff()
      do_debuff()

    if sec_difference >= 95:
      cast_mode = True
      cast_mode = True
      cancel_aura(1.5)

    if mode == STATE_THREE and cast_mode == True:
      do_final_mode()
      set_last_cast_mode(mode)
      mode = 2
      cast_mode = False
      mode_time = time.time()
    elif mode == STATE_TWO and cast_mode == True:
      force_battle_mode()
      set_last_cast_mode(mode)
      mode = 3
      cast_mode = False
      mode_time = time.time()

    try:
      if type == STATE_ZERO: boss = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_archer_region())
      elif type == STATE_ONE: boss = pyauto.locateOnScreen(IMG_BOSS, grayscale=False, confidence=.9, region=get_archer_region())
      elif type == STATE_TWO: boss = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_archer_region())
      log_action(MSG_ATTACK_MOBS + unit)
      do_special_attack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
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
      log_action(MSG_MOBS_NOT_FOUND)

    try:
      if select == STATE_ONE:
        do_select(0.1)
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
      plunder_box(select, 3)

      if select == STATE_ONE:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOX_NOT_FOUND)
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
