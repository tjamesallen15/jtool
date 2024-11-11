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

class HazardousValleyVeradrix(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.set_reset_status(False)
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(consts.MSG_START_DG)
      util.log_run(run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.do_key_release()
      util.go_skill_slot(0.2)
      util.do_buffs()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.move(677, 361)
      util.move(735, 361, 0.5)
      self.click_dungeon_portal(735, 361)
      util.move_click(440, 300, 0.5)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()
      util.move_scroll(250, 150, 700, 150, 0.3)

      util.move(500, 300)
      if util.get_attack_type() == consts.IS_MELEE: util.do_dash(3.5)
      else: util.do_dash()
      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)

      util.move(375, 150)
      util.do_dash()
      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)

      if util.get_attack_type() == consts.IS_MELEE: util.do_dash(5.5)
      else: util.do_dash()
      util.do_fade()
      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)

      util.move(375, 175)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      if util.get_attack_type() == consts.IS_MELEE:
        util.move(375, 175)
        util.do_fade(1)

        util.move(250, 350)
        util.do_dash(3)
        util.do_fade(2)
      else:
        util.move(375, 175)
        util.do_fade()

        util.move(250, 350)
        util.do_dash()
        util.do_fade()
      util.do_final_mode(1)
      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)

      util.move(535, 150)
      util.do_dash()
      util.do_fade()
      util.move(400, 200)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)

      util.do_dash_rel(456, 156)
      util.do_fade_rel(416, 253)
      util.do_dash_rel(434, 333)

      atk.attack_monsters(consts.UNIT_CUTTER_TOAD, False, 0.3, self.val_sidestep_disabled)
      util.do_fade_rel(533, 327)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Cutter and Toad Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
            util.log_action(consts.MSG_TERMINATE)
            moving = False

        if moving == False:
          break

        self.path_find(consts.UNIT_CUTTER_TOAD)
        try:
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(consts.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.move(630, 520)
      util.do_fade()
      util.move(550, 250)
      util.do_dash(0.1)

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
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # First Boss
      atk.attack_boss()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(570, 260)
      util.do_fade()
      util.do_dash()

      atk.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      # Start to End Dungeon
      util.force_exit_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time()
    util.do_close_app_status()

  def path_find(self, unit):
    pathing = True
    boss_found = 0
    backtrack_counter = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(consts.MSG_PATH_FIND + unit)

      backtrack_counter += 1
      util.move_click(675, 450)
      util.log_action(consts.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 10):
        backtrack_counter = 0
        self.path_backtrack(unit)

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(consts.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(500, 260, 0.5)
        util.do_dash(0.5)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(consts.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      if unit == consts.UNIT_CUTTER_TOAD:
        try:
          util.move_click(450, 260)
          util.do_fade()
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(consts.MSG_CHECK_BOSS)
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        if pathing == False:
          break

      try:
        util.move_click(400, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(consts.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(300, 260)
        if unit == consts.UNIT_WHITE_SNAKE:
          util.do_dash()
          util.do_fade()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(consts.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      if unit == consts.UNIT_WHITE_SNAKE or unit == consts.UNIT_BOAR_SNAKE:
        try:
          util.move_click(200, 260)

          if unit == consts.UNIT_WHITE_SNAKE:
            util.do_dash()
            util.do_fade()

          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(consts.MSG_CHECK_BOSS)
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(100, 260)

          if unit == consts.UNIT_WHITE_SNAKE:
            util.do_dash()
            util.do_fade()

          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(consts.MSG_CHECK_BOSS)
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

        if pathing == False:
          break

    interval = 0.3
    if unit == consts.UNIT_CUTTER_TOAD:
      interval = 0.5

    if boss_found == consts.STATE_ZERO:
      atk.attack_monsters(unit, 1, interval)

  def path_backtrack(self, unit):
    backtracking = True
    backtrack_counter = 0
    while backtracking:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        backtracking = False

      if backtracking == False:
        break

      backtrack_counter += 1
      util.log_action(consts.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 10):
        backtrack_counter = 0
        backtracking = False

      util.log_action(consts.MSG_BACKTRACK + unit)

      try:
        util.move_click(650, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOX_FOUND)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOX_NOT_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(700, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOX_FOUND)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOX_NOT_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(750, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOX_FOUND)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOX_NOT_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(800, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOX_FOUND)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOX_NOT_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(850, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOX_FOUND)
        backtracking = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOX_NOT_FOUND)

      if backtracking == False:
        break

    atk.attack_backtrack(unit, True, True, False)
