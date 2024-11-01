import math
import time
import sys
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from tkinter import *
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import common.constants as consts
import common.attack as atk

pynboard = Controller()

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
val_buffs = True
val_cancel_buffs = False
val_shorts = True
val_hard_shorts = False
val_debuffs = False
val_hard_debuffs = False
val_close_app = False
val_vera = True
aura_counter = 0
val_runs = 1
val_run_restart = 0
val_run_restart_stack = 0
val_pword = 'default'
val_pin = '123'
val_resolution = '0'
val_load_time = 0
val_channel = 4
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
  set_access_level(args[consts.DATA_ACCESS_LEVEL])
  set_char_class(args[consts.DATA_CHAR_CLASS])
  set_initial_battle_mode(int(args[consts.DATA_MODE]))
  set_battle_mode_status(False)
  set_party_leader_status(args[consts.DATA_LEADER])
  set_party_member_status(args[consts.DATA_MEMBER])
  set_buffs_status(args[consts.DATA_BUFFS])
  set_cancel_buffs_status(args[consts.DATA_CANCEL_BUFFS])
  set_debuffs_status(args[consts.DATA_DEBUFFS])
  set_hard_debuffs_status(args[consts.DATA_HARD_DEBUFFS])
  set_shorts_status(args[consts.DATA_SHORTS])
  set_hard_shorts_status(args[consts.DATA_HARD_SHORTS])
  set_veradrix_status(args[consts.DATA_VERADRIX])
  set_total_run_count(args[consts.DATA_RUNS])
  set_run_restart_status(args[consts.DATA_RUN_RESTART])
  set_password(args[consts.DATA_PWORD])
  set_pin(args[consts.DATA_PIN])
  set_resolution(args[consts.DATA_RESOLUTION])
  set_channel(args[consts.DATA_CHANNEL])
  set_load_time(args[consts.DATA_LOAD])
  set_close_app_status(args[consts.DATA_CLOSE_APP])

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
  click = consts.CLICK_LEFT if right == consts.IS_FALSE else consts.CLICK_RIGHT
  move(x, y)
  pyauto.click(button=click)

  if delay != 0: time.sleep(delay)

def click_press_combo(key_hold, key_one, right=False):
  click = consts.CLICK_LEFT if right == consts.IS_FALSE else consts.CLICK_RIGHT

  pynboard.press(key_hold)
  time.sleep(0.15)

  pyauto.click(button=click)
  pynboard.release(key_hold)
  time.sleep(0.15)

  if key_one != consts.STATE_EMPTY:
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
  log_action(consts.MSG_WAIT)
  time.sleep(delay)

def log_run(run_number, fail_run_count=0):
  if fail_run_count == consts.STATE_ZERO:
    run_builder = consts.MSG_RUN_NUMBER + str(run_number) + consts.LBL_HYPHEN + str(get_total_run_count())
  else:
    run_builder = consts.MSG_RUN_NUMBER + str(run_number) + consts.LBL_HYPHEN + str(get_total_run_count()) + consts.LBL_OPEN_SECTION + str(fail_run_count) + consts.LBL_CLOSE_SECTION

  lbl_current_run.config(text=run_builder)

  print(run_builder)
  frame_root.update()

def log_action(message):
  msg_builder = consts.MSG_ACTION + message

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
  time_difference = consts.STATE_EMPTY

  if hour_difference > 0:
    time_difference += str(hour_difference) + consts.STRING_HOUR

  if min_difference > 0:
    time_difference += str(min_difference - (hour_difference * 60)) +  consts.STRING_MIN

  time_difference += str(sec_difference - (min_difference * 60)) +  consts.STRING_SEC

  val_time_difference = consts.LBL_RUN_TIME + time_difference
  lbl_run_time.config(text=val_time_difference)
  frame_root.update()

  if delay != 0: time.sleep(delay)

def terminate():
  log_action(consts.MSG_EXIT)
  global macro
  macro = False

def pause():
  log_action(consts.MSG_PAUSE)
  wait(15)

