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

  shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
  btn_start.config(state="disabled")
  frame_root.update()
  run_dungeon(int(runs))
  btn_start.config(state="active")
  frame_root.update()

def position_second_boss():
  util.move(700, 350)
  util.do_fade(0.5)

  util.move(200, 320)
  util.do_dash(1.2)
  util.move(200, 520)
  util.do_dash(1.2)

  util.move(600, 520)
  util.do_dash(1.2)

  util.move(200, 320)
  util.do_dash(1.2)

  util.move(200, 420)
  util.do_dash(1.2)

  util.move(620, 280)
  util.do_fade(0.5)

def pre_position_final_boss():
  util.move(250, 520)
  util.do_dash(1.2)

  util.move(550, 600)
  util.do_dash(1.2)

  util.move(350, 520)
  util.do_dash(1.2)

  util.move(350, 520)
  util.do_dash(1.2)

  util.move(350, 520)
  util.do_dash(1.2)

def position_final_boss():
  util.move(620, 650)
  util.do_dash(1.2)

  util.move(350, 620)
  util.do_dash(1.2)

  util.move(350, 560)
  util.do_dash(1.2)

  util.move(350, 560)
  util.do_dash(1.2)

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    util.set_reset_status(False)
    run_counter += 1
    util.log_action(util.MSG_START_DG)
    util.log_run(run_counter)

    # Click Cabal Window
    util.go_cabal_window()
    util.release_keys()
    util.go_skill_slot(0.5)
    util.do_buffs()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(500, 500)
    util.do_dash(1)
    util.move(500, 300)
    util.do_fade(0.5)

    util.move_click(570, 300)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    # First Boss
    util.move(570, 300)
    util.do_dash(1)

    util.attack_boss()
    util.set_battle_mode(False)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(400, 600)
    util.do_dash(1)

    try:
      util.move_click(570, 375)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    position_second_boss()
    util.move_click(670, 380, 0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(1000, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(1)

    util.focus_mobs(util.UNIT_ICE_BLOCK, 0)
    util.wait(2.5)

    util.move_click(450, 520, 1)

    util.move(450, 520)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(450, 520)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1000, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(1)

    util.move(530, 420)
    util.do_dash(0.5)
    util.wait(1)

    checking = True
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
         break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        checking = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)
        util.attack_mobs(util.UNIT_SPECTOR, 0, 0.3, val_sidestep)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.wait(1)
    util.attack_boss()
    util.cancel_aura(1)
    util.plunder_box(1, 3)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(730, 390)
    util.do_fade(1)

    dialog_check = True
    while dialog_check:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        dialog_check = False

      if dialog_check == False:
        break

      try:
        util.move_click(610, 300)
        util.move_click(610, 305)
        util.move_click(610, 310)
        util.move_click(700, 380)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 2)
        dialog_check = False
        break
      except pyauto.ImageNotFoundException:
        util.force_exit_dungeon()
        dialog_check = False
        util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Final Boss
    pre_position_final_boss()
    util.do_battle_mode(7)
    util.do_short_buffs()

    position_final_boss()
    util.attack_boss()
    util.plunder_box(1, 3)
    util.set_battle_mode(False)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(600, 600)
    util.do_dash(1.2)

    try:
      util.move_click(540, 435)
      util.move_click(540, 440)
      util.move_click(540, 445)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Start to End Dungeon
    util.check_notifications()
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
