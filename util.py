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
val_deselect = Key.esc
loot_space = Key.space

# GLOBAL VARIABLES
cabalwindow = []
frame_root = []
lbl_current_run = []
lbl_macro = []
macro = True
battle_mode = 0
is_battle_mode = False
is_buffs_allowed = 1
is_short_buffs_allowed = 1
is_veradrix_allowed = 0
is_party = 0
is_leader = 0
aura_counter = 0
atk_type = 0
trigger_reset_dungeon = False

region_normal_bar = []
region_mode_bar = []
region_screen = []
region_full_normal_bar = []
region_full_mode_bar = []
region_notification = []

# CONSTANT UI VARIABLES
APP_FONT = "Tahoma 10"
APP_FRAME_SIZE = "330x230"
APP_NAME = "Cabal JTool "
APP_VERSION = "v5.01"
APP_FULL_NAME = APP_NAME + APP_VERSION
HOTKEY_TERMINATE = "ctrl+r"
HOTKEY_PAUSE = "ctrl+p"

# CONSTANT MESSAGES
MSG_START_DG = "Starting Dungeon"
MSG_END_DG = "End Dungeon"
MSG_EXIT = "Macro Exit"
MSG_PAUSE = "Pause for 10 seconds"
MSG_TERMINATE ="Macro Terminate"
MSG_PATH_FIND = "Pathfind, "
MSG_ATTACK_MOBS = "Attack, "
MSG_ATTACK_BOSS = "Boss Attack"
MSG_MOBS_FOUND = "Mobs Found, "
MSG_BOSS_FOUND = "Boss Found"
MSG_BOSS_KILLED = "Boss Killed"
MSG_NO_MOBS_FOUND = "No Mobs Found"
MSG_NO_BOSS_FOUND = "No Boss Found"
MSG_MOBS_CLEARED = "Mobs Cleared"
MSG_CHECK_BOSS = "Checking Boss"
MSG_BOX_FOUND = "Box Found"
MSG_NO_BOX_FOUND = "No Box Found"
MSG_PATH_STOP = "Pathing stop, attacking"
MSG_MOVE_STOP = "Moving stop, proceeding"
MSG_CHECK_END_DG = "Check End Dungeon"
MSG_NOTIFICATION_FOUND = "Notification Found"
MSG_NO_NOTIFICATION_FOUND = "No Notification Found"
MSG_ACTION = ""
MSG_RUN_NUMBER =  "Run #: "
MSG_BACKTRACK = "Backtrack #: "
MSG_CHALLENGE_DG = "Challenge Dungeon"
MSG_ENTER_DG = "Enter Dungeon"
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

# CONSTANT IMAGES
IMG_APP_ICON = "img/icon.png"
IMG_CABAL_WINDOW = "img/cabalwindow.jpg"
IMG_CHALLENGE_DG = "img/challengedg.jpg"
IMG_DUNGEON = "img/dungeon.jpg"
IMG_ENTER_DG = "img/enterdg.jpg"
IMG_END_DG = "img/enddg.jpg"
IMG_EXIT_DG = "img/exitdg.jpg"
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
IMG_SHOWORAI = "img/showorai.jpg"

# CONSTANT UNITS
UNIT_BLANK = "--"
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
UNIT_DARK_ARCHER = "Dark Archer"
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
UNIT_BOX = "Box"

def initialize(window, frame, mlbl, rlbl):
  global macro
  macro = True

  global cabalwindow
  cabalwindow = window

  global frame_root
  frame_root = frame

  global lbl_macro
  lbl_macro = mlbl

  global lbl_current_run
  lbl_current_run = rlbl

  global region_normal_bar
  region_normal_bar = (int(cabalwindow[0] + 475), int(cabalwindow[1] + 25), 45, 30)

  global region_mode_bar
  region_mode_bar = (int(cabalwindow[0] + 350), int(cabalwindow[1] + 25), 325, 30)

  global region_screen
  region_screen = (int(cabalwindow[0]), int(cabalwindow[1]) + 20, 1265, 720)

  global region_full_normal_bar
  region_full_normal_bar = (int(cabalwindow[0] + 477), int(cabalwindow[1] + 25), 283, 30)

  global region_full_mode_bar
  region_full_mode_bar = (int(cabalwindow[0] + 354), int(cabalwindow[1] + 25), 565, 30)

  global region_notification
  region_notification = (int(cabalwindow[0]) + 1235, int(cabalwindow[1]) + 270, 30, 400)


