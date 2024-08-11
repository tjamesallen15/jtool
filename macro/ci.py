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

# UNIQUE VARIABLES
val_sidestep = 0

def initialize(frame, btn, runs):
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

def run_dungeon(runs):
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

    util.move(500, 300)
    util.do_dash(1)

    # Click Dungeon
    util.click_portal(580, 400)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.5)

    util.move(650, 250)
    util.do_dash(1)

    util.move(500, 360)
    util.do_fade(0.5)

    util.move(500, 360)
    util.do_dash(1)

    util.move(750, 150)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(550, 300)
    util.do_dash(1)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.5)

    util.move(600, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_select(0.1)
    util.focus_gate(util.UNIT_GATE, 0)
    util.wait(1)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(3)
    util.do_fade(0.5)

    util.move(620, 250)
    util.do_dash(3)

    # 12 bosses
    bosses = 0
    arena = True
    while arena:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        pathing = False

      if bosses >= 12:
        arena = False

      if arena == False:
        break

      util.do_select(0.1)
      try:
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        util.attack_boss(0, 1)
        bosses += 1
        util.wait(3)
        util.do_select(0.1)
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      try:
        boss = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOX_FOUND)
        util.plunder_box(1, 3)
        util.wait(5)
      except pyauto.ImageNotFoundException:
        pass

      try:
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ARENA_MOBS)
        util.focus_mobs(util.UNIT_ARENA_MOBS, 0, 1, val_sidestep)
      except pyauto.ImageNotFoundException:
        pass

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.cancel_aura(2)

    # Start to End Dungeon
    util.check_notifications()
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
