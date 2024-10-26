import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class PanicCaveAwakened(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
  val_sidestep = 0
  val_fade_speed = 0.5
  val_post_fade_speed = 0.45

  def initialize(self, frame, btn, runs):
    self.frame_root = frame
    self.btn_start = btn

    if util.get_access_level() == util.ACCESS_SUPER:
      self.val_fade_speed = 0.3
    else:
      self.val_fade_speed = 0.5

    shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    self.run_dungeon(runs)

    self.btn_start.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def position_nualle(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(610, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(610, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(610, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(610, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(560, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(610, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(680, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(640, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(570, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(770, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(640, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(500, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(570, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(500, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(640, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(680, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(640, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.move(660, 150)
    util.do_dash()
    util.do_fade(self.val_fade_speed)

    util.do_final_mode(2)
    util.do_aura(1)

    if util.get_attack_type() == util.STATE_ONE:
      util.move(610, 440)
      util.do_fade(1)

      util.move(680, 380)
      util.do_fade(1)
    else:
      util.wait(2)

  def position_first_shadow(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(460, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(640, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(820, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(750, 300)
    util.do_dash()

    util.move(600, 350)
    util.do_fade(self.val_post_fade_speed)

    util.move(620, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(580, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(580, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(580, 350)
    util.do_dash(1.5)

    util.move(770, 280)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(770, 280)
    util.do_dash()

    util.move(550, 370)
    util.do_fade(self.val_post_fade_speed)

  def position_second_shadow(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(720, 200)
    util.do_fade(1)

    util.move(720, 200)
    util.do_fade(self.val_post_fade_speed)

    util.move(780, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(730, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(760, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(670, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(620, 200)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

  def position_third_shadow(self):
    util.log_action(util.MSG_MOVING_POSITION)
    util.move(670, 230)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(690, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(690, 150)
    util.do_dash()
    util.do_fade(self.val_post_fade_speed)

    util.move(690, 150)
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
      util.click_portal(720, 360)

      # Enter Dungeon
      util.enter_dungeon(1.5)
      util.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      self.position_nualle()
      # First Boss Sequence
      util.force_short_buffs()
      util.attack_boss()

      if util.get_attack_type() == util.STATE_ONE:
        util.move(590, 460)
        util.do_fade()
      else:
        util.move_click(630, 325)
        util.wait(2)

      util.move_scroll(375, 150, 1000, 150)
      util.plunder_box(1, 2)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_attack_type() == util.STATE_ZERO:
        util.cancel_aura(1.2)
      util.move(1000, 520)
      util.do_dash()

      util.move_click(580, 440)
      corpse_found = False
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 3:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.3)
          corpse_found = True
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
          checking = False

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if corpse_found == False:
        util.move(630, 150)
        util.do_dash(1.5)

        util.move(670, 600)
        util.do_dash()

        util.move(660, 500)
        util.do_fade(self.val_fade_speed)

        util.move_click(580, 440)
        checking = True
        dialog_count = 0
        while checking:
          if not util.get_macro_state():
            util.log_action(util.MSG_TERMINATE)
            checking = False

          if checking == False:
            break

          if dialog_count == 3:
            checking = False
            break

          try:
            dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
            util.log_action(util.MSG_CHECK_DIALOG_FOUND)
            util.move_click_rel(10, 10, dialog, 0.3)
            corpse_found = True
            dialog_count += 1
          except pyauto.ImageNotFoundException:
            util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
            checking = False

      if corpse_found == util.IS_FALSE:
        try:
          timeout = pyauto.locateOnScreen(util.IMG_TIMEOUT, grayscale=False, confidence=.7, region=util.get_middle_region())
          timeout_exit = pyauto.locateOnScreen(util.IMG_TIMEOUT_EXIT, grayscale=False, confidence=.9, region=util.get_middle_region())
          util.move_click_rel(10, 10, timeout_exit, 0.2)
          util.wait(3)
        except pyauto.ImageNotFoundException:
          util.force_exit_dungeon()
        fail_run_counter += 1
        util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # First Shadow Sequence
      self.position_first_shadow()
      if util.get_attack_type() == util.STATE_ZERO:
        util.wait(8)
      else:
        util.wait(0.3)

      check_showorai = True
      count_showorai = 0
      util.log_action(util.MSG_CHECK_BOSS)
      while check_showorai:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_showorai = False

        if check_showorai == False:
          break

        if count_showorai > 10:
          check_showorai = False
          if util.get_attack_type() != util.VAL_RANGE:
            util.force_exit_dungeon()
            fail_run_counter += 1
            util.set_reset_status(True)

        try:
          util.do_select(0.1)
          util.log_action(util.MSG_CHECK_BOSS)
          mobs = pyauto.locateOnScreen(util.IMG_SHOWORAI, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(util.MSG_BOSS_FOUND)
          check_showorai = False
        except pyauto.ImageNotFoundException:
          count_showorai += 1
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # First Shadow
      util.focus_mobs(util.UNIT_SHOWORAI_F, 0, 0, 0)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Second Shadow Sequence
      self.position_second_shadow()
      if util.get_attack_type() == util.STATE_ZERO:
        util.wait(6)
      else:
        util.wait(0.3)

      check_showorai = True
      count_showorai = 0
      util.log_action(util.MSG_CHECK_BOSS)
      while check_showorai:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_showorai = False

        if check_showorai == False:
          break

        if count_showorai > 10:
          check_showorai = False
          if util.get_attack_type() != util.VAL_RANGE:
            util.force_exit_dungeon()
            fail_run_counter += 1
            util.set_reset_status(True)

        try:
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_SHOWORAI, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(util.MSG_BOSS_FOUND)
          check_showorai = False
        except pyauto.ImageNotFoundException:
          count_showorai += 1
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Second Shadow
      util.focus_mobs(util.UNIT_SHOWORAI_R, 0, 0, 0)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Third Shadow Sequence
      self.position_third_shadow()
      if util.get_attack_type() == util.STATE_ZERO:
        util.wait(5)
      else:
        util.wait(1)

      check_showorai = True
      count_showorai = 0
      util.log_action(util.MSG_CHECK_BOSS)
      while check_showorai:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_showorai = False

        if check_showorai == False:
          break

        if count_showorai > 20:
          util.force_exit_dungeon()
          fail_run_counter += 1
          check_showorai = False
          util.set_reset_status(True)

        try:
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_SHOWORAI, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(util.MSG_BOSS_FOUND)
          check_showorai = False
        except pyauto.ImageNotFoundException:
          count_showorai += 1
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Third Shadow
      util.focus_mobs(util.UNIT_SHOWORAI_M, 0, 0, 0)

      if util.get_attack_type() == util.STATE_ONE and util.get_battle_mode() == util.STATE_ONE:
        util.cancel_aura(1.5)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Final Boss Sequence
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.move_click(580, 430)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_full_region())
          util.focus_mobs(util.UNIT_GHOST, 0, 0, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        try:
          util.move_click(580, 430)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Final Boss
      util.move(620, 520)
      util.do_fade(self.val_fade_speed)
      util.do_battle_mode(5, False)

      check_count = 0
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False
          break

        if check_count > 3:
          checking = False

        if checking == False:
          break

        try:
          check_count += 1
          util.do_select(0.1)
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          checking = False
          util.log_action(util.MSG_BOSS_FOUND)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      util.attack_boss(0, 0, 0, 0)
      util.plunder_box(1, 2)

      util.move(650, 350)
      util.do_fade(0.5)

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.move_click(580, 430)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_full_region())
          util.do_select(0.1)
          util.focus_mobs(util.UNIT_GHOST, 0, 0, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        try:
          util.move_click(580, 430)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.move_click(580, 430)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
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
      util.log_time()
      util.set_battle_mode(False)
    util.do_close_app_status()
