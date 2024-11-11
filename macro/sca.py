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

class SteamerCrazyAwakened(Dungeon):

  # UNIQUE VARIABLES
  portal_counter = 0

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      self.portal_counter = 0
      util.log_action(consts.MSG_START_DG)
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

      util.move_scroll(375, 150, 700, 150)

      # Click Dungeon
      self.click_dungeon_portal(600, 250)

      # Enter Dungeon
      self.enter_dungeon(0.3)
      self.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Mechape Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(consts.UNIT_MECHAPE)
        try:
          boss = pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(consts.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # First Boss
      util.do_short_buffs()
      atk.attack_semi_boss(True, True, False, False)
      atk.plunder_box(True, 0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(630, 250)
      util.do_dash()
      util.do_fade()

      util.do_dash()
      util.do_fade()

      util.do_dash()
      util.do_fade()

      util.do_dash(0.1)

      # Tricus Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(consts.UNIT_TRICUS)
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

      # Final Boss
      atk.attack_boss(consts.UNIT_EMPTY, True, False, False, False)
      util.do_plunder(1)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      atk.plunder_box(True, 0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(1)
    util.do_close_app_status()

  def path_find(self, unit):
    pathing = True
    boss_found = 0
    mobs_found = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(consts.MSG_PATH_FIND + unit)
      util.move_click(620, 460)

      try:
        util.move_click(630, 250)
        if self.portal_counter % 2 == consts.STATE_ZERO:
          util.do_dash()
          util.do_fade(0.1)

        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(620, 250)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        self.portal_counter += 1
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)

        if self.portal_counter % 2 == consts.STATE_ZERO:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade(0.1)
        elif self.portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.cancel_aura(1.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade()

          util.do_dash()
          util.do_fade(0.1)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 400)
          util.do_fade(2)
          util.do_final_mode(1)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(600, 250)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(600, 250)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        self.portal_counter += 1
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)

        if self.portal_counter % 2 == consts.STATE_ZERO:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade(0.1)
        elif self.portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.cancel_aura(1.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade()

          util.do_dash()
          util.do_fade(0.1)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 400)
          util.do_fade(2)
          util.do_final_mode(1)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(650, 250)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(650, 250)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        self.portal_counter += 1
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)

        if self.portal_counter % 2 == consts.STATE_ZERO:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade(0.1)
        elif self.portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.cancel_aura(1.5)
          util.move(630, 250)
          util.do_dash()
          util.do_fade()

          util.do_dash()
          util.do_fade(0.1)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 400)
          util.do_fade(2)
          util.do_final_mode(1)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_DIALOG_NOT_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

    if boss_found == consts.STATE_ZERO and mobs_found == consts.STATE_ONE:
      atk.attack_monsters(unit, True, consts.VAL_INTERVAL_DEFAULT, self.val_sidestep_disabled)

      util.move(630, 250)
      util.do_dash()
      util.do_fade()

      util.do_dash()
      util.do_fade()

      util.do_dash()
      util.do_fade(0.1)
