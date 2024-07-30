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
  run_dungeon(runs)
  btn_start.config(state="active")
  frame_root.update()

def path_find(unit=util.UNIT_BLANK):
  pathing = True
  boss_found = 0
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    util.log_action(util.MSG_PATH_FIND + unit)
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
      util.move_click(580, 260, 0.5)
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

    try:
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

  if boss_found == 0:
    util.attack_mobs(unit, 1, 0.3, val_sidestep)

def path_find_gate_strict(unit=util.UNIT_BLANK):
  pathing = True
  gate_counter = 0
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if util.get_party_status() == 1:
      gate_counter += 1
      if gate_counter >= 2:
        pathing = False

    if pathing == False:
        break

    util.log_action(util.MSG_PATH_FIND + unit)
    try:
      util.move_click(600, 260)
      util.do_select(0.1)
      gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_GATE_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_GATE_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(580, 260)
      util.do_select(0.1)
      gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_GATE_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_GATE_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(620, 260)
      util.do_select(0.1)
      gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_GATE_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_GATE_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(540, 260)
      util.do_select(0.1)
      gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_GATE_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_GATE_FOUND)

    if pathing == False:
      break

    try:
      util.move_click(660, 260)
      util.do_select(0.1)
      gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_GATE_FOUND + unit)
      pathing = False
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_GATE_FOUND)

    if pathing == False:
      break

    if unit == util.UNIT_GATE_FOUR or unit == util.UNIT_GATE_TWO:
      try:
        util.move_click(450, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(500, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(550, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(700, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(750, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(800, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(850, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(900, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(1000, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

      if pathing == False:
        break

    util.move_click(705, 450, 2)
    util.move_click(705, 250, 1.5)

  return gate_counter

def path_find_boss():
  pathing = True
  boss_found = 0
  util.log_action(util.MSG_CHECK_BOSS)
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    try:
      util.move_click(600, 260)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move_click(620, 260)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move_click(580, 160)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move_click(660, 160)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move_click(540, 160)
      util.do_select(0.1)
      mobs = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_BOSS_FOUND)
      pathing = False
      boss_found = 1
      util.log_action(util.MSG_PATH_STOP)
      break
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOSS_FOUND)

    if pathing == False:
      break

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
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

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Click Dungeon
    util.click_portal(600, 240)

    util.enter_dungeon()
    util.challenge_dungeon()

    if util.is_party == 1:
      util.wait(3)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Mech Lion Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      path_find(util.UNIT_MECH_LION)
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

    # First Boss
    util.do_deselect_pack()
    util.move(700, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_short_buffs()
    util.do_battle_mode()
    util.attack_boss(1, 1, 0, 0)
    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.set_battle_mode(False)

    util.move(710, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(710, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(680, 200)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(530, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Gate One
    util.focus_gate(util.UNIT_GATE_ONE)
    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(530, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(530, 150)
    util.do_dash(1)
    util.do_fade(0.5)
    util.wait(3)

    util.move(500, 150)
    util.do_dash(1)

    util.wait(2)
    util.do_fade(0.5)

    util.move(500, 420)
    util.do_fade(1)

    util.wait(5)
    util.attack_mobs(util.UNIT_MECH_LIHONAR, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(530, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(530, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(500, 440)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(350, 200)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(350, 200)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(350, 200)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(550, 380)
    util.do_fade(0.5)

    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Gate Two
    util.focus_gate(util.UNIT_GATE_TWO)
    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(650, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(590, 260)
    util.do_dash(1)

    util.do_select(0.1)
    util.focus_mobs(util.UNIT_ESPADA_1, 1, 0, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(900, 380)
    util.do_dash(1)
    util.do_fade(0.5)
    util.wait(8)

    util.move(400, 380)
    util.do_dash(1)

    # Espada I Sequence
    util.attack_mobs(util.UNIT_ESPADA_1, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(550, 380)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1000, 400)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(320, 500)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(320, 500)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(320, 500)
    util.do_dash(1)
    util.do_fade(0.5)

    # Power Supply
    util.do_select(0.1)
    util.focus_gate(util.UNIT_POWER_SUPPLY)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(900, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(400, 360)
    util.do_fade(0.5)

    util.move(550, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(540, 260)
    util.do_dash(1)
    util.do_fade(0.5)
    util.wait(5)

    # Espada II Sequence
    util.attack_mobs(util.UNIT_ESPADA_2, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(580, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(580, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Power Supply II
    util.do_select(0.1)
    util.focus_gate(util.UNIT_POWER_SUPPLY)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(600, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.wait(0.1)
    util.move(420, 400)
    util.do_fade(0.5)

    util.move(650, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)

    util.move(620, 550)
    util.do_fade(1.2)

    util.move(620, 550)
    util.do_dash(1.2)

    util.do_fade(0.5)
    util.wait(10)

    util.move(630, 250)
    util.do_fade(1)

    # Espada III Sequence
    util.attack_mobs(util.UNIT_ESPADA_3, 1, 0.3, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(640, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(500, 350)
    util.do_dash(1)
    util.do_fade(0.5)

    # Power Supply III
    util.do_select(0.1)
    util.focus_gate(util.UNIT_POWER_SUPPLY)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(900, 300)
    util.do_dash(1)
    util.do_fade(0.5)
    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(770, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(770, 150)
    util.do_dash(1)
    util.do_fade(0.5)
    util.wait(1)

    util.move(800, 400)
    util.do_dash(1)
    util.wait(4)

    util.move(400, 400)
    util.do_dash(1)

    # Poerte Sequence
    util.attack_mobs(util.UNIT_POERTE, 1, 0.6, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.do_deselect_pack()
    util.move(620, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_short_buffs()
    util.do_battle_mode()

    # Second Boss
    util.attack_boss()
    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.set_battle_mode(False)

    util.move(640, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1040, 410)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(570, 550)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(580, 550)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(640, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    # Gate Three
    util.focus_gate(util.UNIT_GATE_THREE)
    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(640, 150)
    util.do_dash(1)

    util.move(450, 350)
    util.do_fade(0.5)

    util.move(590, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)
    util.wait(2)

    if util.get_atk_type() == 0:
      util.move(640, 500)
      util.do_dash(1)
      util.do_fade(0.5)

    # Redonno Sequence
    for x in range(5):
      util.do_select(0.1)
      util.focus_mobs(util.UNIT_REDONNO, 1, 0, 0)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(670, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(670, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Third Boss
    util.attack_boss()
    util.set_battle_mode(False)
    util.plunder_box()

    util.move(670, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Gate IV
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      gate_counter = path_find_gate_strict(util.UNIT_GATE_FOUR)
      if gate_counter > 3 and util.get_party_status() == 1:
        moving = False

      try:
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    util.move(800, 400)
    util.do_fade(0.5)
    util.focus_gate(util.UNIT_GATE_FOUR)
    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.do_battle_mode()
    util.do_aura()
    util.do_short_buffs()

    # Final Boss Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

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

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.do_deselect_pack()
    util.move(560, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    # Final Boss
    util.attack_boss()
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
