
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class HolyWindmill(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
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

  def path_find_gate_strict(self, unit=util.UNIT_BLANK):
    pathing = True
    while pathing:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        pathing = False

      if pathing == False:
          break

      util.log_action(util.MSG_PATH_FIND + unit)

      if unit == util.UNIT_GATE_THREE:
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
          util.move_click(650, 260)
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
          util.do_dash(0.5)
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
          util.do_fade()
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_GATE_FOUND)

        if pathing == False:
          break

      else:
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

        if unit == util.UNIT_GATE_TWO:
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

      if unit == util.UNIT_GATE_FOUR:
        util.move_click(675, 450)
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

  def path_find_legrin_gate(self, unit=util.UNIT_BLANK):
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
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

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

      try:
        util.move_click(580, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

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

      try:
        util.move_click(620, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

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

      try:
        util.move_click(300, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_GATE_FOUND)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_NO_GATE_FOUND)

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

    if boss_found == util.STATE_ZERO:
      util.focus_gate(util.UNIT_LEGRIN)

  def path_find(self, unit=util.UNIT_BLANK):
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

      backtrack_counter += 1
      util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
      if (backtrack_counter >= 10):
        backtrack_counter = 0
        self.path_backtrack(unit)

      if unit == util.UNIT_BOX:
        if (backtrack_counter >= 5):
          util.move_click(675, 450)

        try:
          util.move(680, 160)
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_HOLY_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

        if pathing == False:
          break

        try:
          util.move(660, 160)
          util.do_dash(0.5)
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_HOLY_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

        if pathing == False:
          break

        try:
          util.move(640, 160)
          util.do_select(0.1)
          box = pyauto.locateOnScreen(util.IMG_HOLY_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

        if pathing == False:
          break

      elif unit == util.UNIT_LEO:
        try:
          util.move_click(600, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(550, 260, 0.5)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(500, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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

      elif unit == util.UNIT_ESPI:
        try:
          util.move_click(700, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(650, 260, 0.5)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(600, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(550, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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
          util.move_click(500, 260)
          util.do_select(0.1)
          leo = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          pathing = False
          util.log_action(util.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

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

      elif unit == util.UNIT_DRACO:
        util.do_deselect_pack()
        util.move(200, 250)
        util.do_dash()
        util.do_fade()

        if (backtrack_counter >= 5):
          util.wait(1)
          util.move_click(800, 400)
          util.do_fade()

        try:
          util.move_click(600, 260)
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

        try:
          util.move_click(580, 260, 0.5)
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
          util.move_click(620, 260)
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
          util.move_click(560, 260)
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
          util.move_click(640, 260)
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

      boss_check += 1
      if boss_check >= 3 and unit == util.UNIT_DRACO:
        util.move_click(800, 260)
        util.do_fade()
        boss_check = 0

    interval = 0.3
    if unit == util.UNIT_BOX:
      util.attack_mobs(unit, 0, interval, self.val_sidestep)
    elif boss_found == util.STATE_ZERO and box_found == util.STATE_ZERO and unit != util.UNIT_ESPI:
      util.attack_mobs(unit, 1, interval, self.val_sidestep)
    elif boss_found == util.STATE_ZERO and box_found == util.STATE_ZERO and unit == util.UNIT_ESPI:
      if util.get_attack_type() == util.STATE_ZERO:
        interval = 0.8
      util.attack_mobs(unit, 1, interval, self.val_sidestep)

  def path_backtrack(self, unit):
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

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(util.MSG_START_DG)
      util.log_run(run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.release_keys(1)
      util.go_skill_slot(0.2)
      util.do_buffs()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.move(400, 500)
      util.do_dash(0.8)
      util.click_portal(590, 400)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon()

      util.move(740, 420)
      util.do_fade()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Gate I
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find_gate_strict(util.UNIT_GATE_ONE)
        try:
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move(800, 300)
      util.do_dash()
      util.do_fade()

      util.do_final_mode(1)
      util.do_aura()

      util.move_scroll(500, 150, 375, 150)

      # First Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find_legrin_gate(util.UNIT_LEGRIN)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOSS_FOUND)
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
      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move(440, 560)
      util.do_dash()
      util.do_fade()

      util.do_deselect_pack()
      util.do_short_buffs()
      util.attack_boss()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(660, 150, 375, 150)
      util.move(500, 250)
      util.do_dash()

      # Gate II
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find_gate_strict(util.UNIT_GATE_TWO)
        try:
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move(620, 150)
      util.do_dash()

      util.focus_gate(util.UNIT_GATE_TWO)

      util.do_deselect_pack()
      util.move(400, 240)
      util.do_dash()
      util.do_fade()

      # Second Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_LEO)
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

      util.move(620, 150)
      util.do_dash(1.2)
      util.move(620, 150)
      util.do_dash(1.2)
      util.move(620, 150)
      util.do_dash(1.2)
      util.move(820, 550)
      util.do_dash()

      util.do_battle_mode()
      util.attack_boss()
      util.set_battle_mode(False)
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(620, 150)
      util.do_dash()
      util.move_scroll(375, 150, 660, 150)

      # Gate III
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find_gate_strict(util.UNIT_GATE_THREE)
        try:
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
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

      util.move(1000, 360)
      util.do_dash()
      util.do_fade()
      util.move(620, 150)
      util.do_dash()
      util.do_fade()
      util.move_scroll(600, 150, 375, 150)

      util.focus_gate(util.UNIT_GATE_THREE)

      util.do_deselect_pack()
      util.move(620, 150)
      util.do_dash()

      util.move(1000, 350)
      util.do_dash()
      util.do_fade()

      # Third Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_ESPI)
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
      util.move(620, 500)
      util.do_dash()
      util.do_fade()

      util.attack_boss()
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(520, 100)
      util.do_dash()
      util.do_fade()

      util.move(520, 200)
      util.do_dash()
      util.do_fade()

      # Gate IV
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find_gate_strict(util.UNIT_GATE_FOUR)
        try:
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
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
      util.move(620, 150)
      util.do_dash()
      util.do_fade(1.5)

      util.move(800, 360)
      util.do_fade()

      util.move(700, 440)
      util.do_fade(1)

      util.do_select(0.1)
      util.focus_gate(util.UNIT_GATE_FOUR)

      util.do_deselect_pack()
      util.move(620, 150)
      util.do_dash()

      util.move(200, 250)
      util.do_dash()
      util.do_fade()

      # Fourth Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_DRACO)
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
      util.do_deselect_pack()

      util.move(400, 160)
      util.do_dash()
      util.do_fade()

      util.move(1000, 300)
      util.do_dash()
      util.do_fade(1)

      util.move(610, 160)
      util.do_fade(1)

      util.do_battle_mode()
      util.do_short_buffs()

      util.attack_boss()
      util.set_battle_mode(False)

      # Box Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_BOX)
        try:
          box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_BOX_FOUND)
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_NO_BOX_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()

      util.move(660, 160)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(700, 250)
      util.move_click(700, 360)
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Start to End Dungeon
      util.check_notifications()
      util.end_dungeon()
      util.dice_dungeon()
      util.log_action(util.MSG_END_DG)
      util.log_time()
