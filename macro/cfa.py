import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput import keyboard
from tkinter import *
from pynput.keyboard import Key, Listener, Controller

from common.dungeon import Dungeon

import common.constants as consts
import common.util as util
import common.attack as atk

pynboard = Controller()

class CatacombsFrostAwakened(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    fail_run_counter = 0
    while run_counter < runs:
      util.set_reset_status(False)
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(consts.MSG_START_DG)
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

      util.move(500, 500)
      util.do_dash()

      # util.move_click(545, 300, 0.3)
      util.move(500, 300)
      util.do_fade()

      # Click Dungeon
      util.do_final_mode(1.2)
      util.do_aura(2)
      self.click_dungeon_portal(560, 330)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon(0.5)

      # First Boss
      util.move(570, 300)
      util.do_dash()

      atk.attack_boss(True, False)

      if util.get_attack_type() == consts.IS_MELEE: util.cancel_aura(1.2)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(400, 600)
      util.do_dash()

      try:
        util.move_click(570, 375)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.3)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
        util.force_exit_dungeon()
        fail_run_counter += 1
        util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      self.position_second_boss()
      util.move_click(670, 380, 0.5)
      util.move_scroll(375, 150, 1000, 150, 1)

      util.do_select(0.1)
      atk.focus_monsters(consts.UNIT_ICE_BLOCK, False, False, False)
      util.wait(1.5)

      util.move_click(450, 520, 1)

      util.move(450, 520)
      util.do_dash()
      util.do_fade()

      util.move(450, 520)
      util.do_dash()
      util.do_fade()

      if util.get_attack_type() == consts.IS_MELEE: util.move_scroll(1000, 150, 375, 150, 2)
      else: util.move_scroll(1000, 150, 375, 150, 0.2)
      util.move(530, 420)
      util.do_dash()

      # Check Spector is Available
      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + consts.UNIT_SPECTOR)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)
        util.force_exit_dungeon()
        fail_run_counter += 1
        util.set_reset_status(True)

      if util.get_reset_status():
        continue

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.do_select(0.1)
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOSS_FOUND)
          checking = False
          break
        except pyauto.ImageNotFoundException:
          pass

        try:
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          atk.attack_monsters(consts.UNIT_SPECTOR, False, 0.3, self.val_sidestep_disabled)
        except pyauto.ImageNotFoundException:
          pass

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      atk.attack_boss()
      util.cancel_aura(1.2)
      atk.plunder_box(True, 3)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(730, 390)
      util.do_fade(0.3)

      util.move(770, 470)
      util.do_fade(0.3)

      util.move(770, 480)
      util.do_fade(0.3)

      dialog_check = True
      while dialog_check:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          dialog_check = False

        if dialog_check == False:
          break

        try:
          util.move_click(720, 430)
          util.move_click(610, 300)
          util.move_click(610, 305)
          util.move_click(610, 310)
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.3)
          dialog_check = False
          break
        except pyauto.ImageNotFoundException:
          util.force_exit_dungeon()
          fail_run_counter += 1
          dialog_check = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Final Boss
      self.pre_position_final_boss()
      util.do_battle_mode(6, False)
      util.do_short_buffs()

      self.position_final_boss()
      atk.attack_boss(True, True, False, False)
      atk.plunder_box()
      util.set_battle_mode(False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.wait(1)
      util.move_click(600, 600, 1)

      try:
        util.move_click(540, 435)
        util.move_click(540, 440)
        util.move_click(540, 445)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.3)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
        util.force_exit_dungeon()
        fail_run_counter += 1
        util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time()
    util.do_close_app_status()

  def position_second_boss(self):
    util.log_action(consts.MSG_MOVING_POSITION)
    util.move(700, 350)
    util.do_fade()

    util.move(200, 320)
    util.do_dash()
    util.do_fade()

    util.move(300, 650)
    util.do_dash()
    util.do_fade()

    util.move(200, 350)
    util.do_dash()
    util.do_fade(1.2)

    util.move(620, 260)
    util.do_fade()

  def pre_position_final_boss(self):
    util.log_action(consts.MSG_MOVING_POSITION)
    util.move(250, 520)
    util.do_dash()

    util.move(550, 600)
    util.do_fade()

    util.move(350, 520)
    util.do_dash()

    util.move(350, 520)
    util.do_fade()

    util.move(350, 520)
    util.do_dash(0.5)

  def position_final_boss(self):
    util.log_action(consts.MSG_MOVING_POSITION)
    util.move(620, 650)
    util.do_dash()

    util.move(350, 620)
    util.do_fade()

    util.move(350, 560)
    util.do_dash()

    util.move(350, 560)
    util.do_fade()

    util.move(425, 560)
    util.do_dash(0.5)
