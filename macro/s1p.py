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

class SienaB1FPrideus(Dungeon):

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
      util.do_key_release()
      util.go_skill_slot(0.1)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.move(500, 610)
      util.do_dash(0.8)
      self.click_dungeon_portal(620, 380)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()
      util.do_buffs()

      util.move_scroll(375, 150, 500, 150, 0.8)
      util.move(660, 160)
      util.do_dash()
      util.do_fade()

      # First Sibling Dialog
      util.move_click(600, 380, 0.8)
      util.move_click(15, 525, 0.8)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 4:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      util.move_click(15, 535, 0.8)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move_click(490, 400, 1.5)

      util.do_final_mode(1)
      util.do_aura(3)
      util.move(660, 150)
      util.do_dash(1.5)
      util.move(660, 250)
      util.do_dash(0.5)

      # First Boss
      util.do_essentials()
      atk.attack_boss()
      util.set_battle_mode(False)
      util.do_essentials()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(580, 150)
      util.do_dash()
      util.do_fade()

      util.move(750, 300)
      util.do_dash(1.3)

      util.move(1000, 600)
      util.do_dash()
      util.do_fade()

      util.move(580, 600)
      util.do_dash()
      util.do_fade()

      util.move(580, 600)
      util.do_dash()
      util.do_fade()

      util.move(620, 600)
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(550, 175)
      util.do_fade()

      # Portal
      util.move_click(620, 250, 1.5)
      util.move_click(15, 535, 1)

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.move(660, 150)
      util.do_dash()
      util.do_fade()

      util.move(660, 150)
      util.do_dash()
      util.do_fade()

      # Second Sibling Dialog
      util.move_click(600, 380, 0.8)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 5:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(630, 600)
      util.do_dash()
      util.do_fade()

      util.move(640, 600)
      util.do_dash()
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.move(800, 250)
      util.do_dash()
      util.do_fade(3)

      # Box Dialog
      util.move_click(430, 340, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 4:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(750, 600)
      util.do_dash()
      util.do_fade()

      util.move(370, 600)
      util.do_dash()
      util.do_fade()

      util.move(720, 600)
      util.do_dash()
      util.do_fade()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(510, 150)
      util.do_dash()
      util.do_fade()

      util.move(800, 350)
      util.do_dash()
      util.do_fade()

      # Altar Dialog
      util.move_click(760, 450, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.move(400, 450)
      util.do_dash()

      # Second Sibling Sequence II
      util.move_click(575, 300, 1.5)
      util.move_click(600, 380, 0.8)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      util.move_click(15, 535, 0.8)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(600, 650)
      util.do_dash()
      util.do_fade()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(640, 150)
      util.do_dash()
      util.do_fade()

      util.move(200, 400)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move(700, 250)
      util.do_dash()
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(400, 150)
      util.do_dash()
      util.do_fade()

      util.move(820, 250)
      util.do_dash()
      util.do_fade()

      util.do_final_mode(1)
      util.do_aura(3)
      util.do_short_buffs()

      util.move(640, 150)
      util.do_dash()
      util.do_fade()

      util.move(640, 150)
      util.do_dash()

      # Second Boss
      util.do_essentials()
      atk.attack_boss()
      util.do_essentials()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(330, 300)
      util.do_dash(1.3)

      util.move(660, 150)
      util.do_dash()
      util.do_fade()

      util.move(1000, 250)
      util.do_dash()
      util.do_fade()

      util.move(1200, 460)
      util.do_dash()
      util.do_fade()

      util.move(600, 600)
      util.do_dash()
      util.do_fade()

      util.move(600, 600)
      util.do_dash()
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(1200, 350)
      util.do_dash()
      util.do_fade()

      util.move(900, 350)
      util.do_dash(1.5)

      util.move(600, 275)
      util.do_dash()
      util.do_fade()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(500, 150)
      util.do_dash()
      util.do_fade()

      util.move(800, 250)
      util.do_dash(1.5)

      util.move(80, 350)
      util.do_dash()

      util.move(500, 300)
      util.do_fade()
      util.do_dash(1.5)

      util.move(770, 300)
      util.do_dash()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(650, 150)
      util.do_dash()
      util.do_fade()

      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      util.move(680, 150)
      util.do_dash()

      # Third Sibling
      util.move_click(705, 390, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 5:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      if util.get_reset_status():
        continue

      util.move_click(15, 535, 0.8)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(700, 550)
      util.do_dash()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(700, 150)
      util.do_dash()
      util.do_fade()

      util.move(700, 150)
      util.do_dash()

      # Third Boss
      util.do_essentials()
      atk.attack_boss()
      util.set_battle_mode(False)
      util.do_essentials()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(720, 150)
      util.do_dash()
      util.do_fade()

      util.move(670, 150)
      util.do_dash()
      util.do_fade()

      util.move(100, 350)
      util.do_dash()
      util.do_fade(2)

      # Egg Dialog
      util.move_click(360, 350, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 2:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(700, 160)
      util.do_dash()
      util.do_fade()

      util.move(700, 160)
      util.do_dash()
      util.do_fade()

      util.move(700, 160)
      util.do_dash()
      util.do_fade()

      util.move(700, 160)
      util.do_dash()
      util.do_fade()

      util.move(700, 160)
      util.do_dash()
      util.do_fade()

      # Wall Dialog
      util.move_click(1100, 400, 2)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(350, 400)
      util.do_dash(1.3)

      util.move(575, 600)
      util.do_dash()
      util.do_fade()

      util.move(575, 600)
      util.do_dash()
      util.do_fade()

      util.move(575, 600)
      util.do_dash()
      util.do_fade()

      util.move(575, 600)
      util.do_dash()
      util.do_fade(1.5)

      util.move(575, 600)
      util.do_fade()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(700, 150)
      util.do_dash()
      util.do_fade()

      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      # Fire Dialog
      util.move_click(570, 320, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(680, 625)
      util.do_dash()
      util.do_fade()

      util.move(630, 625)
      util.do_dash()
      util.do_fade()

      util.move(350, 625)
      util.do_dash()

      util.move(850, 625)
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(620, 625)
      util.do_dash()
      util.do_fade()

      util.move(400, 625)
      util.do_dash()

      util.move(750, 625)
      util.do_fade()

      # Egg Dialog II
      util.move_click(360, 450, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 3:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(800, 150)
      util.do_dash(1.3)

      util.move(520, 200)
      util.do_dash(1.3)

      util.move_scroll(700, 150, 375, 150, 0.8)
      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      # Four Altars Dialog
      util.move_click(520, 300, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_click(900, 330, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_click(420, 260, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_click(900, 320, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)
      util.move_click(15, 535, 1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Twin Boss Sequence (Fourth and Fifth Boss)
      util.move(580, 150)
      util.do_dash(1.5)

      util.move(640, 250)
      util.do_dash(1.5)

      util.move(270, 400)
      util.do_dash()

      util.do_essentials()
      atk.attack_boss()

      util.wait(1)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(1000, 150)
      util.do_dash()
      util.do_fade()

      util.do_essentials()
      atk.attack_boss()
      util.set_battle_mode(False)
      util.do_essentials()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(820, 150)
      util.do_dash()
      util.do_fade()

      # Portal II
      util.move_click(420, 450, 1.5)
      util.move_click(500, 500, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move_scroll(375, 150, 1000, 150, 0.8)

      util.move(100, 350)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.8)
      util.move(250, 150)
      util.do_dash()
      util.do_fade(1.3)

      util.move(750, 150)
      util.do_fade()

      # Umpra The Weak Sequence
      util.log_action(consts.MSG_CHECK_UMPRA_WEAK)
      checking = True
      count_umpra = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if count_umpra > 10:
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

        try:
          util.do_select(0.1)
          umpra = pyauto.locateOnScreen(consts.IMG_UMPRA_WEAK, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(consts.MSG_UMPRA_WEAK_FOUND)
          atk.focus_monsters(consts.UNIT_UMPRA_WEAK, False, False, self.val_sidestep_disabled)
          checking = False
        except pyauto.ImageNotFoundException:
          count_umpra += 1
          util.log_action(consts.MSG_UMPRA_WEAK_NOT_FOUND)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.wait(1)
      util.do_plunder(10)

      util.move(750, 150)
      util.do_dash(1.5)

      # Altar Dialog
      util.move_click(700, 300, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == 3:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
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

      # Going to the Siena Secret Room
      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(200, 425)
      util.do_dash()
      util.do_fade()

      util.move(620, 625)
      util.do_dash()
      util.do_fade()

      util.move(100, 350)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move(500, 150)
      util.do_dash()
      util.do_fade()

      util.move_click(500, 300, 1.5)
      checking = True
      dialog_count = 0
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        if dialog_count == consts.STATE_ONE:
          checking = False
          break

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.5)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          util.force_exit_dungeon()
          fail_run_counter += 1
          checking = False
          util.set_reset_status(True)

      # Siena Box Sequence
      util.log_action(consts.MSG_CHECK_SIENA_BOX)
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.do_select(0.1)
          siena = pyauto.locateOnScreen(consts.IMG_SIENA, grayscale=False, confidence=.8, region=util.get_full_region())
          util.log_action(consts.MSG_SIENA_BOX_FOUND)
          util.wait(1)
          atk.plunder_ref_box(False, 10, consts.IMG_SIENA)
          checking = False
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_SIENA_BOX_NOT_FOUND)

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.force_exit_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time()
    util.do_close_app_status()