def set_variables(mode=0, buff=1, sbuffs=1, atk=0, vera=0, party=0, leader=0):
  global battle_mode
  battle_mode = int(mode)

  global is_battle_mode
  is_battle_mode = False

  global is_buffs_allowed
  is_buffs_allowed = int(buff)

  global is_short_buffs_allowed
  is_short_buffs_allowed = int(sbuffs)

  global atk_type
  atk_type = int(atk)

  global is_veradrix_allowed
  is_veradrix_allowed = vera

  global is_party
  is_party = party

  global is_leader
  is_leader = leader

def set_cabal_window(window):
  global cabalwindow
  cabalwindow = window

def go_cabal_window():
  move_click(50, 15)

def move(x, y, sec=0):
  pyauto.moveTo(cabalwindow[0] + x, cabalwindow[1] + y)

  if (sec != 0):
    time.sleep(sec)

def move_rel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)

  if (sec != 0):
    time.sleep(sec)

def move_click(x, y, sec=0):
  pyauto.moveTo(cabalwindow[0] + x, cabalwindow[1] + y)
  pyauto.click(cabalwindow[0] + x, cabalwindow[1] + y)

  if (sec != 0):
    time.sleep(sec)

def move_click_rel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)
  pyauto.click(ref[0] + x, ref[1] + y)

  if (sec != 0):
    time.sleep(sec)

def wait(sec=1):
  log_action(MSG_WAIT)
  time.sleep(sec)

def log_run(runNumber):
  runBuilder = StringVar()
  runBuilder = MSG_RUN_NUMBER + str(runNumber)
  print(runBuilder)
  lbl_current_run.config(text=runBuilder)
  frame_root.update()

def log_action(message):
  msgBuilder = StringVar()
  msgBuilder = MSG_ACTION + message
  print(msgBuilder)
  lbl_macro.config(text=msgBuilder)
  frame_root.update()

def terminate():
  log_action(MSG_EXIT)
  global macro
  macro = False

def pause():
  log_action(MSG_PAUSE)
  wait(10)

def get_region():
  if is_battle_mode and atk_type == 1:
    return region_mode_bar
  else:
    return region_normal_bar

def get_full_region():
  if is_battle_mode and atk_type == 1:
    return region_full_mode_bar
  else:
    return region_full_normal_bar

def get_screen_region():
  return region_screen

def get_notification_region():
  return region_notification

def get_atk_type():
  return atk_type

def get_battle_mode():
  return battle_mode

def get_reset_status():
  return trigger_reset_dungeon

def set_reset_status(val=False):
  global trigger_reset_dungeon
  trigger_reset_dungeon = val

def get_party_status():
  return is_party

def get_party_leader_status():
  return is_leader

def get_macro_state():
  return macro

def force_exit_dungeon():
  wait(3)
  move_click(830, 710)
  wait(0.5)

  move_click(850, 430)
  wait(0.5)

  move_click(1030, 485)
  wait(1)

  move_click(620, 440)
  wait(3)

def go_skill_slot(sec=0):
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

  if (sec != 0):
    time.sleep(sec)

def set_battle_mode(val):
  cancel_aura(1)
  if battle_mode == 1:
    global is_battle_mode
    is_battle_mode = val

