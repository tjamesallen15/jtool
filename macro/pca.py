import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import util
pynboard = Controller()

# GLOBAL VARIABLES
frame_root = []
btn_start = []

# UNIQUE VARIABLES
val_sidestep = 0

def initialize(frame, btn, runs=1):
  global frame_root
  frame_root = frame

  global btn_start
  btn_start = btn

  btn_start.config(state="disabled")
  frame_root.update()
  run_dungeon(int(runs))
  btn_start.config(state="active")
  frame_root.update()

def position_nualle():
  util.move(610, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(610, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(610, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(610, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(560, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(610, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(680, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(640, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(570, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(770, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(640, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(500, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(570, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(500, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(640, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(680, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(640, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.do_aura_strict(1)
  util.do_aura(1)
  time.sleep(4)

  util.move(660, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(610, 440)
  util.do_fade(1)

  util.move(680, 380)
  util.do_fade(1)

def position_first_shadow():
  util.move(460, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(640, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(820, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(750, 300)
  util.do_dash(1)

  util.move(600, 350)
  util.do_fade(0.5)

  util.move(620, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(580, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(580, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move_click(580, 350, 2)

  util.move(760, 300)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(720, 200)
  util.do_dash(1)

def position_second_shadow():
  util.move(720, 200)
  util.do_fade(1)

  util.move(720, 200)
  util.do_fade(0.5)

  util.move(780, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(730, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(760, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(670, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(620, 200)
  util.do_dash(1)
  util.do_fade(0.5)

def position_third_shadow():
  util.move(670, 230)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(690, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(690, 150)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(690, 150)
  util.do_dash(1)

def run_dungeon(runs=1):
  run_counter = 0
  trigger_continue = False
  while run_counter < runs:
    trigger_continue = False
    run_counter += 1
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.log_action(util.MSG_START_DG)
    util.log_run(run_counter)

    # Click Cabal Window
    util.go_cabal_window()
    util.release_keys()
    util.do_buffs()
    util.go_skill_slot(0.5)

    util.move_click(720, 360)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    position_nualle()
    # First Boss Sequence
    util.force_short_buffs()
    util.attack_boss()

    time.sleep(3)
    util.move_click(590, 460)
    util.do_fade(1)

    time.sleep(2)
    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(1000, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.loot_box(1)
    util.cancel_aura(2)

    util.move(1000, 520)
    util.do_dash(1)

    util.move_click(580, 440)
    checking = True
    dialog_count = 0
    while checking:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        checking = False
        sys.exit()

      if checking == False:
        break

      if dialog_count == 3:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 2)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        trigger_continue = True

    if trigger_continue:
      continue

    position_first_shadow()
    # First Shadow
    time.sleep(3)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_FEAR, 0, 0, 0)
    time.sleep(1)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_FEAR, 0, 0, 0)
    time.sleep(1)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_FEAR, 0, 0, 0)

    position_second_shadow()
    # Second Shadow
    time.sleep(3)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_RESIGN, 0, 0, 0)
    time.sleep(1)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_RESIGN, 0, 0, 0)

    position_third_shadow()
    # Third Shadow
    time.sleep(3)
    util.do_select(0.1)
    util.focus_mobs(util.UNIT_SHOWORAI_MADNESS, 0, 0, 0)

    util.move_click(580, 430)
    checking = True
    while checking:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        checking = False
        sys.exit()

      if checking == False:
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        trigger_continue = True

    if trigger_continue:
      continue

    # Final Boss
    util.do_battle_mode()
    util.attack_boss(1, 0)
    util.set_battle_mode(False)

    time.sleep(1)
    checking = True
    while checking:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        checking = False
        sys.exit()

      if checking == False:
        break

      try:
        util.move_click(580, 430)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        trigger_continue = True

    if trigger_continue:
      continue

    checking = True
    while checking:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        checking = False
        sys.exit()

      if checking == False:
        break

      try:
        util.move_click(580, 430)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        trigger_continue = True

    if trigger_continue:
      continue

    # Start to End Dungeon
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    time.sleep(3)
