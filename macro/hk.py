import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class HolyKeldrasil(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
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

  def find_mobs(self, unit=util.UNIT_BLANK):
    finding = True
    find_count = 0
    while finding:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        finding = False

      if finding == False:
          break

      util.do_select(0.1)
      match unit:
        case util.UNIT_HUMMING_BIRD:
          try:
            boss = pyauto.locateOnScreen(util.IMG_AREIHORN, grayscale=False, confidence=.6, region=util.get_full_region())
            util.log_action(util.MSG_BOSS_FOUND)
            find_count += 35
            finding = False
            break
          except pyauto.ImageNotFoundException:
            find_count += 1
        case util.UNIT_HATCHLING:
          try:
            boss = pyauto.locateOnScreen(util.IMG_PHIXIA, grayscale=False, confidence=.7, region=util.get_full_region())
            util.log_action(util.MSG_BOSS_FOUND)
            find_count += 35
            finding = False
            break
          except pyauto.ImageNotFoundException:
            find_count += 1
        case util.UNIT_OWL_BEAR:
          try:
            boss = pyauto.locateOnScreen(util.IMG_VAOUR, grayscale=False, confidence=.6, region=util.get_full_region())
            util.log_action(util.MSG_BOSS_FOUND)
            find_count += 35
            finding = False
            break
          except pyauto.ImageNotFoundException:
            find_count += 1

      if find_count >= 30:
        finding = False

      if finding == False:
        break

      try:
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.8, region=util.get_full_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        util.focus_mobs(unit, 0, 1, self.val_sidestep)
      except pyauto.ImageNotFoundException:
        util.do_deselect_pack()
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
      util.release_keys(1)
      util.go_skill_slot(0.2)
      util.do_buffs()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.move(400, 500)
      util.do_dash(0.8)
      util.click_portal(590, 400)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Position First Sequence
      util.move_scroll(375, 150, 700, 150)

      util.move(500, 150)
      util.do_dash()
      util.do_fade()

      util.move(500, 150)
      util.do_dash()
      util.do_fade()

      util.wait(1)

      util.move(500, 150)
      util.do_dash()
      util.do_fade()

      util.wait(3)

      util.move(500, 150)
      util.do_dash()
      util.do_fade()
      util.move_scroll(375, 150, 700, 150)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack First Boss
      util.wait(7)
      self.find_mobs(util.UNIT_HUMMING_BIRD)
      try:
        boss = pyauto.locateOnScreen(util.IMG_AREIHORN, grayscale=False, confidence=.6, region=util.get_full_region())
        # Attack First Boss
        util.focus_mob_boss(util.UNIT_AREIHORN, 0, 1, 0, 0)
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_attack_type() == util.STATE_ONE:
        util.move(420, 150)
        util.do_dash()
        util.do_fade()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Going to Portal
      util.move(420, 150)
      util.do_dash()
      util.do_fade()

      util.move(420, 150)
      util.do_dash()
      util.do_fade()

      check_dialog = True
      while check_dialog:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_dialog = False

        if check_dialog == False:
          break

        try:
          util.move_click(600, 320)
          util.move_click(550, 320)
          util.wait(0.2)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 2)
          check_dialog = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          check_dialog = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(375, 150, 1000, 150)

      # Attack Second Group
      util.move(300, 250)
      util.do_dash()
      util.wait(4)

      util.move(900, 400)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == util.VAL_MELEE: util.wait(4)
      else: util.wait(1)

      self.find_mobs(util.UNIT_HATCHLING)
      try:
        boss = pyauto.locateOnScreen(util.IMG_PHIXIA, grayscale=False, confidence=.7, region=util.get_full_region())
        # Attack Second Boss
        util.do_battle_mode()
        util.focus_mob_boss(util.UNIT_PHIXIA, 0, 1, 0, 0)
        util.set_battle_mode(False)
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_BOSS_NOT_FOUND)

      util.move(525, 400)
      util.do_fade()

      if util.get_attack_type() == util.STATE_ONE:
        util.move(500, 400)
        util.do_dash(1.5)

      util.move(550, 150)
      util.do_dash()

      util.move(550, 250)
      util.do_fade()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Going to Portal
      util.move(540, 150)
      util.do_dash()
      util.do_fade()

      util.move(540, 150)
      util.do_dash()
      util.do_fade()

      check_dialog = True
      while check_dialog:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_dialog = False

        if check_dialog == False:
          break

        try:
          util.move_click(600, 320)
          util.move_click(550, 320)
          util.wait(0.2)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 2)
          check_dialog = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          check_dialog = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      util.wait(0.5)
      util.move_scroll(375, 150, 850, 150)

      # Third Group Sequence
      util.wait(9)
      util.move(630, 320)
      util.do_dash()
      self.find_mobs(util.UNIT_OWL_BEAR)

      util.do_deselect_pack()
      util.move(620, 550)
      util.do_dash(0.5)

      select_counter = 0
      selecting = True
      vaour_found = False
      while selecting:

        if select_counter > 2:
          selecting = False
          break

        if selecting == False:
          break

        select_counter += 1
        try:
          util.do_select(0.1)
          boss = pyauto.locateOnScreen(util.IMG_VAOUR, grayscale=False, confidence=.7, region=util.get_full_region())
          selecting = False
          vaour_found = True
          break
        except pyauto.ImageNotFoundException:
          pass

      if vaour_found == False:
        util.log_action(util.MSG_BOSS_NOT_FOUND)
        util.force_exit_dungeon()
        fail_run_counter += 1
        util.set_reset_status(True)
      else:
        # Attack Third Boss
        util.focus_mob_boss(util.UNIT_VAOUR, 0, 1, 0, 0)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(570, 150)
      util.do_dash()
      util.do_fade()

      util.move(570, 250)
      util.do_dash()
      util.do_fade()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Going to Portal
      util.log_action(util.MSG_MOVING_POSITION)
      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      check_dialog = True
      while check_dialog:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_dialog = False

        if check_dialog == False:
          break

        try:
          util.move_click(600, 320)
          util.move_click(550, 320)
          util.wait(0.2)
          dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(util.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 2)
          check_dialog = False
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          check_dialog = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(375, 150, 935, 150, 0.8)

      # Position Last Sequence
      util.log_action(util.MSG_MOVING_POSITION)
      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.do_select(0.1)
      util.focus_mobs(util.UNIT_GATE_FOUR, 0, 0, self.val_sidestep)
      util.wait(2)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(util.MSG_MOVING_POSITION)
      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      # Attack Fourth Group
      if util.get_attack_type() == util.VAL_MELEE: util.wait(9)
      else: util.wait(6)

      util.move(620, 600)
      util.attack_mobs(util.UNIT_KNIGHT, 1, 0.3, 0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_battle_mode()
      util.do_short_buffs()
      util.wait(0.3)

      util.log_action(util.MSG_MOVING_POSITION)
      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      # Attack Final Boss
      util.focus_mob_boss(util.UNIT_SHIRDRAHN, 1, 1, 0, 0)
      util.plunder_final_box()
      util.set_battle_mode(False)

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
    util.do_close_app_status()
