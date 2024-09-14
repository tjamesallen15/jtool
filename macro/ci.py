import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class ChaosInfinity(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
  val_sidestep = 0

  def initialize(self, frame, btn, runs):
    global frame_root
    frame_root = frame

    global btn_start
    btn_start = btn

    shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
    btn_start.config(state=util.STATE_DISABLED)
    frame_root.update()

    self.run_dungeon(runs)

    btn_start.config(state=util.STATE_NORMAL)
    frame_root.update()

  def reposition_center(self):
    # HORIZONTAL
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(100, 360)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1200, 400)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(900, 400)
    util.do_dash(1.5)

    # VERTICAL
    util.move(620, 100)
    util.do_dash(1.5)

    util.move(620, 600)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1.5)

    util.move(620, 100)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(0.5)

  def run_dungeon(self, runs):
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

      util.log_action(util.MSG_MOVING_POSITION)
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

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

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

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_select(0.1)
      util.focus_gate(util.UNIT_GATE, 0)

      util.move(620, 150)
      util.do_dash(1)
      util.do_fade(0.5)

      util.move(620, 150)
      util.do_dash(5)
      util.do_fade(0.5)

      util.move(620, 250)
      util.do_dash(3)

      util.move(620, 100)
      util.do_dash(2)

      util.move(620, 600)
      util.do_dash(1)
      util.do_fade(0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # 12 bosses
      bosses = 0
      arena = True
      mob_checker = 0
      while arena:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          arena = False

        if bosses >= 12:
          arena = False

        if arena == False:
          break

        mob_checker += 1
        util.do_select(0.1)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          util.attack_boss(0, 1)
          bosses += 1
          mob_checker = 0
          util.wait(0.2)
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

        try:
          boss = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          mob_checker = 0
          util.plunder_box(1, 3)
          if util.get_atk_type() == 1:
            util.wait(1)
          else:
            util.wait(5)
        except pyauto.ImageNotFoundException:
          pass

        try:
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ARENA_MOBS)
          mob_checker = 0
          util.focus_mobs(util.UNIT_ARENA_MOBS, 0, 1, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          pass

        if mob_checker >= 15:
          mob_checker = 0
          self.reposition_center()


      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.cancel_aura()

      # Start to End Dungeon
      util.check_notifications()
      util.end_dungeon()
      util.dice_dungeon()
      util.log_action(util.MSG_END_DG)
      util.log_time()
      util.wait(3)
