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

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
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

  def reposition_ulwaan(self):
    # HORIZONTAL
    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()
    util.do_select(0.1)

    # HORIZONTAL
    util.move(1200, 400)
    util.do_dash()
    util.do_fade()

    util.move(875, 400)
    util.do_dash(1.5)
    util.do_select(0.1)

  def reposition_mobs(self):
    # VERTICAL CHECK
    util.move(620, 100)
    util.do_dash()
    util.do_fade()
    util.do_select(0.1)

    util.move(620, 600)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()
    util.do_select(0.1)

    util.move(620, 250)
    util.do_dash()

    util.move(620, 300)
    util.do_fade()

  def chaos_reposition_top(self):
    util.move(620, 100)
    util.do_dash()
    util.do_fade()

  def chaos_reposition_bottom(self):
    util.move(620, 600)
    util.do_dash()
    util.do_fade()

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
      util.do_dash()
      util.do_fade()

      util.move(620, 325)
      util.do_dash()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # 12 bosses
      bosses = 0
      arena = True
      mob_checker = 0
      chaos_move = 0
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
        util.do_fast_plunder()

        try:
          chaos_gate = pyauto.locateOnScreen(util.IMG_CHAOS_GATE, grayscale=False, confidence=.7, region=util.get_full_region())

          if chaos_move == 0:
            util.do_deselect_pack()
            self.chaos_reposition_top()
            chaos_move = 1
          else:
            util.do_deselect_pack()
            self.chaos_reposition_bottom()
            chaos_move = 0

        except pyauto.ImageNotFoundException:
          pass

        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          util.attack_boss(0, 1)
          bosses += 1
          mob_checker = 0
          reposition_count = 0
          chaos_move = 0
          util.wait(0.2)
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        try:
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          mob_checker = 0
          reposition_count = 0
          chaos_move = 0
          util.plunder_box(1, 3, 1, 0)

          if util.get_member_status() == 0:
            util.wait(1.5)

        except pyauto.ImageNotFoundException:
          pass

        try:
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ARENA_MOBS)
          mob_checker = 0

          if util.get_attack_type() == 1:
            util.do_attack(0.1)
          else:
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
          util.cancel_aura(1.2)

          if reposition_count > 2:
            self.reposition_center()

          if bosses == 10 and reposition_count < 2:
            self.reposition_ulwaan()
          else:
            self.reposition_mobs()
          reposition_count += 1

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Start to End Dungeon
      util.reset_battle_mode()
      util.check_notifications()
      util.end_dungeon()
      util.dice_dungeon()
      util.log_action(util.MSG_END_DG)
      util.log_time()
