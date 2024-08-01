import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import common.util as util
pynboard = Controller()

# GLOBAL VARIABLES
frame_root = []
btn_start = []

def initialize(frame, btn, runs=1):
  global frame_root
  frame_root = frame

  global btn_start
  btn_start = btn

  shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
  btn_start.config(state=util.STATE_DISABLED)
  frame_root.update()
  run_dungeon(runs)
  btn_start.config(state=util.STATE_NORMAL)
  frame_root.update()

def path_find_gate(unit=util.UNIT_BLANK):
  pathing = True
  gate_counter = 0
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)
    gate_counter += 1
    if gate_counter >= 12:
      try:
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_LAVA_GATE, grayscale=False, confidence=.8, region=util.get_full_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)
    else:
      util.move_click(350, 250)
      util.move_click(450, 250)
      util.move_click(500, 250)
      util.move_click(550, 250)
      util.move_click(600, 250)
      util.move_click(650, 250)
      util.move_click(700, 250)

def position_fire_guard():
  util.log_action(util.MSG_MOVING_POSITION)
  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(750, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(800, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(920, 200)
  util.do_dash(1)
  util.do_fade(0.5)

def position_gate_keeper():
  util.log_action(util.MSG_MOVING_POSITION)
  util.move(850, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(850, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(850, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(750, 420)
  util.do_fade(0.5)

  util.move(840, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(350, 420)
  util.do_dash(1)
  util.do_fade(0.5)

def position_lava_gate():
  util.log_action(util.MSG_MOVING_POSITION)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(250, 500)

  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(250, 500)

def position_boss():
  util.log_action(util.MSG_MOVING_POSITION)
  util.move(720, 400)
  util.do_fade(0.5)

  util.move(375, 150)
  pyauto.mouseDown(button="right")
  util.move(660, 150)
  pyauto.mouseUp(button="right")
  pyauto.scroll(-10000)

  util.wait(1)

  util.move(300, 420)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(300, 420)
  util.do_dash(1)
  util.do_fade(0.5)

  if util.get_atk_type() == 1:
    util.move(300, 420)
    util.do_dash(1)
    util.do_fade(0.5)

  util.move(480, 160)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(480, 160)
  util.do_dash(1)

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    util.set_reset_status(False)
    util.check_run_restart(run_counter)
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

    # Click Dungeon
    util.click_portal(650, 260)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()
    util.wait(1)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(620, 260)
    util.do_dash(0.5)

    # First Boss
    util.attack_boss()

    util.wait(1)
    util.move(580, 260)
    util.do_fade(0.5)
    util.plunder_box(1, 3)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # First Semi Boss Sequence
    position_fire_guard()
    util.wait(2)

    util.move(680, 400)
    util.do_fade(0.5)
    moving = True
    check_count = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if check_count >= 15:
        util.force_exit_dungeon()
        moving = False
        util.set_reset_status(True)

      if moving == False:
        break

      try:
        util.do_select(0.1)
        check_count += 1
        boss = pyauto.locateOnScreen(util.IMG_FIRE_GUARD, grayscale=False, confidence=.8, region=util.get_full_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      util.wait(0.2)

      if moving == False:
        break

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # First Semi Boss
    util.attack_semi_boss(0)

    # Second Semi Boss Sequence
    position_gate_keeper()
    util.wait(3)
    moving = True
    check_count = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if check_count >= 15:
        util.force_exit_dungeon()
        moving = False
        util.set_reset_status(True)

      if moving == False:
        break

      try:
        util.do_select(0.1)
        check_count += 1
        boss = pyauto.locateOnScreen(util.IMG_GATEKEEPER, grayscale=False, confidence=.8, region=util.get_full_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Second Semi Boss
    util.attack_semi_boss(0)
    util.set_battle_mode(False)

    # Gate Sequence
    position_lava_gate()
    path_find_gate(util.UNIT_LAVA_GATE)

    util.move(720, 400)
    util.do_fade(0.5)

    util.focus_mobs(util.UNIT_LAVA_GATE, 0, 0)
    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Boss Sequence
    util.do_battle_mode()

    position_boss()
    util.do_short_buffs()
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Final Boss
    util.attack_boss()
    util.plunder_box(1, 3)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.set_battle_mode(False)

    # Start to End Dungeon
    util.check_notifications()
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
