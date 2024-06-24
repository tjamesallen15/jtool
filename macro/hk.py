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

# UNIQUE VARIABLES
val_sidestep = 0

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

def path_find(unit=util.UNIT_BLANK):
  pathing = True
  boss_found = 0
  boss_check = 0
  box_found = 0
  backtrack_counter = 0
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)

    # backtrack_counter += 1
    # util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
    # if (backtrack_counter >= 10):
    #   backtrack_counter = 0
    #   path_backtrack(unit)

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

    if pathing == False:
      break

    try:
      util.move_click(580, 260, 0.5)
      util.do_dash(0.5)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(620, 260)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(560, 260)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(640, 260)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    if pathing == False:
      break

    util.attack_mobs(unit, 1, 0.3, val_sidestep)

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

    if unit == util.UNIT_LEO:
      try:
        util.move_click(400, 450)
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
        util.move_click(350, 450)
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
        util.move_click(300, 450)
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
        util.move_click(900, 450)
        util.do_dash(1)
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
        util.move_click(950, 450)
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
        util.move_click(1000, 450)
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

    elif unit == util.UNIT_ESPI:
      try:
        util.move_click(700, 550)
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
        util.move_click(650, 550)
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
        util.move_click(600, 550)
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
        util.move_click(550, 550)
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
        util.move_click(500, 550)
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

def find_mobs(unit=util.UNIT_BLANK):
  finding = True
  find_count = 0
  while finding:
    if unit == util.UNIT_OWL_BEAR:
      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_VAOUR, grayscale=False, confidence=.7, region=util.get_full_region())
        util.log_action(util.MSG_BOSS_FOUND)
        find_count += 15
        finding = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)
        find_count += 1

      if find_count >= 15:
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_OWLBEAR, grayscale=False, confidence=.7, region=util.get_full_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        util.focus_mobs(unit, 1, 0, val_sidestep)
      except pyauto.ImageNotFoundException:
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

    elif unit == util.UNIT_HATCHLING:
      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_BOSS)
        boss = pyauto.locateOnScreen(util.IMG_PHIXIA, grayscale=False, confidence=.7, region=util.get_full_region())
        util.log_action(util.MSG_BOSS_FOUND)
        find_count += 15
        finding = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)
        find_count += 1

      if find_count >= 15:
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_HATCHLING, grayscale=False, confidence=.7, region=util.get_full_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        util.focus_mobs(unit, 1, 0, val_sidestep)
      except pyauto.ImageNotFoundException:
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    run_counter += 1
    util.set_reset_status(False)
    util.log_action(util.MSG_START_DG)
    util.log_run(run_counter)

    # Click Cabal Window
    util.go_cabal_window()
    util.release_keys(1)
    util.go_skill_slot(0.5)
    util.do_buffs()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Click Dungeon
    util.move(500, 300)
    util.do_dash(1)
    util.move_click(595, 335, 0.5)
    util.move_click(595, 335, 0.5)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Position First Sequence
    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.wait(1)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.wait(2)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Attack First Boss
    util.wait(5)
    util.attack_mobs(util.UNIT_AREIHORN_GROUP, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.loot_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Going to Portal
    util.move(420, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(420, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    try:
      util.move_click(600, 320)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(1000, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Attack Second Group
    util.wait(5)
    util.attack_mobs(util.UNIT_HATCHLING, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.wait(4)
    find_mobs(util.UNIT_HATCHLING)
    try:
      boss = pyauto.locateOnScreen(util.IMG_PHIXIA, grayscale=False, confidence=.7, region=util.get_full_region())
      # Attack Second Boss
      util.do_battle_mode()
      util.focus_mobs(util.UNIT_PHIXIA, 1, 0, val_sidestep)
      util.set_battle_mode(False)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    util.move(540, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.loot_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Going to Portal
    util.move(540, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(540, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    try:
      util.move_click(600, 320)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

    util.wait(0.5)
    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(850, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Third Group Sequence
    util.wait(5)
    # util.attack_mobs(util.UNIT_VAOUR_GROUP, 1, 0.3, 0)
    find_mobs(util.UNIT_OWL_BEAR)
    try:
      boss = pyauto.locateOnScreen(util.IMG_VAOUR, grayscale=False, confidence=.7, region=util.get_full_region())
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Attack Third Boss
    util.focus_mobs(util.UNIT_VAOUR, 1, 0, val_sidestep)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(550, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.loot_box()

    # Going to Portal
    util.move(600, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    try:
      util.move_click(600, 320)
      dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9)
      util.log_action(util.MSG_CHECK_DIALOG_FOUND)
      util.move_click_rel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)

    util.wait(1)
    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(935, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Position Last Sequence
    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.focus_gate(util.UNIT_GATE_FOUR)
    util.wait(2)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Attack Fourth Group
    util.wait(12)
    util.attack_mobs(util.UNIT_KNIGHT, 1, 0.3, 0)

    util.wait(1)
    util.move(620, 550)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 550)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 550)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_short_buffs()
    util.do_battle_mode()

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    # util.do_fade(0.5)

    # Attack Final Boss
    util.attack_mobs(util.UNIT_SHIRDRAHN, 1, 0.3, 0)
    util.loot_final_box(3)
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
    util.wait(3)


