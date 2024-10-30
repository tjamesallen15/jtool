import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from common.dungeon import Dungeon
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from tkinter import *

import common.util as util
pynboard = Controller()

class PurifierOfTheForest(Dungeon):

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

  def find_kill_boss(self, unit_image, unit_name, cancel=True):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(unit_image, grayscale=False, confidence=.7, region=util.get_archer_region())
        util.focus_high_boss(unit_name, False, True, False)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    util.wait(0.5)
    if cancel == util.IS_TRUE: util.cancel_aura(1.5)

  def find_kill_special_boss(self, unit_name):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_archer_region())
        util.focus_high_boss(unit_name, False, True, True)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    util.wait(0.5)
    util.cancel_aura(1.5)

  def find_kill_mobs(self, unit_image, unit_name):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(unit_image, grayscale=False, confidence=.7, region=util.get_archer_region())
        util.focus_high_mobs(unit_name, False)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    util.wait(0.5)

  def go_portal(self, x, y, deviate=False):
    check_dialog = True
    while check_dialog:
      if not util.get_macro_state():
        util.log_action(util.MSG_TERMINATE)
        check_dialog = False

      if check_dialog == False:
        break

      try:
        util.move_click(x, y, 0.2)
        if deviate == util.IS_TRUE:
          util.move_click(x - 10, y, 0.2)
          util.move_click(x + 10, y, 0.2)
        dialog = pyauto.locateOnScreen(util.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(util.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        check_dialog = False
      except pyauto.ImageNotFoundException:
        pass

  def attack_monsters(self, unit_name, sec=1, aura=False):
    util.attack_mobs(unit_name, aura, 0.3, False)
    util.wait(sec)

  def focus_monsters(self, unit_name, reps=4, sec=1, aura=False):
    for x in range(reps):
      util.focus_mobs(unit_name, True, aura, False)

    util.wait(sec)

  def go_web_gate(self):
    util.move(735, 200)
    util.do_fade()
    util.force_veradrix()
    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.move(820, 200)
    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.move(250, 200)
    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.move(350, 300)
    util.do_dash()
    util.do_fade()
    util.force_veradrix()

    util.move(415, 275)
    util.do_dash()

    util.move(435, 275)
    util.do_fade()
    util.force_veradrix()

    util.move(550, 275)
    util.do_dash()

    util.move(475, 300)
    util.do_fade()
    util.force_veradrix()
    util.do_dash()

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
      util.cancel_buffs()
      util.do_buffs()

      # Click Dungeon
      util.move(677, 361)
      util.move(735, 361, 0.5)
      util.click_portal(735, 361)

      # Enter Dungeon
      util.enter_dungeon()
      util.challenge_dungeon(1)

      util.move(1000, 330)
      util.do_dash()
      util.do_fade()

      util.move_click(1000, 400, 2.5)

      util.move(1000, 400)
      util.do_dash()

      util.move(820, 600)
      util.do_fade()

      util.move(830, 600)
      util.do_dash()

      # Attack First Boss (Bloody Sweeper)
      self.find_kill_boss(util.IMG_BLOODY_SWEEPER, util.UNIT_BLOODY_SWEEPER)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(780, 200)
      util.do_dash()

      util.move_click(1000, 200, 5)

      util.move(1100, 400)
      util.do_dash()
      util.do_fade()

      if util.get_attack_type() == util.IS_MELEE: util.wait(7)
      else: util.wait(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(util.UNIT_BLOODY_HORN, 4, 6, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      self.focus_monsters(util.UNIT_BLOODY_HORN, 4, 1, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(625, 440)
      util.do_fade()

      util.move_click(1050, 435, 5)

      util.move(660, 450)
      if util.get_attack_type() == util.IS_MELEE: util.do_fade(3)
      else: util.do_fade()
      util.cancel_aura(1.5)

      # Attack Second Boss (Bloody Fang)
      self.find_kill_boss(util.IMG_BLOODY_FANG, util.UNIT_BLOODY_FANG)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(825, 600)
      util.do_dash()
      if util.get_party_member_status() == util.IS_TRUE: util.plunder_box()
      else: util.party_roll_box()

      util.move(720, 500)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      # First Portal
      self.go_portal(650, 400, True)
      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.move(525, 175)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == util.IS_MELEE: util.wait(6)
      else: util.wait(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(util.UNIT_KORAIDER, 3, 1, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_click(1050, 325, 4)
      util.move(1000, 600)
      util.do_dash()
      util.do_fade()

      util.move(800, 400)
      util.do_dash()

      util.move(1050, 325)
      util.do_fade(3)

      util.move(1050, 325)
      util.do_dash(2)
      util.do_fade(2)
      util.do_dash()

      if util.get_attack_type() == util.IS_MELEE:
        util.move(400, 475)
        util.do_dash()

      self.focus_monsters(util.UNIT_MUTANT_KORAIDER, 2, 1, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.cancel_aura(1.5)

      # Move to Beelzebub Boss
      util.move(1050, 325)
      util.do_dash()
      util.do_fade()

      util.move_click(750, 200, 4)
      util.move_click(900, 200, 4)

      util.move(660, 100)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == util.IS_MELEE:
        util.wait(8)

        util.move(600, 600)
        util.do_fade()
      else: util.wait(3)

      # Attack Third Boss
      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(util.IMG_BEELZEBUB, util.UNIT_BEELZEBUB)
      util.move_scroll(375, 150, 700, 150, 0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Electrishia Base
      util.move(660, 100)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(600, 600)
      util.do_dash(1.5)

      util.move(425, 350)
      util.do_dash(1.5)

      if util.get_party_member_status() == util.IS_TRUE: util.plunder_box()
      else: util.party_roll_box()

      util.move(100, 325)
      util.do_dash()

      util.move(300, 400)
      util.do_fade()

      if util.get_party_member_status() == util.IS_TRUE: util.wait(12)
      util.wait(3)

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move_click(755, 210, 5)
      util.move_click(510, 200, 7)
      util.move_click(800, 300, 3)
      util.move_scroll(375, 150, 700, 150, 0.5)

      util.move_click(775, 130, 4)

      if util.get_party_member_status() == util.IS_TRUE:
        util.move(910, 200)
        util.do_dash(2)
        util.do_fade(4)

        util.do_dash(2)
        util.do_fade(3)

        util.do_dash()
        util.do_fade(5)

        util.move(450, 550)
        util.do_dash()
      else:
        util.move(910, 200)
        util.do_dash()
        util.do_fade()

        util.do_dash()
        util.do_fade()

        util.do_dash()
        util.do_fade()

        util.move(450, 550)
        util.do_dash()

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(util.UNIT_ELECTRISHIA, 1, True)

      util.move(450, 550)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(util.UNIT_ELECTRISHIA, 1, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Web Gate
      util.move(910, 200)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.cancel_aura(1.5)

      util.move_scroll(375, 150, 700, 150, 0.5)

      self.go_web_gate()

      check_gate = True
      while check_gate:
        if not util.get_macro_state():
          util.log_action(util.MSG_TERMINATE)
          check_gate = False

        if check_gate == False:
          break

        try:
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(util.IMG_WEB_GATE, grayscale=False, confidence=.7, region=util.get_archer_region())
          check_gate = False
          break
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()
          self.go_web_gate()

      # Attack Web Gate
      if util.get_party_leader_status() == util.IS_TRUE: util.wait(2)
      if util.get_party_member_status() == util.IS_TRUE: util.focus_gate(util.UNIT_WEB_GATE, 0)
      else: util.wait(8)

      if util.get_party_status() == util.IS_TRUE: util.wait(5)
      else: util.wait(2)

      util.move(675, 300)
      util.do_fade(5)
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.5)
      # util.move(650, 420)
      # util.do_fade()

      # Attack Fourth Boss (Electula)
      self.find_kill_boss(util.IMG_ELECTULA, util.UNIT_ELECTULA)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # util.move(1000, 425)
      util.move(835, 425)
      util.do_dash()
      util.do_fade()
      if util.get_party_member_status() == util.IS_TRUE:
        util.do_select(0.1)
        util.plunder_box()
      else:
        util.party_roll_box()

      util.wait(10)

      # Move to Ant Base
      util.move_click(1125, 325, 5)
      util.move_scroll(375, 150, 700, 150, 0.5)
      util.move_click(760, 205, 5)
      util.move_scroll(375, 150, 700, 150, 0.5)
      util.move_click(560, 175, 5)

      util.do_final_mode(2)
      util.do_aura(2)
      util.set_last_cast_mode(3)

      if util.get_party_member_status() == util.IS_TRUE: util.move_click(900, 235, 7)
      else: util.move_click(900, 235, 4)

      # Attack First Ant Hill
      util.move(1050, 340)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      util.move(690, 380)
      util.do_dash()
      self.find_kill_mobs(util.IMG_FULL_ANT_HILL, util.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Second Ant Hill
      util.move(1050, 470)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      self.find_kill_mobs(util.IMG_FULL_ANT_HILL, util.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Third Ant Hill
      util.move(690, 290)
      util.do_dash()
      util.force_veradrix()
      self.find_kill_mobs(util.IMG_FULL_ANT_HILL, util.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Fourth Ant Hill
      util.move(340, 300)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      self.find_kill_mobs(util.IMG_FULL_ANT_HILL, util.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(800, 350)
      util.do_dash()
      util.move(640, 250)
      util.do_fade()
      util.force_veradrix()
      util.cancel_aura(1.5)

      # Attack Fifth Boss (Queen Ripley)
      self.find_kill_boss(util.IMG_QUEEN_RIPLEY, util.UNIT_QUEEN_RIPLEY)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == util.IS_TRUE:
        finding = True
        while finding:
          if not util.get_macro_state():
            util.log_action(util.MSG_TERMINATE)
            finding = False

          if finding == False:
            break

          try:
            util.force_veradrix()
            util.do_select(0.1)
            box = pyauto.locateOnScreen(util.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
            util.plunder_box(False)
            finding = False
            break
          except pyauto.ImageNotFoundException:
            pass
      else:
        util.party_roll_box()

      util.move(620, 200)
      util.do_dash()
      util.do_fade()

      # Second Portal
      self.go_portal(580, 300, True)
      util.move(660, 275)
      util.do_dash()

      # Attack Final Boss
      self.find_kill_special_boss(util.UNIT_OMERAI)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == util.IS_TRUE:
        util.do_plunder(3)
        util.wait(2)
      else:
        util.wait(4)

      util.move(300, 600)
      util.do_dash()
      util.do_fade()

      util.move(550, 600)
      util.do_dash()
      util.do_fade()

      if util.get_party_member_status() == util.IS_TRUE: util.plunder_final_box()
      else: util.party_roll_box()

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
    util.do_close_app_status()

