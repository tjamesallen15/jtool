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

def initialize(frame, btn, runs=1):
  global frame_root
  frame_root = frame

  global btn_start
  btn_start = btn

  btn_start.config(state="disabled")
  frame_root.update()
  run_dungeon(int(runs))
  btn_start.config(state="active")
  frame_root.update()

def path_find(unit):
  pathing = True
  boss_found = 0
  backtrack_counter = 0
  while pathing:
    if not util.macro:
      util.log_action(util.MSG_TERMINATE)
      pathing = False
      sys.exit()

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

  if boss_found == 0:
    util.attack_mobs(unit)

def path_backtrack(unit):
  backtracking = True
  boss_found = 0
  backtrack_counter = 0
  while backtracking:
    if not util.macro:
      util.log_action(util.MSG_TERMINATE)
      backtracking = False
      sys.exit()

    if backtracking == False:
      break

    backtrack_counter += 1
    util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
    if (backtrack_counter >= 10):
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

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    run_counter += 1
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.log_action(util.MSG_START_DG)
    util.log_run(run_counter)

    # Click Cabal Window
    util.go_cabal_window()
    util.release_keys()

    # Click Dungeon
    util.move(677, 361)
    util.move(735, 361, 0.5)
    util.move_click(735, 361, 0.5)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(250, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.go_skill_slot(0.5)
    util.do_buffs()

    # Initial Position
    util.move(850, 600)
    util.do_dash(0.1)

    # Mush and Flower Sequence
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      path_find(util.UNIT_MUSH_FLOWER)
      try:
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    util.do_deselect_pack()
    util.move(850, 600)
    util.do_dash(0.1)

    # First Boss
    util.do_short_buffs()

    util.attack_boss()
    util.move(450, 450)
    util.do_fade(0.5)
    util.loot_box()

    util.move_click(400, 260)
    util.do_dash(0.5)

    # Mossite and Toad Sequence
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      path_find(util.UNIT_MOSS_TOAD)
      try:
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Second Boss
    util.do_deselect_pack()
    util.move(800, 360)
    util.do_dash(1)
    util.move(500, 300)
    util.do_fade(0.1)

    secondBoss = True
    while secondBoss:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        secondBoss = False
        sys.exit()

      if secondBoss == False:
        break

      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        secondBoss = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    util.attack_boss()
    util.do_deselect_pack()
    util.move(500, 100)
    util.do_fade(0.5)
    util.loot_box()

    # Lumber and Dorigo Sequence
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      path_find(util.UNIT_LUMBER_DORIGO)
      try:
        mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Position for First Orphidia
    util.do_deselect_pack()
    util.move(800, 260)
    util.do_dash(0.5)

    util.move_click(500, 260)
    util.move_click(400, 320)
    util.do_dash(1)
    util.do_dash(1)
    util.do_fade(0.1)

    util.move(320, 540)
    util.do_deselect_pack()
    util.do_dash(0.5)

    util.move(400, 400)
    util.do_fade(0.5)

    # First Orphidia
    try:
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.attack_boss()
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    util.move(675, 600)
    util.do_dash(0.5)

    util.do_battle_mode()

    # Second and Third Orphidia
    bossTracker = 0
    bossCount = 0
    shortBuffsCounter = 0
    while bossCount < 2:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      bossTracker += 1
      if bossTracker >= 60:
        bossTracker = 0
        bossCount += 10
        break

      if (bossCount == 1 and shortBuffsCounter == 0 and util.shortBuffsAllowed == 1):
        shortBuffsCounter = 1
        util.do_short_buffs()

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        bossCount += 1
        util.attack_boss()
        util.do_deselect_pack()
        if (bossCount == 1):
          util.wait(5)
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Pathfind Treasure Boxes
    boxing = True
    while boxing:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        boxing = False
        sys.exit()

      util.log_action(util.MSG_PATH_FIND + util.UNIT_BOX)
      util.move_click(550, 160)
      util.wait(1)

      util.do_dash(0.5)
      util.move_click(650, 160, 0.3)
      util.move_click(750, 160, 0.3)
      util.move_click(850, 160, 0.3)
      util.move_click(950, 160, 0.3)
      util.move_click(950, 480)
      util.do_dash(1)
      util.do_fade(0.5)

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOX_FOUND)
        boxing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOX_FOUND)

    # Loot Treasure Boxes
    boxCounter = 0
    while boxCounter < 10:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        boxCounter = False
        sys.exit()

      if boxCounter > 10:
        break

      try:
        util.do_select(0.1)
        boxCounter += 1
        box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_BOX_FOUND)
        util.log_action(util.MSG_PATH_STOP)
        boxCounter += 2
        util.loot_final_box()
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOX_FOUND)

      try:
        checkenddg = pyauto.locateOnScreen(util.IMG_END_DG, grayscale=False, confidence=.9)
        boxCounter += 10
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_CHECK_END_DG)

    util.set_battle_mode(False)

    # Start to End Dungeon
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
