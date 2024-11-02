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

class TerminusMachina(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      util.log_action(consts.MSG_START_DG)
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
      self.click_dungeon_portal(600, 240)

      self.enter_dungeon()
      self.challenge_dungeon()
      util.move_scroll(700, 150, 375, 150, 0.5)

      util.move(630, 150)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade(1.5)
      util.do_dash(3)

      util.move(630, 550)
      util.do_dash()
      util.do_fade(1.5)
      util.do_dash()

      util.do_final_mode(1)
      util.do_aura(2)

      atk.attack_monsters(consts.UNIT_MECH_LION, False, consts.VAL_INTERVAL_DEFAULT, self.val_sidestep_disabled)

      util.move(630, 150)
      if util.get_attack_type() == consts.IS_MELEE: util.do_dash(3)
      else: util.do_dash()

      atk.attack_monsters(consts.UNIT_MECH_LION, False, consts.VAL_INTERVAL_DEFAULT, self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Mech Lion Sequence
      # moving = True
      # while moving:
      #   if not util.get_macro_state():
      #     util.log_action(consts.MSG_TERMINATE)
      #     moving = False

      #   if moving == False:
      #     break

      #   self.path_find(consts.UNIT_MECH_LION)
      #   try:
      #     boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      #     moving = False
      #     util.log_action(consts.MSG_MOVE_STOP)
      #     break
      #   except pyauto.ImageNotFoundException:
      #     util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # # Check Macro State
      # if not util.get_macro_state():
      #   run_counter += 1000
      #   continue

      # First Boss
      # util.do_deselect_pack()
      # util.move(700, 260)
      util.do_battle_mode()
      util.move(630, 150)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      # util.do_battle_mode()
      util.do_short_buffs()
      atk.attack_boss(True, True, False, False)
      atk.plunder_box()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      # util.move(710, 260)
      # util.do_dash()
      # util.do_fade()

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
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_GATE_ONE)
      else: atk.focus_gate(consts.UNIT_GATE_ONE)
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
      util.do_fade(3)

      util.move(500, 150)
      util.do_dash(2)

      util.do_fade()

      util.move(500, 420)
      util.do_fade(1)

      if util.get_attack_type() == consts.IS_MELEE: util.wait(7)
      else: util.wait(2)

      atk.attack_monsters(consts.UNIT_MECH_LIHONAR, True, 0.3, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(530, 150)
      util.do_dash()

      if util.get_attack_type() == consts.IS_MELEE:
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
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_GATE_TWO)
      else: atk.focus_gate(consts.UNIT_GATE_TWO)
      util.wait(0.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(650, 260)
      util.do_dash()

      util.move(590, 260)
      util.do_fade()
      util.do_dash()

      util.do_select(0.1)
      atk.focus_monsters(consts.UNIT_ESPADA_1, False, True, self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(800, 380)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == consts.IS_MELEE: util.wait(8)
      else: util.wait(1)

      util.move(500, 380)
      util.do_dash()

      # Espada I Sequence
      power_ticks = 0
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        util.do_select(0.1)
        try:
          mobs = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          power_ticks += 1
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        if power_ticks > 10:
          checking = False

        if checking == False:
          break

        try:
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + consts.UNIT_ESPADA_1)
          atk.focus_monsters(consts.UNIT_ESPADA_1, False, True, self.val_sidestep_disabled)
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_CLEARED)
          power_ticks += 1

        if power_ticks > 10:
          checking = False

        if checking == False:
          break

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(130, 225)
      util.do_dash()
      util.do_fade()

      util.move(360, 430)
      util.do_dash()

      # util.move(550, 380)
      # util.do_dash()
      # util.do_fade()

      # util.move(680, 150)
      # util.do_dash()
      # util.do_fade()

      # util.move(680, 150)
      # util.do_dash()
      # util.do_fade()

      # util.move(1000, 400)
      # util.do_dash()
      # util.do_fade()

      # util.move(320, 500)
      # util.do_dash()
      # util.do_fade()

      # util.move(320, 500)
      # util.do_dash()
      # util.do_fade()

      # util.move(320, 500)
      # util.do_dash()
      # util.do_fade()

      # Power Supply
      util.do_select(0.1)
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_POWER_SUPPLY)
      else: atk.focus_gate(consts.UNIT_POWER_SUPPLY)

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
      if util.get_attack_type() == consts.IS_MELEE: util.wait(8)
      else: util.wait(2)

      # Espada II Sequence
      atk.attack_monsters(consts.UNIT_ESPADA_2, True, 0.3, False)
      # util.cancel_aura(1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(540, 150)
      util.do_dash()
      util.do_fade()

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      # Power Supply II
      util.do_select(0.1)
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_POWER_SUPPLY)
      else: atk.focus_gate(consts.UNIT_POWER_SUPPLY)

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
      util.do_fade(1.5)
      util.do_dash(2.5)
      util.do_fade()
      if util.get_attack_type() == consts.IS_MELEE: util.wait(12)
      else: util.wait(1)

      # Espada III Sequence
      power_ticks = 0
      checking = True
      while checking:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          checking = False

        util.do_select(0.1)
        try:
          mobs = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
          power_ticks += 1
          util.do_select(0.1)
        except pyauto.ImageNotFoundException:
          pass

        if power_ticks > 20:
          checking = False

        if checking == False:
          break

        try:
          mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_MONSTERS_FOUND + consts.UNIT_ESPADA_3)
          if util.get_attack_type() == consts.IS_MELEE: atk.focus_monsters(consts.UNIT_ESPADA_3, False, False, self.val_sidestep_disabled)
          else: atk.focus_monsters(consts.UNIT_ESPADA_3, False, True, self.val_sidestep_disabled)
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_MONSTERS_CLEARED)
          power_ticks += 1

        if power_ticks > 20:
          checking = False

        if checking == False:
          break

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.cancel_aura(1.5)
      util.move(350, 250)
      util.do_dash()
      util.do_fade()

      util.move(450, 250)
      util.do_dash()
      util.do_fade()

      # Power Supply III
      util.do_select(0.1)
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_POWER_SUPPLY)
      else: atk.focus_gate(consts.UNIT_POWER_SUPPLY)
      util.wait(0.4)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(900, 300)
      util.do_dash()
      util.do_fade()
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

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
      if util.get_attack_type() == consts.IS_MELEE: util.wait(4)
      else: util.wait(2)

      util.move(400, 400)
      util.do_dash()

      util.move(640, 150)
      util.do_dash()
      util.do_fade(1.5)

      util.move(620, 600)
      util.do_dash()
      util.do_fade()
      util.do_dash(2)

      # Poerte Sequence
      atk.attack_monsters(consts.UNIT_POERTE, False, 0.3, self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.do_battle_mode()
      util.do_short_buffs()

      util.move(580, 260)
      util.do_dash()
      util.do_fade(1.2)
      util.do_fade()

      # Second Boss
      atk.attack_boss(True, True, False, False)
      util.wait(0.5)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

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
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_GATE_THREE)
      else: atk.focus_gate(consts.UNIT_GATE_THREE)
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
      util.do_fade(3)

      util.move(590, 150)
      util.do_dash()

      if util.get_attack_type() == consts.IS_MELEE:
        util.wait(5)
        atk.attack_monsters(consts.UNIT_REDONNO, False, consts.VAL_INTERVAL_MELEE, self.val_sidestep_disabled)
      else:
        util.wait(1)
        atk.attack_monsters(consts.UNIT_REDONNO, True, consts.VAL_INTERVAL_DEFAULT, self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(710, 190)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      # # Redonno Sequence
      # moving = True
      # while moving:
      #   if not util.get_macro_state():
      #     util.log_action(consts.MSG_TERMINATE)
      #     moving = False

      #   if moving == False:
      #     break

      #   self.path_find(consts.UNIT_REDONNO)
      #   try:
      #     boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      #     moving = False
      #     util.log_action(consts.MSG_MOVE_STOP)
      #     break
      #   except pyauto.ImageNotFoundException:
      #     util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # util.do_deselect_pack()
      # if util.get_attack_type() == consts.IS_MELEE:
      #   util.move(750, 150)
      #   util.do_dash()
      #   util.do_fade()
      # else:
      #   util.move(950, 150)
      #   util.do_dash()
      #   util.do_fade()

      # Third Boss
      atk.attack_boss()
      util.set_battle_mode(False)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box(True, 4, False)
      else: atk.plunder_box_party()

      # util.move(670, 150)
      # util.do_dash()
      # util.do_fade()

      util.move(630, 150)
      util.do_dash()
      util.do_fade()

      util.move(945, 355)
      util.do_dash()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Gate IV
      if util.get_party_leader_status() == consts.IS_TRUE: util.wait(5)
      moving = True
      while moving:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        gate_counter = self.find_gate(consts.UNIT_GATE_FOUR)

        try:
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(consts.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BOSS_NOT_FOUND)

      util.move(800, 400)
      util.do_fade()
      if util.get_party_member_status() == consts.IS_TRUE: atk.focus_gate_party(consts.UNIT_GATE_FOUR)
      else: atk.focus_gate(consts.UNIT_GATE_FOUR)

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
          util.log_action(consts.MSG_TERMINATE)
          moving = False

        if moving == False:
          break

        self.find_boss()
        try:
          boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
          moving = False
          util.log_action(consts.MSG_MOVE_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BOSS_NOT_FOUND)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_deselect_pack()
      util.move(560, 260)
      util.do_dash()
      util.do_fade(1.2)
      util.do_fade()

      # Final Boss
      atk.attack_boss(True, True, False, False)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_final_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.set_battle_mode(False)

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time()
    util.do_close_app_status()

  def path_find(self, unit=consts.UNIT_EMPTY):
    pathing = True
    boss_found = 0
    backtrack_counter = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      util.log_action(consts.MSG_PATH_FIND + unit)

      if unit == consts.UNIT_REDONNO:
        backtrack_counter += 1
        util.log_action(consts.MSG_BACKTRACK + str(backtrack_counter))
        if (backtrack_counter >= 10):
          backtrack_counter = 0
          self.path_backtrack(unit)

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(580, 260, 0.5)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(620, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(560, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(640, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_MONSTERS_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

      try:
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

      if pathing == False:
        break

    if boss_found == consts.STATE_ZERO:
      atk.focus_monsters(unit, False, True, self.val_sidestep_disabled)

  def path_backtrack(self, unit):
    util.log_action(consts.MSG_BACKTRACK + unit)
    util.move(630, 600)
    util.do_dash()
    util.do_fade()

    util.move(630, 600)
    util.do_dash()
    util.do_fade()

  def find_gate(self, unit=consts.UNIT_EMPTY):
    pathing = True
    gate_counter = 0
    while pathing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        pathing = False

      if pathing == False:
          break

      util.log_action(consts.MSG_PATH_FIND + unit)
      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_GATE_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(580, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_GATE_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(620, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_GATE_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(540, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_GATE_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(660, 260)
        util.do_select(0.1)
        gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_GATE_FOUND + unit)
        pathing = False
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_GATE_NOT_FOUND)

      if pathing == False:
        break

      if unit == consts.UNIT_GATE_FOUR or unit == consts.UNIT_GATE_TWO:
        try:
          util.move_click(450, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(500, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(550, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(700, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(750, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(800, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(850, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(900, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

        try:
          util.move_click(1000, 260)
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
          util.log_action(consts.MSG_GATE_FOUND + unit)
          pathing = False
          util.log_action(consts.MSG_PATH_STOP)
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_GATE_NOT_FOUND)

        if pathing == False:
          break

      util.move_click(705, 450, 2)
      util.move_click(705, 250, 1.5)

    return gate_counter

  def find_boss(self):
    pathing = True
    boss_found = 0
    util.log_action(consts.MSG_CHECK_BOSS)
    while pathing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        pathing = False

      if pathing == False:
        break

      try:
        util.move_click(600, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(620, 260)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(580, 160)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(660, 160)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break

      try:
        util.move_click(540, 160)
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BOSS_FOUND)
        pathing = False
        boss_found = 1
        util.log_action(consts.MSG_PATH_STOP)
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BOSS_NOT_FOUND)

      if pathing == False:
        break
