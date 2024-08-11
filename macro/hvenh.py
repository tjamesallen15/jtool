from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import common.util as util
pynboard = Controller()

# GLOBAL VARIABLES
frame_root = []
btn_start = []
val_sidestep = 0

difficulty = "Hazardous Valley (Easy)"
dungeonList = [
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)"
]

def initialize(frame, btn, runs, diff):
  global frame_root
  frame_root = frame

  global btn_start
  btn_start = btn

  global difficulty
  difficulty = diff

  shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
  btn_start.config(state=util.STATE_DISABLED)
  frame_root.update()

  run_dungeon(runs)

  btn_start.config(state=util.STATE_NORMAL)
  frame_root.update()

def path_find(unit):
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
      path_backtrack(unit)

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

    if unit == util.UNIT_CUTTER_TOAD:
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
      if unit == util.UNIT_WHITE_SNAKE:
        util.do_dash(1)
        util.do_fade(0.5)
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

    if unit == util.UNIT_WHITE_SNAKE or unit == util.UNIT_BOAR_SNAKE:
      try:
        util.move_click(200, 260)

        if unit == util.UNIT_WHITE_SNAKE:
          util.do_dash(1)
          util.do_fade(0.5)

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
        util.move_click(100, 260)

        if unit == util.UNIT_WHITE_SNAKE:
          util.do_dash(1)
          util.do_fade(0.5)

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

  interval = 0.3
  if unit == util.UNIT_CUTTER_TOAD:
    interval = 0.5

  if boss_found == 0:
    util.attack_mobs(unit, 1, interval)

def path_find_boss(unit):
  pathing = True
  boss_found = 0
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)
    util.move_click(675, 450)

    util.move_click(600, 260)
    util.do_dash(0.5)
    util.do_select(0.1)
    util.log_action(util.MSG_CHECK_BOSS)

    util.move_click(500, 260, 0.5)
    util.do_dash(0.5)
    util.do_select(0.1)
    util.log_action(util.MSG_CHECK_BOSS)

    try:
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND)
      util.focus_mobs(util.UNIT_WHITE_SNAKE, 0, 0)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.move_click(400, 260)
    util.move_click(300, 260)
    util.move_click(200, 260)

    try:
      util.move_click(200, 360)
      util.do_dash(0.5)
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      util.do_deselect_pack()
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    try:
      util.move_click(200, 160)
      util.do_dash(0.5)
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      util.do_deselect_pack()
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

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
    if unit == util.UNIT_WHITE_SNAKE:
      path_find_white_snake()

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

    try:
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOX_FOUND)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

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

    try:
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOX_FOUND)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

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

    try:
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOX_FOUND)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

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

    try:
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOX_FOUND)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

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

    try:
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOX_FOUND)
      backtracking = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

    if backtracking == False:
      break

  util.attack_backtrack(unit, 1, 1, 0)

def position_orphidia():
  util.do_deselect_pack()
  util.move(400, 260)
  util.do_dash(1)
  util.do_fade(0.5)

  util.do_deselect_pack()
  util.move(320, 540)
  util.do_dash(1)

  util.do_deselect_pack()
  util.move(400, 260)
  util.do_dash(1)
  util.do_fade(0.5)

  util.do_deselect_pack()
  util.move(320, 540)
  util.do_dash(1)

  util.move(400, 400)
  util.do_fade(0.5)

def path_find_white_snake():
  util.log_action(util.MSG_PATH_FIND + util.UNIT_WHITE_SNAKE)
  util.move_click(650, 160, 0.3)
  util.do_dash(1)

  util.move_click(850, 160, 1)
  util.do_fade(0.5)

  util.move_click(950, 480)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move_click(850, 570)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move_click(850, 600)
  util.do_dash(1)
  util.do_fade(0.5)

def move_to_box():
  util.move_click(675, 450)
  util.move_click(500, 260)

  util.move(800, 380)
  util.do_fade(0.5)

def run_dungeon(runs):
  run_counter = 0
  while run_counter < runs:
    util.set_reset_status(False)
    util.check_run_restart(run_counter)
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

    # Click Dungeon
    util.move(677, 361)
    util.move(735, 361, 0.5)
    util.click_portal(735, 361)

    if difficulty == dungeonList[0]:
      util.move_click(440, 300, 1)
    elif difficulty == dungeonList[1]:
      util.move_click(440, 280, 1)
    elif difficulty == dungeonList[2]:
      util.move_click(440, 260, 1)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(250, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.3)

    util.move(500, 300)
    util.do_dash(0.5)
    util.wait(3)
    util.attack_mobs(util.UNIT_CUTTER_TOAD, 1, 0.3, val_sidestep)

    util.move(375, 150)
    util.do_dash(1)
    util.do_fade(1.5)
    util.do_fade(0.5)
    util.wait(6)
    util.attack_mobs(util.UNIT_CUTTER_TOAD, 1, 0.3, val_sidestep)

    util.move(375, 175)
    util.do_dash(1)
    util.do_fade(0.5)
    util.do_dash(1)
    util.do_fade(1)

    util.move(250, 350)
    util.do_dash(3)
    util.do_fade(2)
    util.attack_mobs(util.UNIT_CUTTER_TOAD, 1, 0.3, val_sidestep)

    util.move(535, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(400, 200)
    util.do_dash(1)
    util.do_fade(1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Cutter and Toad Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

      if moving == False:
        break

      path_find(util.UNIT_CUTTER_TOAD)
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
    util.move(630, 520)
    util.do_fade(0.5)
    util.move(550, 250)
    util.do_dash(0.5)

    checking = True
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
         break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        checking = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # First Boss
    util.attack_boss()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.do_deselect_pack()
    util.move_click(570, 260)
    util.do_fade(1.5)
    util.do_fade(0.5)

    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Boars and Snakes Sequence (Orphidia I)
    moving = True
    while moving:
      if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

      if moving == False:
        break

      path_find(util.UNIT_BOAR_SNAKE)
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

    # Position for Orphidia I
    util.do_deselect_pack()
    position_orphidia()

    # Attack Orphidia I
    try:
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      util.attack_boss()
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(640, 560)
    util.do_fade(0.5)
    util.plunder_box()

    # Orphidia Sequence II
    path_find_white_snake()
    moving = True
    while moving:
      if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

      if moving == False:
        break

      path_find(util.UNIT_WHITE_SNAKE)
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

    # Position for Orphidia II
    position_orphidia()

    util.wait(1)
    # Attack Orphidia II
    try:
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      util.attack_boss()
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(640, 560)
    util.do_fade(0.5)
    util.plunder_box()

    # Orphidia Sequence III
    path_find_white_snake()
    moving = True
    while moving:
      if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

      if moving == False:
        break

      path_find(util.UNIT_WHITE_SNAKE)
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

    # Position for Orphidia III
    position_orphidia()

    # Attack Orphidia III
    try:
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      util.attack_boss()
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)
      util.force_exit_dungeon()
      util.set_reset_status(True)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(640, 560)
    util.do_fade(0.5)
    util.plunder_final_box()

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
