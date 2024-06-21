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
  while pathing:
    if not util.macro:
      util.log_action(util.MSG_TERMINATE)
      pathing = False
      sys.exit()

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)

    try:
      util.move_click(600, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

    try:
      util.move_click(700, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

    try:
      util.move_click(750, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

    try:
      util.move_click(800, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

    try:
      util.move_click(850, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

    try:
      util.move_click(900, 250)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    util.wait(0.2)

    if pathing == False:
      break

def path_find_boss():
  pathing = True
  boss_found = 0
  while pathing:
    if not util.macro:
      util.log_action(util.MSG_TERMINATE)
      pathing = False
      sys.exit()

    if pathing == False:
      break

    try:
      util.move_click(600, 250)
      util.do_dash(1)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(650, 250)
      util.do_fade(0.5)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(700, 250)
      util.do_dash(0.5)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(900, 250)
      util.do_fade(0.5)
      util.do_select(0.1)
      boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    if pathing == False:
      break

def path_find_lava_gate(unit=util.UNIT_BLANK):
  pathing = True
  gate_counter = 0
  while pathing:
    if not util.macro:
      util.log_action(util.MSG_TERMINATE)
      pathing = False
      sys.exit()

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)
    if gate_counter >= 10:
      try:
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break
    else:
      gate_counter += 1
      util.move_click(350, 250)
      util.move_click(450, 250)
      util.move_click(500, 250)
      util.move_click(550, 250)
      util.move_click(600, 250)
      util.move_click(650, 250)
      util.move_click(700, 250)

def positionDarkArcher():
  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(750, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(620, 100)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(800, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(920, 200)
  util.do_dash(1)
  util.do_fade(0.5)

def positionGateKeeper():
  util.move(620, 550)
  util.do_fade(0.5)

  util.move(820, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(820, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(840, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 200)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(350, 420)
  util.do_dash(1)
  util.do_fade(0.5)

def positionLavaGate():
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(450, 600)
  util.move_click(250, 500)

def positionBoss():
  util.move(720, 400)
  util.do_fade(0.5)

  util.move(375, 150)
  pyauto.mouseDown(button="right")
  util.move(660, 150)
  pyauto.mouseUp(button="right")
  pyauto.scroll(-10000)

  util.wait(1)

  util.move(300, 420)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(300, 420)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(480, 160)
  util.do_dash(1)
  util.do_fade(0.5)

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
    util.go_skill_slot(0.5)

    util.move_click(650, 260)

    # Enter Dungeon
    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.go_skill_slot(0.5)
    util.do_buffs()

    util.move(620, 260)
    util.do_dash(1)

    # First Boss
    util.attack_boss()
    util.move(580, 260)
    util.do_fade(0.5)
    util.loot_box(2)

    # First Semi Boss Sequence
    positionDarkArcher()
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      path_find(util.UNIT_DARK_ARCHER)
      try:
        boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # First Semi Boss
    util.attack_semi_boss(0)

    # Second Semi Boss Sequence
    positionGateKeeper()
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Second Semi Boss
    util.attack_semi_boss(0)

    # Gate Sequence
    positionLavaGate()
    path_find_lava_gate(util.UNIT_LAVA_GATE)
    util.focus_mobs(util.UNIT_LAVA_GATE, 1, 0)

    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    util.focus_mobs(util.UNIT_LAVA_GATE, 1, 0)

    # Boss Sequence
    positionBoss()
    moving = True
    while moving:
      if not util.macro:
        util.log_action(util.MSG_TERMINATE)
        moving = False
        sys.exit()

      if moving == False:
        break

      path_find_boss()
      try:
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    # Final Boss
    util.do_battle_mode()
    util.do_short_buffs()
    util.attack_boss()
    util.loot_box(2)
    util.set_battle_mode(False)

    # Start to End Dungeon
    util.end_dungeon()
    util.dice_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