def do_battle_mode(sec=5):
  if battle_mode == 1:
    log_action(MSG_BATTLE_MODE)
    cancel_aura(1)

    move(790, 670)
    pyauto.click(button="right")

    move(790, 670)
    pyauto.click(button="right")

    global is_battle_mode
    is_battle_mode = True
    time.sleep(sec)

    pynboard.press(val_bm_aura)
    pynboard.release(val_bm_aura)
    time.sleep(1)

def do_veradrix():
  if is_veradrix_allowed == 1:
    pynboard.press(val_veradrix)
    pynboard.release(val_veradrix)

def do_cont_battle_mode():
  move(790, 670)
  pyauto.click(button="right")

  do_veradrix()
  global aura_counter
  aura_counter += 1
  if aura_counter > 45:
    do_aura_strict()
    aura_counter = 0

def do_buffs():
  if is_buffs_allowed == 1:
    log_action(MSG_BUFFS)
    move(400, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(430, 670)
    pyauto.click(button="right")
    time.sleep(2)

def do_short_buffs():
  if is_short_buffs_allowed == 1:
    log_action(MSG_SHORT_BUFFS)
    move(470, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

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
    time.sleep(0.5)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(540, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(570, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

def cancel_aura(sec=0):
  move(175, 100)
  pyauto.click(button="right")

  if (sec != 0):
    time.sleep(sec)

def do_dash(sec=0):
  pynboard.press(val_dash)
  pynboard.release(val_dash)

  if (sec != 0):
    time.sleep(sec)

def do_fade(sec=0):
  pynboard.press(val_fade)
  pynboard.release(val_fade)

  if (sec != 0):
    time.sleep(sec)

def do_select(sec=0):
  pynboard.press(val_select)
  pynboard.release(val_select)

  if (sec != 0):
    time.sleep(sec)

def do_deselect(sec=0):
  pynboard.press(val_deselect)
  pynboard.release(val_deselect)

  if (sec != 0):
    time.sleep(sec)

def do_deselect_pack():
  do_deselect()
  do_deselect(0.1)
  do_deselect(0.1)

def do_loot():
  do_select(0.1)
  do_select(0.1)
  if is_battle_mode:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    do_essentials()
  else:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    pynboard.press(val_attack[0])
    pynboard.release(val_attack[0])
    pynboard.press(val_attack[1])
    pynboard.release(val_attack[1])
    pynboard.press(val_attack[2])
    pynboard.release(val_attack[2])
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)

  for x in range(4):
    pynboard.press(val_loot)
    pynboard.release(val_loot)
    time.sleep(0.3)
    pynboard.press(loot_space)
    pynboard.release(loot_space)
    time.sleep(0.3)

def loot_box(sec=3, select=1):
  checking = True
  boxCounter = 0
  while checking:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      if select == 1:
        do_select(0.1)
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BOX_FOUND)

    do_loot()
    if is_party == 1:
      try:
        roll = pyauto.locateOnScreen(IMG_DICE_EQUIP, grayscale=False, confidence=.9, region=get_screen_region())
        log_action(MSG_ROLL_EQUIPMENT)
        move_click_rel(10, 10, roll)
        move_click_rel(10, 10, roll)
      except pyauto.ImageNotFoundException:
        log_action(MSG_NO_ROLL_EQUIPMENT_FOUND)

    boxCounter += 1
    if boxCounter > sec:
      boxCounter = 0
      break

def loot_final_box(sec=4):
  checking = True
  boxCounter = 0
  while checking:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      do_select(0.1)
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BOX_FOUND)

    do_loot()
    if is_party == 1:
      try:
        roll = pyauto.locateOnScreen(IMG_DICE_EQUIP, grayscale=False, confidence=.9, region=get_screen_region())
        log_action(MSG_ROLL_EQUIPMENT)
        move_click_rel(10, 10, roll)
        move_click_rel(10, 10, roll)
      except pyauto.ImageNotFoundException:
        log_action(MSG_NO_ROLL_EQUIPMENT_FOUND)

    boxCounter += 1
    if boxCounter > sec:
      boxCounter = 0
      break

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

def loot_essentials():
  pynboard.press(loot_space)
  pynboard.release(loot_space)
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

  if (sec != 0):
    time.sleep(sec)

def do_aura(sec=0):
  pynboard.press(val_bm3)
  pynboard.release(val_bm3)
  do_essentials()
  pynboard.press(val_bm_aura)
  pynboard.release(val_bm_aura)
  do_essentials()
  pynboard.press(val_bm3)
  pynboard.release(val_bm3)

  if (sec != 0):
    time.sleep(sec)

def do_aura_strict(sec=0):
  pynboard.press(val_bm_aura)
  pynboard.release(val_bm_aura)
  pynboard.press(val_bm_aura)
  pynboard.release(val_bm_aura)

  if (sec != 0):
    time.sleep(sec)

def do_attack(sec=0):
  do_veradrix()

  if is_battle_mode:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    do_essentials()
    do_cont_battle_mode()
  else:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    do_essentials()
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    do_essentials()
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    pynboard.press(val_attack[0])
    pynboard.release(val_attack[0])
    do_essentials()
    pynboard.press(val_attack[1])
    pynboard.release(val_attack[1])
    do_essentials()
    pynboard.press(val_attack[2])
    pynboard.release(val_attack[2])
    do_essentials()

  if (sec != 0):
    time.sleep(sec)

def do_attack_strict(sec=0):
  if is_battle_mode:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
  else:
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    pynboard.press(val_bm3_atk)
    pynboard.release(val_bm3_atk)
    pynboard.press(val_attack[0])
    pynboard.release(val_attack[0])
    pynboard.press(val_attack[1])
    pynboard.release(val_attack[1])
    pynboard.press(val_attack[2])
    pynboard.release(val_attack[2])

  if (sec != 0):
    time.sleep(sec)

def enter_dungeon():
  entering = True
  while entering:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      entering = False
      
    if entering == False:
      break

    try:
      enterdg = pyauto.locateOnScreen(IMG_ENTER_DG, grayscale=False, confidence=.9)
      move_click_rel(15, 15, enterdg, 1)
      entering = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BUTTON_FOUND)