def countdown_timer(delay):
  total_countdown = delay
  for x in range(delay):
    log_action(consts.MSG_COUNTDOWN + str(total_countdown))
    total_countdown -= 1
    time.sleep(1)

def countdown_rel_timer(rel, conf, delay):
  total_countdown = delay
  for x in range(delay):
    log_action(consts.MSG_COUNTDOWN + str(total_countdown))
    total_countdown -= 1
    time.sleep(1)

    try:
      window = pyauto.locateOnScreen(rel, grayscale=False, confidence=conf)
      break
    except pyauto.ImageNotFoundException:
      pass

def open_app():
  log_action(consts.MSG_OPEN_APPLICATION)
  check_window = True
  keyword = "CABAL W"
  while check_window:
    if check_window == False:
      break

    windows_start = pyauto.locateOnScreen(consts.IMG_START_WINDOWS, grayscale=True, confidence=.8)
    move_click_rel(10, 15, windows_start, 1)

    for key in keyword: press_release(key, 0.1)
    wait(1)
    press_release(Key.enter)
    countdown_timer(10)

    try:
      launch_load = pyauto.locateOnScreen(consts.IMG_LAUCHER_LOAD, grayscale=False, confidence=.9)
      log_action(consts.MSG_LAUNCHER_LOAD_FAIL)
      continue
    except pyauto.ImageNotFoundException:
      log_action(consts.MSG_LAUNCHER_LOAD)

    try:
      launch_complete = pyauto.locateOnScreen(consts.IMG_LAUCHER_COMPLETE, grayscale=False, confidence=.7)
      log_action(consts.MSG_LAUNCHER_LOAD_COMPLETE)
    except pyauto.ImageNotFoundException:
      log_action(consts.MSG_LAUNCHER_LOAD_FAIL)
      continue

    try:
      launch_play = pyauto.locateOnScreen(consts.IMG_LAUNCHER_PLAY, grayscale=False, confidence=.9)
      log_action(consts.MSG_PLAY_BTN_FOUND)
      move_click_rel(20, 15, launch_play)
    except pyauto.ImageNotFoundException:
      log_action(consts.MSG_PLAY_BTN_NOT_FOUND)
      continue

    try:
      countdown_rel_timer(consts.IMG_LOGIN, 0.8, get_load_time())
      window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
      log_action(consts.MSG_CABAL_WINDOW_FOUND)
      set_cabal_window(window)
      initialize_region()
      check_window = False
    except pyauto.ImageNotFoundException:
      log_action(consts.MSG_CABAL_WINDOW_NOT_FOUND)

  countdown_timer(2)

def get_window_coordinates(resolution):
  coords = []
  if resolution == "2560x1440":
    coords = [1260, 360]
  elif resolution == "1920x1080":
    coords = [620, 150]

  return coords

def move_app():
  log_action(consts.MSG_MOVE_APPLICATION)

  go_cabal_window()
  application = pyauto.getActiveWindow()
  if val_resolution == "2560x1440":
    application.moveTo(1260, 360)
  elif val_resolution == "1920x1080":
    application.moveTo(620, 150)

  window = pyauto.locateOnScreen(consts.IMG_CABAL_WINDOW, grayscale=False, confidence=.8)
  set_cabal_window(window)
  initialize_region()

  countdown_timer(2)

def type_password():
  log_action(consts.MSG_TYPE_PASSWORD)
  for key in val_pword: press_release(key, 0.1)

