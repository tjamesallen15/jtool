import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class TerminusMachina(Dungeon):

  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
  val_sidestep = False

  def initialize(self, frame, btn, runs):
    self.frame_root = frame
    self.btn_start = btn

    shortcut.add_hotkey(util.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=util.STATE_DISABLED)
    self.frame_root.update()

    self.run_dungeon(runs)

    self.btn_start.config(state=util.STATE_NORMAL)
    self.frame_root.update()

  def path_find(self, unit=util.UNIT_EMPTY):
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

      if unit == util.UNIT_REDONNO:
        backtrack_counter += 1
        util.log_action(util.MSG_BACKTRACK + str(backtrack_counter))
        if (backtrack_counter >= 10):
          backtrack_counter = 0
          self.path_backtrack(unit)

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(util.MSG_MOBS_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

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
        util.log_action(util.MSG_MOBS_NOT_FOUND)

      if pathing == False:
        break

    if boss_found == util.STATE_ZERO:
      util.focus_mobs(unit, False, True, self.val_sidestep)

  def path_backtrack(self, unit):
    util.log_action(util.MSG_BACKTRACK + unit)
    util.move(630, 600)
    util.do_dash()
    util.do_fade()

    util.move(630, 600)
    util.do_dash()
    util.do_fade()

  def find_gate(self, unit=util.UNIT_EMPTY):
    pathing = True
    gate_counter = 0
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
        util.log_action(util.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(util.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(util.MSG_GATE_NOT_FOUND)

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
        util.log_action(util.MSG_GATE_NOT_FOUND)

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
        util.log_action(util.MSG_GATE_NOT_FOUND)

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
        util.log_action(util.MSG_GATE_NOT_FOUND)

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
        util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

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
          util.log_action(util.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

      util.move_click(705, 450, 2)
      util.move_click(705, 250, 1.5)

    return gate_counter

  def find_boss(self):
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
        util.log_action(util.MSG_BOSS_NOT_FOUND)

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
        util.log_action(util.MSG_BOSS_NOT_FOUND)

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
        util.log_action(util.MSG_BOSS_NOT_FOUND)

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
        util.log_action(util.MSG_BOSS_NOT_FOUND)

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
        util.log_action(util.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
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
      util.click_portal(600, 240)

      util.enter_dungeon()
      util.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150, 0.5)

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

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

        self.path_find(util.UNIT_MECH_LION)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # First Boss
      util.do_deselect_pack()
      util.move(700, 260)
      util.do_dash()
      util.do_fade()

      util.do_short_buffs()
      util.do_battle_mode()
      util.attack_boss(True, True, False, False)
      util.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      util.move(710, 260)
      util.do_dash()
      util.do_fade()

      util.move(710, 260)
      util.do_dash()
      util.do_fade()
      util.move_scroll(375, 150, 700, 150)

      util.move(680, 200)
      util.do_dash()
      util.do_fade()

      util.move(530, 150)
      util.do_dash()
      util.do_fade()

      # Gate One
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_GATE_ONE)
      else: util.focus_gate(util.UNIT_GATE_ONE)
      util.wait(0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(530, 150)
      util.do_dash()
      util.do_fade()

      util.move(530, 150)
      util.do_dash()
      util.do_fade()
      util.wait(3)

      util.move(500, 150)
      util.do_dash()

      util.wait(2)
      util.do_fade()

      util.move(500, 420)
      util.do_fade(1)

      if util.get_attack_type() == util.IS_MELEE: util.wait(7)
      else: util.wait(0.5)
      util.attack_mobs(util.UNIT_MECH_LIHONAR, True, 0.3, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(530, 150)
      util.do_dash()
      util.do_fade()

      util.move(530, 150)
      util.do_dash()
      util.do_fade()

      util.move(500, 440)
      util.do_dash()
      util.do_fade()
      util.move_scroll(700, 150, 375, 150)

      util.move(350, 200)
      util.do_dash()
      util.do_fade()

      util.move(350, 200)
      util.do_dash()
      util.do_fade()

      util.move(350, 200)
      util.do_dash()
      util.do_fade()
      util.move_scroll(700, 150, 375, 150)

      util.move(550, 380)
      util.do_fade()

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      # Gate Two
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_GATE_TWO)
      else: util.focus_gate(util.UNIT_GATE_TWO)
      util.wait(0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(650, 260)
      util.do_dash()
      util.do_fade()

      util.move(590, 260)
      util.do_dash()

      util.do_select(0.1)
      util.focus_mobs(util.UNIT_ESPADA_1, False, True, self.val_sidestep)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(800, 380)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == util.IS_MELEE: util.wait(8)
      else: util.wait(1)

      util.move(500, 380)
      util.do_dash()

      # Espada I Sequence
      power_ticks = 0
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        util.do_select(0.1)
        try:
          mobs = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          power_ticks += 1
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        if power_ticks > 10:
          checking = False

        if checking == False:
          break

        try:
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ESPADA_1)
          util.focus_mobs(util.UNIT_ESPADA_1, False, True, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_MOBS_CLEARED)
          power_ticks += 1

        if power_ticks > 10:
          checking = False

        if checking == False:
          break

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(550, 380)
      util.do_dash()
      util.do_fade()

      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      util.move(680, 150)
      util.do_dash()
      util.do_fade()

      util.move(1000, 400)
      util.do_dash()
      util.do_fade()

      util.move(320, 500)
      util.do_dash()
      util.do_fade()

      util.move(320, 500)
      util.do_dash()
      util.do_fade()

      util.move(320, 500)
      util.do_dash()
      util.do_fade()

      # Power Supply
      util.do_select(0.1)
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_POWER_SUPPLY)
      else: util.focus_gate(util.UNIT_POWER_SUPPLY)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(375, 150, 900, 150)
      util.move(400, 360)
      util.do_fade()

      util.move(550, 260)
      util.do_dash()
      util.do_fade()

      util.move(540, 260)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == util.IS_MELEE: util.wait(8)
      else: util.wait(2)

      # Espada II Sequence
      util.attack_mobs(util.UNIT_ESPADA_2, True, 0.3, False)
      util.cancel_aura(1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(540, 150)
      util.do_dash()
      util.do_fade()

      util.move(580, 150)
      util.do_dash()
      util.do_fade()

      # Power Supply II
      util.do_select(0.1)
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_POWER_SUPPLY)
      else: util.focus_gate(util.UNIT_POWER_SUPPLY)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(600, 150, 375, 150, 0.4)
      util.move(420, 400)
      util.do_fade()

      util.move(650, 150)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()

      util.move(800, 500)
      util.do_fade()
      if util.get_attack_type() == util.IS_MELEE: util.wait(12)
      else: util.wait(1)

      # Espada III Sequence
      power_ticks = 0
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          checking = False

        util.do_select(0.1)
        try:
          mobs = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          power_ticks += 1
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        if power_ticks > 20:
          checking = False

        if checking == False:
          break

        try:
          mobs = pyauto.locateOnScreen(util.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(util.MSG_MOBS_FOUND + util.UNIT_ESPADA_3)
          util.focus_mobs(util.UNIT_ESPADA_3, False, False, self.val_sidestep)
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_MOBS_CLEARED)
          power_ticks += 1

        if power_ticks > 20:
          checking = False

        if checking == False:
          break

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(350, 250)
      util.do_dash()
      util.do_fade()

      if util.get_attack_type() == util.IS_MELEE:
        util.move(450, 250)
        util.do_dash()
        util.do_fade()

      # Power Supply III
      util.do_select(0.1)
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_POWER_SUPPLY)
      else: util.focus_gate(util.UNIT_POWER_SUPPLY)
      util.wait(0.4)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(900, 300)
      util.do_dash()
      util.do_fade()
      if util.get_party_member_status() == util.IS_FALSE: util.plunder_box()
      else: util.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(750, 150)
      util.do_dash()
      util.do_fade()

      util.move(750, 150)
      util.do_dash()
      util.do_fade()
      util.wait(1)

      util.move(800, 400)
      util.do_dash()
      if util.get_attack_type() == util.IS_MELEE: util.wait(4)
      else: util.wait(2)

      util.move(400, 400)
      util.do_dash()

      util.move(640, 150)
      util.do_dash()
      util.do_fade(1.5)

      util.move(620, 600)
      util.do_dash()

      # Poerte Sequence
      util.attack_mobs(util.UNIT_POERTE, False, 0.3, self.val_sidestep)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.move(580, 260)
      util.do_dash()
      util.do_fade()

      util.do_short_buffs()
      util.do_battle_mode()

      # Second Boss
      util.attack_boss(True, True, False, False)
      util.wait(0.5)
      if util.get_party_member_status() == util.IS_FALSE: util.plunder_box()
      else: util.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      util.move(640, 260)
      util.do_dash()
      util.do_fade()

      util.move(640, 260)
      util.do_dash()
      util.do_fade()

      util.move(1040, 410)
      util.do_dash()
      util.do_fade()

      util.move(620, 550)
      util.do_dash()
      util.do_fade()

      util.move(610, 575)
      util.do_dash()
      util.do_fade()

      util.move_scroll(700, 150, 375, 150)
      util.move(640, 260)
      util.do_dash()
      util.do_fade()

      util.move(640, 260)
      util.do_dash()
      util.do_fade()

      # Gate Three
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_GATE_THREE)
      else: util.focus_gate(util.UNIT_GATE_THREE)
      util.wait(0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(640, 150)
      util.do_dash()

      util.move(450, 350)
      util.do_fade()

      util.move(590, 150)
      util.do_dash()
      util.do_fade()

      if util.get_attack_type() == util.IS_MELEE: util.wait(5)
      else: util.wait(2)

      # Redonno Sequence
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.path_find(util.UNIT_REDONNO)
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      if util.get_attack_type() == util.IS_MELEE:
        util.move(750, 150)
        util.do_dash()
        util.do_fade()
      else:
        util.move(950, 150)
        util.do_dash()
        util.do_fade()

      # Third Boss
      util.attack_boss()
      util.set_battle_mode(False)
      if util.get_party_member_status() == util.IS_FALSE: util.plunder_box(True, 4, False)
      else: util.plunder_box_party()

      util.move(670, 150)
      util.do_dash()
      util.do_fade()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Gate IV
      if util.get_party_leader_status() == util.IS_TRUE: util.wait(4)
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        gate_counter = self.find_gate(util.UNIT_GATE_FOUR)

        try:
          gate = pyauto.locateOnScreen(util.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_BOSS_NOT_FOUND)

      util.move(800, 400)
      util.do_fade()
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate_party(util.UNIT_GATE_FOUR)
      else: util.focus_gate(util.UNIT_GATE_FOUR)

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

        self.find_boss()
        try:
          boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(util.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(util.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.move(560, 260)
      util.do_dash()
      util.do_fade()

      # Final Boss
      util.wait(1)
      util.attack_boss(True, True, False, False)
      if util.get_party_member_status() == util.IS_FALSE: util.plunder_final_box()
      else: util.plunder_box_party()

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
    util.do_close_app_status()
