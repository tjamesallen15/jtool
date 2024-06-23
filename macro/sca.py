import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import util
pynboard = Controller()

# GLOBAL VARIABLES
frame_root = []
btn_start = []
portal_counter = 0

def initialize(frame, btn, runs=1):
  global frame_root
  frame_root = frame

  global btn_start
  btn_start = btn

  shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
  btn_start.config(state="disabled")
  frame_root.update()
  run_dungeon(int(runs))
  btn_start.config(state="active")
  frame_root.update()

def path_find(unit):
  global portal_counter
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
    util.move_click(620, 460)
    util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
    if (backtrack_counter >= 10):
      backtrack_counter = 0
      path_backtrack(unit)

    try:
      util.move_click(620, 250)

      if portal_counter % 2 != 0:
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
      util.move_click(620, 250)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      portal_counter += 1
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)

      if portal_counter % 2 == 0:
        util.do_dash(0.1)
      else:
        util.move(620, 460)
        util.do_fade(0.5)

      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

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
      util.log_action(util.MSG_NO_BOSS_FOUND)

    try:
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    try:
      util.move_click(590, 250)
      if portal_counter % 2 != 0:
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
      util.move_click(590, 250)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      portal_counter += 1
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)

      if portal_counter % 2 == 0:
        util.do_dash(0.1)
      else:
        util.move(620, 460)
        util.do_fade(0.5)

      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

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
      util.log_action(util.MSG_NO_BOSS_FOUND)

    try:
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    try:
      util.move_click(650, 250)
      if portal_counter % 2 != 0:
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
      util.move_click(650, 250)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      portal_counter += 1
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)

      if portal_counter % 2 == 0:
        util.do_dash(0.1)
      else:
        util.move(620, 460)
        util.do_fade(0.5)

      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

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
      util.log_action(util.MSG_NO_BOSS_FOUND)

    try:
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

  if boss_found == 0:
    util.attack_mobs(unit)

def path_backtrack(unit):
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
    if (backtrack_counter >= 10):
      backtrack_counter = 0
      backtracking = False

    util.log_action(util.MSG_BACKTRACK + unit)
    try:
      util.move_click(620, 460)
      util.do_dash()
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    try:
      util.move_click(620, 460)
      util.do_dash()
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    try:
      util.move_click(620, 460)
      util.do_dash()
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    try:
      util.move_click(620, 460)
      util.do_dash()
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

  util.attack_mobs(unit)

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    run_counter += 1
    util.log_action(util.MSG_START_DG)
    util.log_run(run_counter)

    # Click Cabal Window
    util.go_cabal_window()
    util.release_keys()
    util.go_skill_slot(0.5)
    util.do_buffs()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Click Dungeon
    util.move_click(600, 240)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

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

      path_find(util.UNIT_MECHAPE)
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

    util.wait(1)

    # First Boss
    util.do_deselect_pack()
    util.do_deselect_pack()

    util.wait(1)
    util.do_battle_mode()
    util.attack_semi_boss()
    util.loot_box(2)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.set_battle_mode(False)

    # Tricus Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      path_find(util.UNIT_TRICUS)
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

    util.wait(1)

    # Final Boss
    util.do_deselect_pack()
    util.do_deselect_pack()
    util.do_dash(1)
    util.do_short_buffs()
    util.attack_boss()
    util.do_loot()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(620, 350)
    util.do_dash(0.5)

    util.move(640, 350)
    util.do_fade(0.5)

    util.loot_box(2)

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
    util.wait(3)
