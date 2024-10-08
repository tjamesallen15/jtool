import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class HazardousValleyAwakened(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  def initialize(self, frame, btn, runs):
    self.frame_root = frame
    self.btn_start = btn

    shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    self.run_dungeon(runs)

    self.btn_start.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def path_find(self, unit):
    pathing = True
    boss_found = 0
    backtrack_counter = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(util.MSG_PATH_FIND + unit)

      backtrack_counter += 1
      util.move_click(675, 450)
      util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 10):
        backtrack_counter = 0
        self.path_backtrack(unit)

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(500, 260, 0.5)
        util.do_dash(0.5)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      if unit == util.UNIT_MOSS_TOAD:
        try:
          util.move_click(475, 260)
          util.do_fade()
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(util.MSG_CHECK_BOSS)
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(450, 260)
          util.do_fade()
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(util.MSG_CHECK_BOSS)
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        if pathing == False:
          break

      try:
        util.move_click(400, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(300, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(200, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      if unit == util.UNIT_LUMBER_DORIGO:
        try:
          util.move_click(200, 360)
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        try:
          util.do_select(0.1)
          util.log_action(util.MSG_CHECK_BOSS)
          mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          pathing = False
          boss_found = 1
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_MOBS_FOUND)

        if pathing == False:
          break

    if boss_found == util.STATE_ZERO:
      util.attack_mobs(unit)

  def path_backtrack(self, unit):
    backtracking = True
    boss_found = 0
    backtrack_counter = 0
    while backtracking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        backtracking = False

      if backtracking == False:
        break

      backtrack_counter += 1
      util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 20):
        backtrack_counter = 0
        backtracking = False

      util.log_action(util.MSG_BACKTRACK + unit)
      try:
        util.move_click(650, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        backtracking = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(700, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        backtracking = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(750, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        backtracking = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(800, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        backtracking = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if backtracking == False:
        break

      try:
        util.move_click(850, 560)
        util.do_dash()
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        backtracking = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if backtracking == False:
        break

    util.attack_mobs(unit)

  def position_orphidia(self):
    util.do_deselect_pack()
    util.move(400, 260)
    util.do_dash()
    util.do_fade()

    util.do_deselect_pack()
    util.move(320, 540)
    util.do_dash()

    util.do_deselect_pack()
    util.move(400, 260)
    util.do_dash()
    util.do_fade()

    util.do_deselect_pack()
    util.move(320, 540)
    util.do_dash()

    util.move(400, 400)
    util.do_fade()

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(util.MSG_START_DG)
      util.log_run(run_counter)

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
      util.move(677, 361)
      util.move(735, 361, 0.5)
      util.click_portal(735, 361)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon()
      util.move_scroll(250, 150, 700, 150)

      # Initial Position
      util.move(850, 600)
      util.do_dash(0.1)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Mush and Flower Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_MUSH_FLOWER)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.move(700, 600)
      util.do_dash(0.1)
      util.do_fade()

      util.move(700, 600)
      util.do_dash(0.1)
      util.do_fade()

      # First Boss
      util.do_short_buffs()

      util.attack_boss()
      util.move(450, 550)
      util.do_fade()

      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_click(400, 260)
      util.do_dash(0.5)

      # Mossite and Toad Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_MOSS_TOAD)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Second Boss
      util.do_deselect_pack()
      util.move(800, 360)
      util.do_dash()
      util.move(500, 300)
      util.do_fade(0.1)

      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        if checking == False:
          break

        try:
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          checking = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Second Boss Cont
      util.attack_boss()
      util.do_deselect_pack()
      util.move(500, 100)
      util.do_fade()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Lumber and Dorigo Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_LUMBER_DORIGO)
        try:
          mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Position for First Orphidia
      util.do_deselect_pack()
      self.position_orphidia()

      # First Orphidia
      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.attack_boss()
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.wait(1)
      util.move(675, 600)
      util.do_dash(0.5)
      util.do_battle_mode()

      # Second and Third Orphidia
      boss_tracker = 0
      boss_count = 0
      short_buffs_counter = 0
      while boss_count < 2:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          boss_count += 10

        if boss_count > 2:
          break

        if (boss_count == util.STATE_ONE and short_buffs_counter == util.STATE_ZERO and util.is_short_buffs_allowed == util.STATE_ONE):
          short_buffs_counter = 1
          util.do_short_buffs()

        try:
          util.do_select(0.1)
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
          boss_count += 1
          util.attack_boss(0, 1)
          util.do_deselect_pack()
          util.wait(5)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Pathfind Treasure Boxes
      util.check_notifications()
      boxing = True
      while boxing:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          boxing = False

        if boxing == False:
          break

        util.log_action(util.MSG_PATH_FIND + util.UNIT_BOX)
        util.move_click(550, 160)
        util.wait(1)

        util.do_dash(0.5)
        util.move_click(650, 160, 0.3)
        util.move_click(750, 160, 0.3)
        util.move_click(850, 160, 0.3)
        util.move_click(950, 160, 0.3)
        util.move_click(950, 480)
        util.do_dash()
        util.do_fade()

        try:
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          boxing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Loot Treasure Boxes
      plundering = True
      while plundering:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          plundering = False

        if plundering == False:
          break

        try:
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          util.log_action(util.MSG_PATH_STOP)
          util.plunder_final_box(0)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

        try:
          checkenddg = pyauto.locateOnScreen(util.IMG_END_DG, grayscale=False, confidence=.9)
          plundering = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_CHECK_END_DG)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      # Start to End Dungeon
      util.check_notifications()
      util.end_dungeon()
      util.dice_dungeon()
      util.log_action(util.MSG_END_DG)
      util.log_time()
