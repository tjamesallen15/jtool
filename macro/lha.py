import time
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class LavaHellfireAwakened(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []
  val_sidestep = 0

  def initialize(self, frame, btn, runs):
    self.frame_root = frame
    self.btn_start = btn

    shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    self.run_dungeon(runs)

    self.btn_start.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def path_find_gate(self, unit=util.UNIT_BLANK):
    pathing = True
    gate_counter = 0
    path_counter = 0
    trigger_fade = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(util.MSG_PATH_FIND + unit)
      util.move_click(350, 250)
      util.move_click(450, 250)
      util.move_click(500, 250)
      util.move_click(550, 250)
      util.move_click(600, 250)
      util.move_click(650, 250)
      util.move_click(700, 250)

      try:
        util.do_select(0.1)
        gate_counter += 1
        path_counter += 1
        gate = pyauto.locateOnScreen(util.IMG_LAVA_GATE, grayscale=False, confidence=.8, region=util.get_full_region())

        if gate_counter >= 1:
          if trigger_fade == util.STATE_ZERO:
            util.move(720, 400)
            util.do_fade(0.1)
            trigger_fade = 1

          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
      except pyauto.ImageNotFoundException:
        if path_counter >= 10:
          util.move(720, 400)
          util.do_dash()
          util.do_fade()

  def position_fire_guard(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(620, 100)
    util.do_dash()
    util.do_fade()

    util.move(620, 100)
    util.do_dash()
    util.do_fade()

    util.move(750, 100)
    util.do_dash()
    util.do_fade()

    util.move(620, 100)
    util.do_dash()
    util.do_fade()

    util.move(800, 200)
    util.do_dash()

    util.move(640, 300)
    util.do_fade()

  def position_gate_keeper(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(850, 200)
    util.do_dash()
    util.do_fade()

    # util.move(700, 400)
    # util.do_fade()

    util.move(640, 200)
    util.do_dash()
    util.do_fade()

    util.move(650, 200)
    util.do_dash()
    util.do_fade()

    util.move(650, 200)
    util.do_dash()
    util.do_fade()

    util.move(350, 420)
    util.do_dash()

    util.move(250, 200)
    util.do_fade()
    util.do_dash()
    util.do_fade()

  def position_lava_gate(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(450, 300)
    util.do_dash()
    util.do_fade()

    if util.get_attack_type() == util.VAL_MELEE:
      util.do_dash()
      util.do_fade()
    else:
      util.do_dash(1.5)

    util.move(550, 100)
    util.do_dash()
    util.do_fade()

    util.move(550, 100)
    util.do_dash()
    util.do_fade()

    if util.get_attack_type() == util.VAL_MELEE:
      util.move(690, 200)
    else:
      util.move(670, 200)
    util.do_dash()
    util.do_fade()

  def position_boss(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(720, 400)
    util.do_fade(0.1)

    util.move_scroll(375, 150, 660, 150, 0.5)

    util.move(300, 420)
    util.do_dash()
    util.do_fade()

    util.move(550, 160)
    util.do_dash()
    util.do_fade()

    util.move(620, 280)
    util.do_dash()

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

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.do_final_mode(1)
      util.do_aura(2)
      util.click_portal(650, 260)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon(0.5)

      util.move_scroll(700, 150, 375, 150, 0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(620, 260)
      util.do_dash()
      util.move(580, 260)
      util.do_fade()

      # First Boss
      util.attack_boss()
      util.plunder_box(1, 3)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # First Semi Boss Sequence
      self.position_fire_guard()
      util.move(1000, 200)
      util.do_dash()
      util.do_fade()

      util.move(850, 200)
      util.do_dash()

      # First Semi Boss Sequence
      moving = True
      check_count = 0
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        if check_count == 10:
          util.move(500, 600)
          util.do_dash()

        if check_count >= 20:
          util.force_exit_dungeon()
          fail_run_counter += 1
          moving = False
          util.set_reset_status(True)

        if moving == False:
          break

        try:
          util.do_select(0.1)
          check_count += 1
          boss = pyauto.locateOnScreen(util.IMG_FIRE_GUARD, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(util.MSG_MOVE_STOP)
          moving = False
          util.attack_semi_boss(0)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

        time.sleep(0.2)

        if moving == False:
          break

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(850, 200)
      util.do_dash()

      util.move(750, 400)
      util.do_fade()

      # Second Semi Boss Sequence
      self.position_gate_keeper()
      moving = True
      check_count = 0
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        if check_count == 10:
          util.move(720, 500)
          util.do_dash()
          util.do_fade()

        if check_count >= 20:
          util.force_exit_dungeon()
          fail_run_counter += 1
          moving = False
          util.set_reset_status(True)

        if moving == False:
          break

        try:
          util.do_select(0.1)
          check_count += 1
          boss = pyauto.locateOnScreen(util.IMG_GATEKEEPER, grayscale=False, confidence=.7, region=util.get_full_region())
          moving = False
          util.attack_semi_boss(0)
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

        time.sleep(0.2)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Gate Sequence
      util.set_battle_mode(False)
      self.position_lava_gate()
      self.path_find_gate(util.UNIT_LAVA_GATE)
      util.focus_mobs(util.UNIT_LAVA_GATE, 0, 0, self.val_sidestep)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Boss Sequence
      util.do_battle_mode(5, False)
      self.position_boss()
      util.force_short_buffs()
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
      util.attack_boss(0, 0, 0, 0)

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.plunder_box(1, 3)
          checking = False
        except pyauto.ImageNotFoundException:
          pass

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
      util.log_time(2)
    util.do_close_app_status()