def type_pin():
  log_action(consts.MSG_TYPE_PIN)
  for key in val_pin:
    match key:
      case "1": pin_number = pyauto.locateOnScreen(consts.IMG_ONE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "2": pin_number = pyauto.locateOnScreen(consts.IMG_TWO, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "3": pin_number = pyauto.locateOnScreen(consts.IMG_THREE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "4": pin_number = pyauto.locateOnScreen(consts.IMG_FOUR, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "5": pin_number = pyauto.locateOnScreen(consts.IMG_FIVE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "6": pin_number = pyauto.locateOnScreen(consts.IMG_SIX, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "7": pin_number = pyauto.locateOnScreen(consts.IMG_SEVEN, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "8": pin_number = pyauto.locateOnScreen(consts.IMG_EIGHT, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "9": pin_number = pyauto.locateOnScreen(consts.IMG_NINE, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case "0": pin_number = pyauto.locateOnScreen(consts.IMG_ZERO, grayscale=False, confidence=.8, region=get_sub_screen_region())
      case _: pin_number = pyauto.locateOnScreen(consts.IMG_ZERO, grayscale=False, confidence=.8, region=get_sub_screen_region())

    move_rel(10, 15, pin_number, 0.2)
    move_click_rel(10, 15, pin_number, 0.2)

  move(580, 530)
  move_click(580, 530, 2)

def enter_world():
  log_action(consts.MSG_ENTER_WORLD)
  press_release(Key.enter, 8)
  press_release(Key.right, 0.5)

  img_channel = consts.IMG_CHANNEL_FOUR
  if get_channel() == consts.STATE_ONE: img_channel = consts.IMG_CHANNEL_ONE
  elif get_channel() == consts.STATE_TWO: img_channel = consts.IMG_CHANNEL_TWO
  elif get_channel() == consts.STATE_THREE: img_channel = consts.IMG_CHANNEL_THREE
  elif get_channel() == consts.STATE_FOUR: img_channel = consts.IMG_CHANNEL_FOUR

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
  log_action(consts.MSG_CHECKING_SUB_PASS)
  while check_pass:
    if check_count >= 3:
      check_pass = False

    if check_pass == False:
      break

    try:
      press_release(Key.enter, 0.4)
      sub_pass = pyauto.locateOnScreen(consts.IMG_SUB_PASS, grayscale=False, confidence=.8, region=get_sub_screen_region())
      log_action(consts.MSG_SUB_PASS_FOUND)
      check_count += 3
      check_pass = False
      type_pin()
      press_release(Key.enter, 0.4)
      break
    except pyauto.ImageNotFoundException:
      check_count += 1
      log_action(consts.MSG_SUB_PASS_NOT_FOUND)

  countdown_timer(10)
  log_action(consts.MSG_CLEARING_WINDOWS)
  for x in range(3): press_release(Key.esc)

def move_bead_window():
  try:
    log_action(consts.MSG_MOVE_BEAD)
    bead_window = pyauto.locateOnScreen("img/bead.jpg", grayscale=False, confidence=.8, region=get_screen_region())
    move_rel(10, 10, bead_window)
    pyauto.mouseDown(button="left")
    move(100, 700)
    pyauto.mouseUp(button="left")
    countdown_timer(2)
  except pyauto.ImageNotFoundException:
    log_action(consts.MSG_BEAD_WINDOW_NOT_FOUND)

def select_task_bar():
  log_action(consts.MSG_SELECT_TASK_BAR)
  coords = val_resolution.split('x')
  x = int(coords[0]) / 2
  y = int(coords[1]) - 20

  for i in range(3):
    pyauto.moveTo(x, y)
    pyauto.click(x, y)

def exit_app(finish=False):
  log_action(consts.MSG_CLOSE_APPLICATION)
  go_cabal_window()
  move(1260, 15)
  move_click(1260, 15)
  press_release(Key.enter)

  if finish == consts.IS_FALSE: countdown_timer(5)

def check_run_restart(run_count):
  global val_run_restart_stack
  if get_run_restart_status() > 0:
    log_action(consts.MSG_CHECK_RECONNECT)
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
  if is_battle_mode and get_attack_type() == consts.IS_RANGE:
    return region_mode_bar
  else:
    return region_normal_bar

def get_full_region():
  if is_battle_mode and get_attack_type() == consts.IS_RANGE:
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
  if get_char_class() == consts.VAL_CLASS_FA or get_char_class() == consts.VAL_CLASS_FG or get_char_class() == consts.VAL_CLASS_DM:
    return consts.IS_RANGE

  return consts.IS_MELEE

def set_last_cast_mode(mode):
  global val_last_cast_mode
  val_last_cast_mode = mode

def get_last_cast_mode():
  global val_last_cast_mode
  return val_last_cast_mode

def get_party_status():
  if get_party_leader_status() == consts.IS_TRUE or get_party_member_status() == consts.IS_TRUE: return True
  return False

def set_party_leader_status(leader):
  global val_leader
  val_leader = True if leader == consts.STATE_ONE else False

def get_party_leader_status():
  return val_leader

def set_party_member_status(member):
  global val_member
  val_member = True if member == consts.STATE_ONE else False

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
  val_vera = True if status == consts.STATE_ONE else False

def get_veradrix_status():
  return val_vera

def set_buffs_status(status):
  global val_buffs
  val_buffs = True if status == consts.STATE_ONE else False

def get_buffs_status():
  return val_buffs

def set_debuffs_status(status):
  global val_debuffs
  val_debuffs = True if status == consts.STATE_ONE else False

def get_debuffs_status():
  return val_debuffs

def set_hard_debuffs_status(status):
  global val_hard_debuffs
  val_hard_debuffs = True if status == consts.STATE_ONE else False

def get_hard_debuffs_status():
  return val_hard_debuffs

def set_cancel_buffs_status(status):
  global val_cancel_buffs
  val_cancel_buffs = True if status == consts.STATE_ONE else False

def get_cancel_buffs_status():
  return val_cancel_buffs

def set_shorts_status(status):
  global val_shorts
  val_shorts = True if status == consts.STATE_ONE else False

def get_shorts_status():
  return val_shorts

def set_hard_shorts_status(status):
  global val_hard_shorts
  val_hard_shorts = True if status == consts.STATE_ONE else False

def get_hard_shorts_status():
  return val_hard_shorts

def get_interval_melee():
  return consts.VAL_INTERVAL_MELEE

def get_interval_range():
  return consts.VAL_INTERVAL_RANGE

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
  val_close_app = True if status == consts.STATE_ONE else False

def get_close_app_status():
  return val_close_app

def do_close_app_status():
  if get_close_app_status() == consts.IS_TRUE:
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
    timeout = pyauto.locateOnScreen(consts.IMG_TIMEOUT, grayscale=False, confidence=.7, region=get_middle_region())
    timeout_exit = pyauto.locateOnScreen(consts.IMG_TIMEOUT_EXIT, grayscale=False, confidence=.9, region=get_middle_region())
    move_click_rel(10, 10, timeout_exit, 0.2)
  except pyauto.ImageNotFoundException:
    pass

  time.sleep(3)

def go_skill_slot(delay=0):
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

  if delay != 0: time.sleep(delay)

def set_battle_mode(val, cancel=True):
  if cancel == consts.IS_TRUE: cancel_aura(1.2)

  if get_battle_mode() == consts.STATE_ONE:
    global is_battle_mode
    is_battle_mode = val

def reset_battle_mode(delay=0):
  cancel_aura(delay)

  if get_battle_mode() == consts.STATE_ONE:
    global is_battle_mode
    is_battle_mode = False

def do_battle_mode(delay=5, cancel=True, aura=True):
  if get_battle_mode() == consts.STATE_ONE:
    log_action(consts.MSG_BATTLE_MODE)
    set_battle_mode(True, cancel)

    click_combo(790, 670, True)
    click_combo(790, 670, True)

    for x in range(delay):
      do_essentials()
      time.sleep(1)

    if aura == consts.IS_TRUE:
      pynboard.press(consts.KEY_AURA)
      pynboard.release(consts.KEY_AURA)
      time.sleep(1)

def force_battle_mode(delay=5):
  click_combo(790, 670, True)
  click_combo(790, 670, True)

  if get_char_class() == consts.VAL_CLASS_FB:
    delay = 4

  for x in range(delay):
    do_essentials()
    time.sleep(1)

def do_cont_battle_mode():
  if get_battle_mode() == consts.STATE_ONE:
    move(790, 670)
    pyauto.click(button="right")

    do_veradrix()
    global aura_counter
    aura_counter += 1
    if aura_counter > 45:
      do_aura()
      aura_counter = 0

def check_battle_mode():
  if get_last_cast_mode() == consts.STATE_TWO:
    press_combo(Key.alt, consts.KEY_BM)
  elif get_last_cast_mode() == consts.STATE_THREE:
    do_final_mode()

def do_veradrix():
  if get_veradrix_status() == consts.IS_TRUE: press_release(consts.KEY_VERADRIX)

def force_veradrix():
  press_release(consts.KEY_VERADRIX)

def do_buffs():
  if get_buffs_status() == consts.IS_TRUE:
    log_action(consts.MSG_BUFFS)
    click_combo(400, 670, True, 0.6)
    click_combo(430, 670, True, 1)

def cancel_buffs(reps=8):
  if get_cancel_buffs_status() == consts.IS_TRUE:
    for x in range(reps):
      move(1250, 185)
      pyauto.click(button="right")
      time.sleep(0.2)

def do_short_buffs():
  if get_shorts_status() == consts.IS_TRUE:
    log_action(consts.MSG_SHORT_BUFFS)
    click_combo(470, 670, True, 0.2)
    click_combo(500, 670, True, 0.2)

    do_hard_short_buffs()

def do_hard_short_buffs():
  if get_hard_shorts_status() == consts.IS_TRUE:
    if get_char_class() == consts.VAL_CLASS_BL:
      click_combo(540, 670, True, 0.5)
      click_combo(570, 670, True, 0.5)

def force_short_buffs():
  log_action(consts.MSG_SHORT_BUFFS)
  click_combo(470, 670, True, 0.2)
  click_combo(500, 670, True, 0.2)

  if get_char_class() == consts.VAL_CLASS_BL:
    click_combo(540, 670, True, 0.5)
    click_combo(570, 670, True, 0.5)

def do_debuff(delay=1.5):
  if get_debuffs_status() == consts.IS_TRUE:
    log_action(consts.MSG_DEBUFF)
    click_combo(610, 670, True, delay)
    force_veradrix()

def do_hard_debuff(delay=1.5):
  if get_hard_debuffs_status() == consts.IS_TRUE:
    log_action(consts.MSG_DEBUFF_HARD)
    click_combo(650, 670, True, delay)
    force_veradrix()

def cancel_aura(delay=0):
  click_combo(175, 100, True)

  if delay != 0: time.sleep(delay)

def do_dash(delay=1.0):
  do_heal()
  pynboard.press(consts.KEY_DASH)
  pynboard.release(consts.KEY_DASH)

  if delay != 0: time.sleep(delay)

def do_fade(delay=0.5):
  pynboard.press(consts.KEY_FADE)
  pynboard.release(consts.KEY_FADE)

  if delay != 0: time.sleep(delay)

def do_select(delay=0):
  pynboard.press(consts.KEY_SELECT)
  pynboard.release(consts.KEY_SELECT)

  if delay != 0: time.sleep(delay)

def do_deselect(delay=0):
  pynboard.press(consts.KEY_DESELECT)
  pynboard.release(consts.KEY_DESELECT)

  if delay != 0: time.sleep(delay)

def do_deselect_pack():
  do_deselect()
  do_deselect(0.1)
  do_deselect(0.1)

def roll_box():
  if get_party_status() == consts.IS_TRUE:
    try:
      roll = pyauto.locateOnScreen(consts.IMG_DICE_EQUIP, grayscale=False, confidence=.9, region=get_screen_region())
      log_action(consts.MSG_ROLL_EQUIPMENT)
      move_rel(10, 10, roll, 0.2)
      move_click_rel(10, 10, roll, 0.2)
    except pyauto.ImageNotFoundException:
      log_action(consts.MSG_ROLL_EQUIPMENT_NOT_FOUND)

def party_roll_box(reps=4):
  roll_reps = reps * 3
  for x in range(roll_reps):
    roll_box()
    if get_veradrix_status() == consts.IS_TRUE: do_veradrix()
    time.sleep(0.3)

def do_plunder(reps=4):
  for x in range(reps):
    log_action(consts.MSG_LOOTING_DROP)
    pynboard.press(consts.KEY_LOOT_ACTION)
    pynboard.release(consts.KEY_LOOT_ACTION)
    time.sleep(0.3)
    pynboard.press(consts.KEY_LOOT_SPACE)
    pynboard.release(consts.KEY_LOOT_SPACE)
    time.sleep(0.3)
    roll_box()

def do_fast_plunder():
  pynboard.press(consts.KEY_LOOT_ACTION)
  pynboard.release(consts.KEY_LOOT_ACTION)
  pynboard.press(consts.KEY_LOOT_SPACE)
  pynboard.release(consts.KEY_LOOT_SPACE)

def do_heal():
  pynboard.press(consts.KEY_HP)
  pynboard.release(consts.KEY_HP)

def do_essentials(release_keys=True):
  pynboard.press(consts.KEY_LOOT_SPACE)
  pynboard.release(consts.KEY_LOOT_SPACE)
  pynboard.press(consts.KEY_FURY)
  pynboard.release(consts.KEY_FURY)
  pynboard.press(consts.KEY_HP)
  pynboard.release(consts.KEY_HP)
  pynboard.press(consts.KEY_LOOT_ACTION)
  pynboard.release(consts.KEY_LOOT_ACTION)
  do_veradrix()

  if release_keys == consts.IS_TRUE:
    pynboard.release(Key.shift)
    pynboard.release(Key.alt)
    pynboard.release(Key.ctrl)

def release_keys(delay=0):
  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

  if delay != 0: time.sleep(delay)

def do_aura(delay=0):
  pynboard.press(consts.KEY_AURA)
  pynboard.release(consts.KEY_AURA)

  if delay != 0: time.sleep(delay)

def do_final_mode(delay=0):
  if get_battle_mode_status() == False:
    pynboard.press(consts.KEY_BM)
    pynboard.release(consts.KEY_BM)

    if delay != 0: time.sleep(delay)

def do_attack(delay=0, strict=False, cont=True):
  do_veradrix()

  if get_battle_mode_status():
    pynboard.press(consts.KEY_BM_ATK)
    pynboard.release(consts.KEY_BM_ATK)
    if strict == consts.IS_FALSE: do_essentials()
    if cont == consts.IS_TRUE: do_cont_battle_mode()
  else:
    pynboard.press(consts.KEY_BM_ATK)
    pynboard.release(consts.KEY_BM_ATK)
    if strict == consts.IS_FALSE: do_essentials()

    pynboard.press(consts.KEY_BM_ATK)
    pynboard.release(consts.KEY_BM_ATK)
    if strict == consts.IS_FALSE: do_essentials()

    pynboard.press(consts.KEY_BM_ATK)
    pynboard.release(consts.KEY_BM_ATK)
    if strict == consts.IS_FALSE: do_essentials()

    pynboard.press(consts.KEY_ATTACK[0])
    pynboard.release(consts.KEY_ATTACK[0])
    if strict == consts.IS_FALSE: do_essentials()

    pynboard.press(consts.KEY_ATTACK[1])
    pynboard.release(consts.KEY_ATTACK[1])
    if strict == consts.IS_FALSE: do_essentials()

    pynboard.press(consts.KEY_ATTACK[2])
    pynboard.release(consts.KEY_ATTACK[2])
    if strict == consts.IS_FALSE: do_essentials()

  if delay != 0: time.sleep(delay)

def do_special_attack(delay=0.1):
  pynboard.press(consts.KEY_BM_ATK)
  pynboard.release(consts.KEY_BM_ATK)

  force_veradrix()
  do_essentials()
  check_battle_mode()

  if delay != 0: time.sleep(delay)

def check_notifications():
  try:
    check_notify = pyauto.locateOnScreen(consts.IMG_CHECK_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(consts.MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(consts.MSG_NOTIFICATION_NOT_FOUND)

  time.sleep(0.2)

  try:
    check_notify = pyauto.locateOnScreen(consts.IMG_CLOSE_NOTIF, grayscale=False, confidence=.9, region=get_notification_region())
    move_click_rel(10, 10, check_notify, 0.2)
    log_action(consts.MSG_NOTIFICATION_FOUND)
  except pyauto.ImageNotFoundException:
    log_action(consts.MSG_NOTIFICATION_NOT_FOUND)

  time.sleep(0.2)
