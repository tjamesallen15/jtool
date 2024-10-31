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

class RadiantHall(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    # fail_run_counter = 0
    while run_counter < runs:
      util.set_reset_status(False)
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(consts.MSG_START_DG)
      util.log_run(run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.release_keys()
      util.go_skill_slot(0.2)
      util.do_buffs()

      util.move(800, 300)
      util.do_dash()

      # Click Dungeon
      self.click_dungeon_portal(700, 320)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()
      util.wait(2)

      util.move_scroll(620, 100, 620, 175, 0.8)

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      util.move(620, 300)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_EMPTY, False, sidestep=False)

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      atk.focus_gate()

      util.move(620, 250)
      util.do_dash(1.5)

      util.move(300, 200)
      util.do_dash(1.5)

      util.move(900, 200)
      util.do_dash()
      util.do_fade()

      checking = True
      dialog_count = 0
      util.move_click(750, 200)
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
          util.move_click_rel(10, 10, dialog, 0.2)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          checking = False

      checking = True
      dialog_count = 0
      util.move_click(500, 320)
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
          util.move_click_rel(10, 10, dialog, 0.2)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          checking = False

      util.move(100, 600)
      util.do_dash()
      util.do_fade()

      util.move(1000, 700)
      util.do_dash()
      util.do_fade()

      util.move(620, 600)
      util.do_dash()
      util.do_fade()

      util.move(100, 440)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(660, 300)
      util.do_fade()

      atk.focus_gate()

      util.move(620, 100)
      util.do_dash()

      util.move(800, 360)
      util.do_fade()

      util.move_click(750, 400)
      try:
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.2)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      util.move(350, 300)
      util.do_dash()

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        util.move_click(660, 270)
        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      util.move(100, 550)
      util.do_dash()
      util.do_fade()

      atk.focus_gate()

      util.move(100, 440)
      util.do_dash()
      util.do_fade(1.5)

      util.move(620, 300)
      util.do_fade()

      util.move_click(630, 320)
      try:
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.2)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      util.move_click(500, 320, 1)
      try:
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.2)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      util.move_click(770, 220, 1)
      try:
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.2)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      util.move_click(650, 320)
      try:
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.2)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      util.move(620, 600)
      util.do_dash(0.5)

      # First Boss
      util.wait(3)
      atk.attack_boss(True, False)
      atk.plunder_box()

      util.move(1020, 400)
      util.do_dash()
      util.do_fade()

      util.move(1020, 400)
      util.do_dash()
      util.do_fade()

      util.move_scroll(350, 150, 1000, 150, 0.8)

      util.move(530, 150)
      util.do_dash()
      util.do_fade()

      util.move(660, 200)
      util.do_dash()
      util.do_fade()

      util.move(640, 100)
      util.do_dash()
      util.do_fade()

      # FOUR BIRDS STATUE
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        util.move_click(680, 360)
        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      util.move(920, 440)
      util.do_fade()

      util.move(520, 100)
      util.do_dash()

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        util.move_click(570, 360)
        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      util.move(640, 600)
      util.do_dash()
      util.do_fade()

      util.move(300, 420)
      util.do_dash()
      util.wait(2)

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        util.move_click(700, 330)
        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.2)
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      util.move(600, 100)
      util.do_dash()

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

        if dialog_count == consts.STATE_ZERO:
          util.move_click(750, 360)

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.4)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      # FOUR BIRDS STATUE END
      util.move_scroll(1000, 150, 350, 150, 0.8)

      util.move(620, 100)
      util.do_dash()

      util.move(450, 100)
      util.do_fade()
      util.do_dash()

      util.move(620, 100)
      util.do_fade()
      util.do_dash()

      # Second Boss
      util.wait(1)
      atk.attack_boss(True, False)
      util.do_plunder(4)

      util.move(620, 100)
      util.do_dash()

      util.move(300, 200)
      util.do_fade()

      util.move(300, 350)
      util.do_dash()

      util.move(100, 400)
      util.do_fade()
      util.do_dash()

      util.move(200, 600)
      util.do_fade()
      util.do_dash()

      checking = True
      dialog_count = 0
      util.move_click(720, 420)
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
          util.move_click_rel(10, 10, dialog, 0.4)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          checking = False

      util.move(900, 300)
      util.do_dash()
      util.do_fade()

      util.move(900, 400)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move_scroll(1000, 150, 350, 150, 0.8)

      util.move(350, 150)
      util.do_dash()
      util.do_fade()

      util.move(620, 100)
      util.do_dash()

      util.move(100, 400)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(100, 400)
      util.do_dash()
      util.do_fade()

      util.move(400, 500)
      util.do_dash()

      util.move_scroll(350, 150, 1000, 150, 0.8)

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      util.move(400, 200)
      util.do_dash()

      util.move(900, 200)
      util.do_fade()
      util.do_dash()

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

        if dialog_count == consts.STATE_ZERO:
          util.move_click(700, 200)

        try:
          dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
          util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
          util.move_click_rel(10, 10, dialog, 0.4)
          dialog_count += 1
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)
          atk.focus_monsters(consts.UNIT_EMPTY, False, False, False)

      util.move(100, 700)
      util.do_dash()
      util.do_fade()

      util.move(1000, 700)
      util.do_dash()
      util.do_fade()

      util.move(530, 600)
      util.do_dash()

      util.move(620, 600)
      util.do_fade()

      util.move(100, 440)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move_scroll(350, 150, 1000, 150, 0.8)

      util.move(620, 100)
      util.do_dash()
      util.do_fade()

      util.move(800, 100)
      util.do_dash()
      util.do_fade()

      util.move(800, 100)
      util.do_dash()
      util.do_fade()

      util.move_scroll(350, 150, 800, 150, 0.8)

      util.move(400, 250)
      util.do_dash(1.5)

      util.move(630, 150)
      util.do_dash()

      util.move(520, 200)
      util.do_fade()

      util.move(350, 350)
      util.do_dash()

      run_counter += 1000
