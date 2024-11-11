import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput import keyboard
from tkinter import *
from pynput.keyboard import Key, Listener, Controller

from common.dungeon import Dungeon

import common.constants as consts
import common.util as util
import common.attack as atk

pynboard = Controller()

class ChaosInfinity(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    fail_run_counter = 0
    while run_counter < runs:
      util.set_reset_status(False)
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(consts.MSG_START_DG)
      util.log_run(run_counter, fail_run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.release_keys()
      util.go_skill_slot(0.2)
      util.do_buffs()

      util.move(500, 300)
      util.do_dash()

      # Click Dungeon
      self.click_dungeon_portal(590, 390)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150, 0.5)

      util.log_action(consts.MSG_MOVING_POSITION)
      util.move(650, 250)
      util.do_dash()

      util.move(500, 360)
      util.do_fade()

      util.move(500, 360)
      util.do_dash()

      util.move(750, 150)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(550, 300)
      util.do_dash()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(600, 150)
      util.do_dash()
      util.do_fade()

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      has_gate = True
      while has_gate:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          has_gate = False

        if has_gate == False:
          break

        util.do_select(0.1)
        if util.get_party_member_status() == consts.IS_FALSE:
          try:
            gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
            atk.focus_gate(consts.UNIT_GATE, False)
            util.wait(0.3)
            has_gate = False
            break
          except pyauto.ImageNotFoundException:
            pass
        else:
          try:
            gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          except pyauto.ImageNotFoundException:
            util.wait(2)
            has_gate = False
            break

      try:
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        atk.focus_gate(consts.UNIT_GATE, False)
        util.wait(0.3)
      except pyauto.ImageNotFoundException:
        pass

      util.move(620, 150)
      util.do_dash()

      if util.get_party_member_status() == consts.IS_TRUE:
        util.do_fade()
      elif util.get_party_leader_status() == consts.IS_TRUE:
        util.do_fade(1)
        counter = 0
        while counter != 5:
          try:
            util.do_select(0.1)
            mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
            atk.focus_monsters(consts.UNIT_ARENA_MOBS, False, True, self.val_sidestep_disabled)
          except pyauto.ImageNotFoundException:
            pass
          counter += 1
      else:
        util.do_fade(5.5)

      util.move(620, 150)
      util.do_dash()
      util.do_fade()

      util.move(620, 325)
      util.do_dash()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # 12 bosses
      bosses = 0
      arena = True
      mob_checker = 0
      chaos_move = 0
      reposition_count = 0
      mob_threshold = 30
      check_left = 0
      check_right = 0

      if util.get_party_status() == consts.IS_TRUE:
        mob_threshold = 200

      while arena:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          arena = False

        if bosses >= 12:
          arena = False

        if reposition_count > 3:
          util.force_exit_dungeon()
          fail_run_counter += 1
          arena = False
          util.set_reset_status(True)

        if arena == False:
          break

        mob_checker += 1
        util.do_select(0.1)
        util.do_fast_plunder()
        util.do_final_mode()

        try:
          chaos_gate = pyauto.locateOnScreen(consts.IMG_CHAOS_GATE, grayscale=False, confidence=.7, region=util.get_full_region())

          if chaos_move == consts.STATE_ZERO:
            util.do_deselect_pack()
            self.chaos_reposition_top()
            chaos_move = 1
          else:
            util.do_deselect_pack()
            self.chaos_reposition_bottom()
            chaos_move = 0

        except pyauto.ImageNotFoundException:
          pass

        try:
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOSS_FOUND)
          atk.attack_boss(consts.UNIT_EMPTY, False, True)
          bosses += 1
          mob_checker = 0
          reposition_count = 0
          chaos_move = 0
          util.wait(0.2)

          if check_left == consts.STATE_ONE:
            util.move(1200, 400)
            util.do_dash()
            check_left = 0
          elif check_right == consts.STATE_ONE:
            util.move(100, 400)
            util.do_dash()
            check_right = 0

          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        try:
          box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_BOX_FOUND)
          mob_checker = 0
          reposition_count = 0
          chaos_move = 0
          atk.plunder_box(True, 3, True, 0)
          if util.get_party_status() == consts.IS_FALSE: util.wait(1.5)

        except pyauto.ImageNotFoundException:
          pass

        try:
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + consts.UNIT_ARENA_MOBS)
          mob_checker = 0

          if util.get_attack_type() == consts.IS_RANGE and util.get_access_level() == consts.ACCESS_SUPER: util.do_attack(0.1)
          else: atk.focus_monsters(consts.UNIT_ARENA_MOBS, False, True, self.val_sidestep_disabled)
        except pyauto.ImageNotFoundException:
          pass

        try:
          end_dungeon = pyauto.locateOnScreen(consts.IMG_END_DG, grayscale=False, confidence=.9)
          bosses += 12
        except pyauto.ImageNotFoundException:
          pass

        if mob_checker >= mob_threshold:
          mob_checker = 0
          util.cancel_aura(1.2)

          if reposition_count > 2:
            self.reposition_center()

          if bosses == 10 and reposition_count < 2:
            if reposition_count == 0:
              self.check_ulwaan_left()
              check_left = 1
            else:
              self.check_ulwaan_right()
              check_right = 1
          else:
            self.reposition_mobs()
          reposition_count += 1

      if util.get_reset_status():
        continue

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      wait_time = 1.5
      if util.get_party_member_status() == consts.IS_TRUE: wait_time = 2

      # Start to End Dungeon
      util.reset_battle_mode()
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(wait_time)
    util.do_close_app_status()

  def reposition_center(self):
    util.log_action(consts.MSG_MOVING_POSITION)
    # HORIZONTAL
    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    # VERTICAL
    util.move(620, 100)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    util.move(620, 600)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()

    # HORIZONTAL
    util.move(1200, 400)
    util.do_dash()
    util.do_fade()

    util.move(900, 400)
    util.do_dash(1.5)

  def reposition_ulwaan(self):
    # HORIZONTAL
    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()
    util.do_select(0.1)

    # HORIZONTAL
    util.move(1200, 400)
    util.do_dash()
    util.do_fade()

    util.move(875, 400)
    util.do_dash(1.5)
    util.do_select(0.1)

  def check_ulwaan_left(self):
    # HORIZONTAL
    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

    util.move(100, 360)
    util.do_fade()

    util.move(1200, 400)
    util.do_dash()

  def check_ulwaan_right(self):
    util.move(1200, 400)
    util.do_dash()

    util.move(1200, 360)
    util.do_fade()

    util.move(1200, 400)
    util.do_dash()

    util.move(1200, 360)
    util.do_fade()

    util.move(1200, 400)
    util.do_dash()

    util.move(1200, 360)
    util.do_fade()

    util.move(100, 400)
    util.do_dash()

  def reposition_mobs(self):
    # VERTICAL CHECK
    util.move(620, 100)
    util.do_dash()
    util.do_fade()
    util.do_select(0.1)

    util.move(620, 600)
    util.do_dash()
    util.do_fade()
    util.do_dash()
    util.do_fade()
    util.do_select(0.1)

    util.move(620, 250)
    util.do_dash()

    util.move(620, 300)
    util.do_fade()

  def chaos_reposition_top(self):
    util.move(620, 100)
    util.do_dash()
    util.do_fade()

  def chaos_reposition_bottom(self):
    util.move(620, 600)
    util.do_dash()
    util.do_fade()