def challenge_dungeon():
  if (is_party == 1 and is_leader == 1) or (is_party == 0 and is_leader == 0):
    challenging = True
    while challenging:
      if not get_macro_state():
        log_action(MSG_TERMINATE)
        challenging = False

      if challenging == False:
        break

      try:
        challengedg = pyauto.locateOnScreen(IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
        move_click_rel(15, 15, challengedg, 1)
        challenging = False
        break
      except pyauto.ImageNotFoundException:
        log_action(MSG_NO_BUTTON_FOUND)

def check_notifications():
  try:
    check_notify = pyauto.locateOnScreen(IMG_CHECK_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 1)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_NOTIFICATION_FOUND)

  wait(0.5)

  try:
    check_notify = pyauto.locateOnScreen(IMG_CLOSE_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 1)
    log_action(MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(MSG_NO_NOTIFICATION_FOUND)

  wait(0.5)

def end_dungeon():
  ending = True
  endCheckTrack = 0
  while ending:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      ending = False

    if ending == False:
      break

    endCheckTrack += 1
    if (endCheckTrack >= 60):
      ending = False
      break

    try:
      enddungeon = pyauto.locateOnScreen(IMG_END_DG, grayscale=False, confidence=.9)
      move_click_rel(50, 15, enddungeon, 0.5)
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
      rolladice = pyauto.locateOnScreen(IMG_DICE_ROLL, grayscale=False, confidence=.9)
      move_click_rel(50, 15, rolladice, 0.8)
      # move_click_rel(50, 15, rolladice)
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
      diceconfirm = pyauto.locateOnScreen(IMG_DICE_OKAY, grayscale=False, confidence=.9)
      # move_click_rel(10, 15, rolladice, 0.8)
      move_click_rel(10, 5, diceconfirm)
      confirming = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_DICE_ROLL_OKAY)

