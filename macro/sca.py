import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class SteamerCrazyAwakened(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []
  portal_counter = 0
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

  def path_find(self, unit):
    global portal_counter
    pathing = True
    boss_found = 0
    mobs_found = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(util.MSG_PATH_FIND + unit)
      util.move_click(620, 460)

      try:
        util.move_click(630, 250)
        if portal_counter % 2 == 0:
          util.do_dash(0.1)

        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(620, 250)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        portal_counter += 1
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)

        if portal_counter % 2 == 0:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(0.1)
        elif portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(1)
          util.do_fade(0.5)

          util.do_dash(1)
          util.do_fade(0.5)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 500)
          util.do_fade(4)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(600, 250)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(600, 250)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        portal_counter += 1
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)

        if portal_counter % 2 == 0:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(0.1)
        elif portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(1)
          util.do_fade(0.5)

          util.do_dash(1)
          util.do_fade(0.5)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 500)
          util.do_fade(4)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(650, 250)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        mobs_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(650, 250)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        portal_counter += 1
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)

        if portal_counter % 2 == 0:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(0.1)
        elif portal_counter == 9:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 250)
          util.do_dash(1)
          util.do_fade(0.5)

          util.do_dash(1)
          util.do_fade(0.5)
        else:
          util.move_click_rel(10, 10, dialog, 0.5)
          util.move(630, 500)
          util.do_fade(4)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

      if pathing == False:
        break

    if boss_found == 0 and mobs_found == 1:
      util.attack_mobs(unit, 1, util.val_default_interval, self.val_sidestep)

      util.move(630, 250)
      util.do_dash(1)
      util.do_fade(0.5)

      util.do_dash(1)
      util.do_fade(0.1)

  def run_dungeon(self, runs):
    global portal_counter
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      portal_counter = 0
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

      util.move_scroll(375, 150, 700, 150)

      # Click Dungeon
      util.click_portal(600, 250)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Mechape Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_MECHAPE)
        try:
          boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOSS_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # First Boss
      util.do_deselect_pack()
      util.do_battle_mode()
      util.attack_semi_boss(1, 1, 0, 0)
      util.plunder_box(1, 3)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      util.move(630, 250)
      util.do_dash(1)
      util.do_fade(0.5)

      util.do_dash(1)
      util.do_fade(0.5)

      util.do_dash(0.1)

      # Tricus Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_TRICUS)
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

      # Final Boss
      util.do_deselect_pack()
      util.do_dash(0.1)
      util.do_short_buffs()
      util.attack_boss()
      util.do_plunder(2)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_atk_type() == 1:
        util.move(620, 350)
        util.do_dash(0.5)

      util.plunder_box(1, 3)

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
      util.wait(1)
