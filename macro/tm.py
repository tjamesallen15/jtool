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

    if unit == util.UNIT_POERTE:
      backtrack_counter += 1
      util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 10):
        backtrack_counter = 0
        path_backtrack(unit)

    if unit == util.UNIT_MECH_LIHONAR or unit == util.UNIT_ESPADA_1 or unit == util.UNIT_ESPADA_2 or unit == util.UNIT_ESPADA_3:

      if unit != util.UNIT_ESPADA_2:
        try:
          util.move_click(300, 260)
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()
          util.log_action(util.MSG_NO_MOBS_FOUND)

        if pathing == False:
          break

        # Power Supply
        if unit == util.UNIT_ESPADA_3:
          try:
            util.do_select(0.1)
            supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
            util.move(500, 440)
            util.do_dash(1)
            util.do_fade(0.5)
            pathing = False
          except pyauto.ImageNotFoundException:
            util.do_deselect_pack()

        if pathing == False:
          break

        try:
          util.move_click(500, 260)
          util.do_select(0.1)
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()
          util.log_action(util.MSG_NO_MOBS_FOUND)

        if pathing == False:
          break

        # Power Supply
        if unit == util.UNIT_ESPADA_3:
          try:
            util.do_select(0.1)
            supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
            util.move(500, 440)
            util.do_dash(1)
            util.do_fade(0.5)
            pathing = False
          except pyauto.ImageNotFoundException:
            util.do_deselect_pack()

        if pathing == False:
          break

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      # Power Supply
      if unit == util.UNIT_ESPADA_3:
        try:
          util.do_select(0.1)
          supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.move(500, 440)
          util.do_dash(1)
          util.do_fade(0.5)
          pathing = False
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()

      if pathing == False:
          break

      try:
        util.move_click(580, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      # Power Supply
      if unit == util.UNIT_ESPADA_3:
        try:
          util.do_select(0.1)
          supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.move(500, 440)
          util.do_dash(1)
          util.do_fade(0.5)
          pathing = False
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()

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
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      # Power Supply
      if unit == util.UNIT_ESPADA_3:
        try:
          util.do_select(0.1)
          supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.move(500, 440)
          util.do_dash(1)
          util.do_fade(0.5)
          pathing = False
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()

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
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

      if pathing == False:
        break

      # Power Supply
      if unit == util.UNIT_ESPADA_3:
        try:
          util.do_select(0.1)
          supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.move(500, 440)
          util.do_dash(1)
          util.do_fade(0.5)
          pathing = False
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()

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
        util.do_deselect_pack()
        util.log_action(util.MSG_NO_MOBS_FOUND)

      # Power Supply
      if unit == util.UNIT_ESPADA_3:
        try:
          util.do_select(0.1)
          supply = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.move(500, 440)
          util.do_dash(1)
          util.do_fade(0.5)
          pathing = False
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()

      pathing = False
      break

    else:
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

  if unit == util.UNIT_ESPADA_1 or unit == util.UNIT_ESPADA_2 or unit == util.UNIT_ESPADA_3:
    util.focus_mobs(unit, 1, 0, val_sidestep)

  if boss_found == 0 and util.get_atk_type() == 0 and unit == util.UNIT_REDONNO:
    util.focus_mobs(unit, 1, 0, val_sidestep)
  elif boss_found == 0 and util.get_atk_type() == 0 and unit == util.UNIT_POERTE:
    util.focus_mobs(unit, 1, 0, val_sidestep)
  elif boss_found == 0:
    util.attack_mobs(unit, 1, 0.3, val_sidestep)

def path_backtrack(unit):
  util.log_action(util.MSG_BACKTRACK + unit)
  util.move(800, 400)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 600)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 600)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 600)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(615, 600)
  util.do_dash(1)
  util.do_fade(0.5)

  util.move(450, 400)
  util.do_dash(1)
  util.do_fade(0.5)

  backtracking = True
  backtrack_counter = 0
  while backtracking:
    backtrack_counter += 1
    util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
    if (backtrack_counter >= 10):
      backtrack_counter = 0
      backtracking = False

    if backtracking == False:
      break

    try:
      util.move_click(620, 250)
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      util.log_action(util.MSG_PATH_STOP)
      util.focus_gate(unit, 0)
      backtrack_counter += 5
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    try:
      util.move_click(620, 250)
      util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(util.MSG_MOBS_FOUND + unit)
      util.log_action(util.MSG_PATH_STOP)
      util.focus_gate(unit, 0)
      util.plunder_box()
      backtrack_counter += 5
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_MOBS_FOUND)

    if backtracking == False:
      break

  util.move(770, 260)
  util.do_dash(1)
  util.do_fade(0.5)

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
  while pathing:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      pathing = False

    if pathing == False:
      break

    try:
      util.move_click(600, 260)
      util.do_select(0.1)
      util.log_action(util.MSG_CHECK_BOSS)
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
      util.log_action(util.MSG_CHECK_BOSS)
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
      util.log_action(util.MSG_CHECK_BOSS)
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
      util.log_action(util.MSG_CHECK_BOSS)
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
      util.log_action(util.MSG_CHECK_BOSS)
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
    util.attack_boss()
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

    util.focus_gate(util.UNIT_GATE_ONE)
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Mech Lihonar Sequence
    moving = True
    counter = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if counter > 6:
        moving = False
        break

      path_find(util.UNIT_MECH_LIHONAR)
      counter += 1
      print(str(counter))

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

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

    # Gate II
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      gate_counter = path_find_gate_strict(util.UNIT_GATE_TWO)
      if gate_counter > 3 and util.get_party_status() == 1:
        moving = False

      try:
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_full_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    util.focus_gate(util.UNIT_GATE_TWO, 1)
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(610, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(590, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    # Espada Sequence
    moving = True
    counter = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if counter > 6:
        moving = False
        break

      path_find(util.UNIT_ESPADA_1)
      counter += 1
      print(str(counter))

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

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

    util.focus_gate(util.UNIT_POWER_SUPPLY)
    util.do_plunder(1)

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
    util.do_fade(1)

    # Espada II Sequence
    moving = True
    counter = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if counter > 3:
        moving = False
        break

      path_find(util.UNIT_ESPADA_2)
      counter += 1
      print(str(counter))

    util.focus_gate(util.UNIT_POWER_SUPPLY)
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(680, 400)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(520, 400)
    util.do_dash(1.5)

    util.move(650, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(500, 300)
    if util.get_atk_type() == 1:
      util.do_dash(4)
    else:
      util.do_dash(1)
      util.do_fade(4)

    # Espada III Sequence
    moving = True
    counter = 0
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      if counter > 4:
        moving = False
        break

      path_find(util.UNIT_ESPADA_3)
      counter += 1
      print(str(counter))

    util.do_deselect_pack()
    util.wait(1.5)
    util.move(600, 600)
    util.do_dash(1)
    util.do_select(0.1)
    util.focus_gate(util.UNIT_POWER_SUPPLY, 0)
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(620, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(900, 300)
    util.do_dash(1)
    util.do_fade(0.5)

    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(770, 260)
    util.do_dash(1)
    util.do_fade(2)

    # Poerte Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      path_find(util.UNIT_POERTE)
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
    util.move(720, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_short_buffs()
    util.do_battle_mode()
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

    # Gate III
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      gate_counter = path_find_gate_strict(util.UNIT_GATE_THREE)
      if gate_counter > 3 and util.get_party_status() == 1:
        moving = False

      try:
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        moving = False
        util.log_action(util.MSG_MOVE_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_BOSS_FOUND)

    if util.get_atk_type == 1:
      util.move_click(650, 450, 1.5)

    util.focus_gate(util.UNIT_GATE_THREE)
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Redonno Sequence
    moving = True
    while moving:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        moving = False

      if moving == False:
        break

      path_find(util.UNIT_REDONNO)
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

    # Third Boss
    util.do_deselect_pack()
    if util.get_atk_type() == 1:
      util.move(580, 260)
      util.do_dash(1)
    else:
      util.move(720, 260)
      util.do_dash(1)

    util.do_battle_mode()
    util.attack_boss()
    util.set_battle_mode(False)
    util.plunder_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    if util.get_battle_mode() == 1:
      util.wait(20)

    util.move(720, 260)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(720, 260)
    util.do_dash(1)
    util.do_fade(0.5)

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
    util.do_plunder(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Final Boss
    util.do_battle_mode()
    util.do_aura(0, 1)
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