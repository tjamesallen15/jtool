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
    util.log_action(util.MSG_MOVING_POSITION)
    # HORIZONTAL
    util.move(100, 400)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    # VERTICAL
    util.move(620, 100)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    util.move(620, 600)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    # HORIZONTAL
    util.move(1200, 400)
    util.do_dash()
    util.do_fade()

    util.move(900, 400)
    util.do_dash(1.5)

  def reposition_mobs(self):
    # VERTICAL CHECK
    util.move(620, 100)
    util.do_dash()
    util.do_fade()

    util.move(620, 600)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    util.move(620, 500)
    util.do_dash()

    util.move(620, 100)
    util.do_fade()
    util.do_dash()

    util.move(620, 350)
    util.do_fade()

    util.wait(2)

  def run_dungeon(self, runs):
    run_counter = 0
    fail_run_counter = 0
    while run_counter < runs:
      util.set_reset_status(False)
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(util.MSG_START_DG)
      util.log_run(run_counter, fail_run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.release_keys()
      util.go_skill_slot(0.2)
      util.do_buffs()

      util.move(500, 300)
      util.do_dash()

      # Click Dungeon
      util.click_portal(590, 390)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150, 0.5)

      util.log_action(util.MSG_MOVING_POSITION)
      util.move(650, 250)
      util.do_dash()

      util.move(500, 360)
      util.do_fade()

      util.move(500, 360)
      util.do_dash()

      util.move(750, 150)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(550, 300)
      util.do_dash()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      has_gate = True
      while has_gate:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          has_gate = False

        if has_gate == False:
          break

        util.do_select(0.1)

        if util.get_member_status() == 0:
          try:
            gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
            util.focus_gate(util.UNIT_GATE, 0)
            util.wait(0.3)
            has_gate = False
            break
          except pyauto.ImageNotFoundException:
            pass
        else:
          try:
            gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          except pyauto.ImageNotFoundException:
            util.wait(2)
            has_gate = False
            break

      util.move(620, 150)
      util.do_dash()
      util.do_fade(6)

      util.move(620, 150)
      util.do_dash(1.5)
      util.do_fade()

      util.move(620, 250)
      util.do_dash(1.5)

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      util.move(620, 600)
      util.do_dash()
      util.do_fade(1.5)
      util.do_fade()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # 12 bosses
      bosses = 0
      arena = True
      mob_checker = 0
      reposition_count = 0
      while arena:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          arena = False

        if bosses >= 12:
          arena = False

        if reposition_count > 3:
          util.force_exit_dungeon()
          fail_run_counter += 1
          arena = False
          util.set_reset_status(True)

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
          reposition_count = 0
          util.wait(0.2)
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

        try:
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          mob_checker = 0
          reposition_count = 0
          util.plunder_box(1, 3)
          util.wait(1)
        except pyauto.ImageNotFoundException:
          pass

        try:
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ARENA_MOBS)
          mob_checker = 0
          util.focus_mobs(util.UNIT_ARENA_MOBS, 0, 1, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          pass

        try:
          end_dungeon = pyauto.locateOnScreen(util.IMG_END_DG, grayscale=False, confidence=.9)
          bosses += 12
        except pyauto.ImageNotFoundException:
          pass

        if mob_checker >= 30:
          mob_checker = 0
          util.cancel_aura(2)

          if reposition_count > 2:
            self.reposition_center()

          self.reposition_mobs()
          reposition_count += 1

      util.cancel_aura()

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
      util.log_time()
      util.wait(2)
