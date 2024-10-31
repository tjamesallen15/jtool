import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput import keyboard
from tkinter import *
from pynput.keyboard import Key, Listener, Controller

from common.dungeon import Dungeon
from common.dungeon import Special

import common.constants as consts
import common.util as util
import common.attack as atk

pynboard = Controller()

class MirageIsland(Dungeon, Special):
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

      # Click Dungeon
      util.move(630, 610)
      util.do_dash()
      util.do_fade()
      self.click_dungeon_portal(630, 440)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move(750, 190)
      util.do_dash()

      util.move(840, 215)
      util.do_fade()
      util.do_dash()

      util.move(650, 150)
      util.do_fade()
      util.do_dash()

      if util.get_party_member_status() == consts.IS_FALSE: self.click_dialog(590, 350, False)
      else: util.wait(2)

      util.move(1150, 400)
      util.do_dash(2)
      util.do_fade()

      # Attack Monsters (Crag Crab)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_CRAG_CRAB, 1, True)
      util.cancel_aura(1.5)

      # Attack Boss (Watchman Tolerant)
      self.find_kill_special_boss(consts.UNIT_WATCHMAN_TOLERANT)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: util.wait(4)

      util.move_scroll(375, 150, 700, 150, 0.5)

      util.move(475, 100)
      util.do_dash()
      util.do_fade()
      util.do_dash(2)

      # Attack Monsters (Border Crab)
      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 1, True)

      util.move(1200, 235)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade(3)

      util.move(775, 185)
      util.do_dash(4)
      util.do_fade()

      # Attack Monsters (Border Crab)
      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 1, True)

      util.move(575, 235)
      util.do_dash()

      util.move(155, 170)
      util.do_fade()
      util.do_dash(2)

      # Attack Monsters (Border Crab)
      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 1, True)

      util.move(155, 170)
      util.do_dash()
      util.do_fade()

      util.move(835, 120)
      util.do_dash()
      util.do_fade(2)

      util.move(575, 180)
      util.do_dash(2)

      # Attack Monsters (Border Crab)
      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 1, True)

      util.move(590, 255)
      util.do_dash(1.5)

      util.move(890, 250)
      util.do_dash()

      util.move(770, 175)
      util.do_fade()
      util.do_dash()

      util.move(740, 210)
      util.do_fade()

      # Attack Monsters (Crag Crab)
      self.attack_monsters(consts.UNIT_CRAG_CRAB, 1, True)
      util.cancel_aura(1.5)

      # Attack Boss (Crasio)
      self.find_kill_special_boss(consts.UNIT_CRASIO, True, 1.5)

      util.move(750, 240)
      util.do_dash()
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      util.move(990, 225)
      util.do_dash()

      util.move(1075, 80)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      self.click_portal(680, 325, False)

      util.move(510, 130)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(325, 260)
      util.do_dash()

      util.move(500, 110)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(725, 135)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(425, 115)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(615, 100)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      if util.get_party_member_status() == consts.IS_FALSE:
        util.move(935, 105)
        util.do_dash()
        util.do_fade()

        util.move(750, 115)
        util.do_dash()

        util.move(560, 190)
        util.do_fade()
        util.do_dash()

        self.click_dialog(570, 390, False)

        util.move(700, 635)
        util.do_dash()
        util.do_fade()

        util.move(485, 675)
        util.do_dash()

        util.move(390, 680)
        util.do_fade()
        util.do_dash()
      else:
        util.wait(8)

      # Attack Boss (Grogo)
      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GROGO)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: util.wait(4)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.move(515, 565)
        util.do_dash(1.5)
      else: util.wait(2)

      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.move(515, 55)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(255, 170)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(75, 335)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move_scroll(375, 150, 1000, 150, 0.5)

      util.move(930, 215)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(795, 75)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      if util.get_party_member_status() == consts.IS_FALSE:
        util.move(1045, 120)
        util.do_dash()
        util.do_fade()
        util.do_dash()

        util.move(705, 90)
        util.do_fade()
        util.do_dash()

        self.click_dialog(675, 350)

        util.move(575, 675)
        util.do_dash()
        util.do_fade()

        util.move(220, 695)
        util.do_dash()
        util.do_fade()
      else:
        util.move(715, 385, 1)
        util.do_fade()
        util.wait(5)

      self.find_kill_special_boss(consts.UNIT_GROGO_II)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box(True, 2)
      else: util.wait(0.2)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.move(420, 670)
        util.do_dash()

      util.move_scroll(1000, 150, 375, 150, 0.5)
      util.move(735, 85)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(715, 85)
      util.do_dash()
      util.do_fade()

      util.move(790, 160)
      util.do_dash()
      util.do_fade()

      util.move(990, 115)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(305, 330)
      util.do_dash()

      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GARLIARDO)
      if util.get_party_member_status() == consts.IS_FALSE: self.find_kill_box()
      else: self.find_kill_box_party()

      util.move(650, 270)
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move(885, 95)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(570, 80)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move(940, 85)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(795, 75)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(735, 70)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.move(540, 85)
      util.do_fade()
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GUARDIAN_GOLEM)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      util.move(570, 145)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      self.click_portal(575, 410)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      util.move_scroll(750, 150, 375, 150, 0.5)
      self.attack_monsters(consts.UNIT_GNELL, 1.5, True)

      util.move(630, 125)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      self.find_kill_special_boss(consts.UNIT_DARTHPENCIO)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      if util.get_party_member_status() == consts.IS_TRUE: util.wait(2)

      util.move(630, 125)
      util.do_dash()
      util.do_fade(1.5)
      util.do_fade()

      self.find_kill_special_boss(consts.UNIT_RULER_BARIALD)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_final_box()
      else: atk.plunder_final_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      wait_time = 1.5
      if util.get_party_leader_status() == consts.IS_TRUE: wait_time = 2

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(wait_time)
    util.do_close_app_status()

      