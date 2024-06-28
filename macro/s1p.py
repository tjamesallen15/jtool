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

def loot_siena_box(sec=3, select=1):
  checking = True
  boxCounter = 0
  while checking:
    if not util.get_macro_state():
      util.log_action(util.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      if select == 1:
        util.do_select(0.1)
      box = pyauto.locateOnScreen(util.IMG_SIENA, grayscale=False, confidence=.8, region=util.get_full_region())
      util.log_action(util.MSG_SIENA_BOX_FOUND)
    except pyauto.ImageNotFoundException:
      util.log_action(util.MSG_NO_BOX_FOUND)

    util.do_loot()

    boxCounter += 1
    if boxCounter > sec:
      boxCounter = 0
      break

def run_dungeon(runs=1):
  run_counter = 0
  while run_counter < runs:
    run_counter += 1
    # util.set_battle_mode(False)
    util.set_reset_status(False)
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
    # util.move_click(450, 600, 1.5)

    util.move(450, 600)
    util.do_dash(1)
    util.move_click(680, 420, 1)

    util.enter_dungeon()
    util.challenge_dungeon()

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(500, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(660, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    # First Sibling Dialog
    util.move_click(600, 380, 0.8)
    util.move_click(15, 525, 0.8)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 4:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)

    util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move_click(490, 400, 1.5)

    util.do_aura(3)
    util.move(660, 150)
    util.do_dash(1.5)
    util.move(660, 250)
    util.do_dash(0.5)

    # First Boss
    util.do_essentials()
    util.attack_boss()
    util.set_battle_mode(False)
    util.do_essentials()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(580, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(750, 300)
    util.do_dash(1.3)

    util.move(1000, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(580, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(580, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 600)
    util.do_dash(1)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(550, 175)
    # util.do_dash(1)
    util.do_fade(0.5)

    # Portal
    util.move_click(620, 250, 1.5)
    util.move_click(15, 535, 1)

    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(660, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(660, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Second Sibling Dialog
    util.move_click(600, 380, 0.8)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 5:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(630, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(630, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(800, 250)
    util.do_dash(1)
    util.do_fade(2)

    # Box Dialog
    util.move_click(430, 340, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 4:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(750, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(370, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(720, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(510, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(800, 350)
    util.do_dash(1)
    util.do_fade(0.5)

    # Altar Dialog
    util.move_click(760, 450, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(400, 450)
    util.do_dash(1)

    # Second Sibling Sequence II
    util.move_click(575, 300, 1.5)
    util.move_click(600, 380, 0.8)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(600, 650)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(640, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(200, 400)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 250)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(400, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(820, 250)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_aura(3)
    util.do_short_buffs()

    util.move(640, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(640, 150)
    util.do_dash(1)

    # Second Boss
    util.do_essentials()
    util.attack_boss()
    util.do_essentials()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(330, 300)
    util.do_dash(1.3)

    util.move(660, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1000, 250)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(1200, 460)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(600, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(1200, 350)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(900, 350)
    util.do_dash(1.5)

    util.move(600, 275)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(800, 250)
    util.do_dash(1.5)

    util.move(80, 350)
    util.do_dash(1)

    util.move(500, 300)
    util.do_fade(0.5)
    util.do_dash(1.5)
    # util.do_fade(0.5)

    util.move(770, 300)
    util.do_dash(1)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(650, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(680, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(680, 150)
    util.do_dash(1)
    # util.do_fade(0.5)

    # Third Sibling
    util.move_click(705, 390, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 5:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(700, 550)
    util.do_dash(1)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(700, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    util.do_dash(1)

    # Third Boss
    util.do_essentials()
    util.attack_boss()
    util.set_battle_mode(False)
    util.do_essentials()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(720, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(670, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(100, 350)
    util.do_dash(1)
    util.do_fade(2)

    # Egg Dialog
    util.move_click(360, 350, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 2:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(700, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 160)
    util.do_dash(1)
    util.do_fade(0.5)

    # Wall Dialog
    util.move_click(1100, 400, 2)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(350, 400)
    util.do_dash(1.3)

    util.move(575, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(575, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(575, 600)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(575, 600)
    util.do_dash(1)
    util.do_fade(1.5)

    util.move(575, 600)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(700, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(680, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Fire Dialog
    util.move_click(570, 320, 1.5)
    # util.move_click(1100, 400, 2)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(680, 625)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(630, 625)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(350, 625)
    util.do_dash(1)

    util.move(850, 625)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(620, 625)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(400, 625)
    util.do_dash(1)

    util.move(750, 625)
    util.do_fade(0.5)

    # Egg Dialog II
    util.move_click(360, 450, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 3:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(680, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(800, 150)
    util.do_dash(1.3)

    util.move(520, 200)
    util.do_dash(1.3)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(680, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Four Altars Dialog
    util.move_click(520, 300, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move_click(900, 330, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move_click(420, 260, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move_click(900, 320, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)
    util.move_click(15, 535, 1.5)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Twin Boss Sequence (Fourth and Fifth Boss)
    util.move(580, 150)
    util.do_dash(1.5)

    util.move(640, 250)
    util.do_dash(1.5)

    util.move(270, 400)
    util.do_dash(1)

    util.do_essentials()
    util.attack_boss()

    util.wait(1)

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(1000, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.do_essentials()
    util.attack_boss()
    util.set_battle_mode(False)
    util.do_essentials()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(820, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    # Portal II
    util.move_click(420, 450, 1.5)
    util.move_click(500, 500, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(1000, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(100, 350)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    util.wait(0.8)

    util.move(250, 150)
    util.do_dash(1)
    util.do_fade(1.3)

    util.move(750, 150)
    util.do_fade(0.5)

    # Umpra The Weak Sequence
    checking = True
    count_umpra = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if count_umpra > 10:
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_UMPRA_WEAK)
        umpra = pyauto.locateOnScreen(util.IMG_UMPRA_WEAK, grayscale=False, confidence=.8, region=util.get_full_region())
        util.log_action(util.MSG_UMPRA_WEAK_FOUND)
        util.focus_mobs(util.UNIT_UMPRA_WEAK, 0, 0, val_sidestep)
        checking = False
      except pyauto.ImageNotFoundException:
        count_umpra += 1
        util.log_action(util.MSG_NO_UMPRA_WEAK_FOUND)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.wait(1)
    for x in range(20):
      util.loot_essentials()
      util.loot_essentials()
      util.loot_essentials()

    util.move(750, 150)
    util.do_dash(1.5)

    # Altar Dialog
    util.move_click(700, 300, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 3:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)
    # util.move_click(15, 535, 0.8)

    if util.get_reset_status():
      continue

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    # Going to the Siena Secret Room
    util.move(200, 425)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 625)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(100, 350)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(620, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move(500, 150)
    util.do_dash(1)
    util.do_fade(0.5)

    util.move_click(500, 300, 1.5)
    checking = True
    dialog_count = 0
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      if dialog_count == 1:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        dialog_count += 1
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_CHECK_DIALOG_FOUND)
        util.force_exit_dungeon()
        checking = False
        util.set_reset_status(True)
    # util.move_click(15, 535, 0.8)

    # Siena Box Sequence
    checking = True
    while checking:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        checking = False

      if checking == False:
        break

      try:
        util.do_select(0.1)
        util.log_action(util.MSG_CHECK_SIENA_BOX)
        umpra = pyauto.locateOnScreen(util.IMG_SIENA, grayscale=False, confidence=.8, region=util.get_full_region())
        util.log_action(util.MSG_SIENA_BOX_FOUND)
        util.focus_mobs(util.UNIT_SIENA_BOX, 0, 0, val_sidestep)
        checking = False
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_SIENA_BOX_FOUND)

    if util.get_reset_status():
      continue

    util.wait(1)
    loot_siena_box()

    # Check Macro State
    if not util.get_macro_state():
      run_counter += 1000
      continue

    util.force_exit_dungeon()
    util.log_action(util.MSG_END_DG)
    util.wait(3)
  