def focus_gate(unit=UNIT_BLANK, select=1):
  combo = True
  fade_count = 0

  if select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    try:
      if select == 1:
        do_select(0.1)
      gate = pyauto.locateOnScreen(IMG_GATE, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.3)
      do_attack(0.3)
    except pyauto.ImageNotFoundException:
      combo = False
      log_action(MSG_MOBS_CLEARED)
      break

def focus_mobs(unit=UNIT_BLANK, aura=1, select=1, sidestep=1):
  combo = True
  fade_count = 0

  if select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == 1:
      do_aura()

    if sidestep == 1:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    try:
      if select == 1:
        do_select(0.1)
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.1)
      do_attack(0.1)

      if select == 1:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_MOBS_CLEARED)
      combo = False
      break

def attack_backtrack(unit=UNIT_BLANK, aura=1, select=1, sidestep=1):
  combo = True
  fade_count = 0

  if select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      sys.exit()

    if aura == 1:
      do_aura()

    if sidestep == 1:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    try:
      if select == 1:
        do_select(0.1)
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      do_attack(0.1)
      do_attack(0.1)

      if select == 1:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_MOBS_FOUND)

    try:
      if select == 1:
        do_select(0.1)
      box = pyauto.locateOnScreen(IMG_BOX, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_BOX_FOUND)

      do_attack(0.1)
      do_attack(0.1)
      do_attack(0.1)
      do_attack(0.1)
      loot_box(2)

      if select == 1:
        do_deselect_pack()
    except pyauto.ImageNotFoundException:
      log_action(MSG_NO_BOX_FOUND)
      combo = False
      break

def attack_mobs(unit=UNIT_BLANK, aura=1, interval=0.3, sidestep=1):
  combo = True
  fade_count = 0

  do_deselect_pack()
  do_select(0.1)
  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    try:
      boss = pyauto.locateOnScreen(IMG_BOSS, grayscale=False, confidence=.9, region=get_region())
      do_deselect()
      log_action(MSG_BOSS_FOUND)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      log_action(MSG_ATTACK_MOBS + unit)

    if aura == 1:
      do_aura()

    if sidestep == 1:
      if (fade_count == 20):
        fade_count = 0
        move_click(700, 440, 0.2)
        do_fade(0.1)
      else:
        fade_count += 1

    try:
      do_select(0.1)
      mobs = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_MOBS + unit)

      if interval > 0.3:
        do_attack(interval)
        do_attack_strict(0.3)
        do_attack(interval)
        do_attack_strict(0.3)
      else:
        do_attack(interval)
        do_attack(interval)

    except pyauto.ImageNotFoundException:
      log_action(MSG_MOBS_CLEARED)
      combo = False
      break

def attack_boss(select=1, aura=1):
  combo = True

  if is_battle_mode and atk_type == 1:
    do_select(0.1)
    do_select(0.1)
  elif select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if is_battle_mode == False:
      if aura == 1:
        do_aura()

    try:
      boss = pyauto.locateOnScreen(IMG_BOSS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_BOSS)
      do_attack(0.1)
      do_attack(0.1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
      combo = False
      break

def attack_semi_boss(select=1):
  combo = True

  if select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if is_battle_mode == False:
      do_aura()

    try:
      boss = pyauto.locateOnScreen(IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_BOSS)
      do_attack()
      time.sleep(0.1)
      do_attack()
      time.sleep(0.1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
      combo = False
      break

def attack_lava_gate(select=1):
  combo = True

  if select == 1:
    do_select(0.1)

  while combo:
    if not get_macro_state():
      log_action(MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if is_battle_mode == False:
      do_aura()

    try:
      gate = pyauto.locateOnScreen(IMG_MOBS, grayscale=False, confidence=.9, region=get_region())
      log_action(MSG_ATTACK_BOSS)
      do_attack()
      time.sleep(0.1)
      do_attack()
      time.sleep(0.1)
    except pyauto.ImageNotFoundException:
      log_action(MSG_BOSS_KILLED)
      combo = False
      break