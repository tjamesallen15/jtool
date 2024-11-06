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
    wait_time = 1.5
    if util.get_party_leader_status() == consts.IS_TRUE: wait_time = 2
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
      util.do_dash_rel(630, 610)
      util.do_fade_rel(630, 610)
      self.click_dungeon_portal(630, 440)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(700, 150, 375, 150, 0.5)
      if util.get_party_member_status() == consts.IS_TRUE: util.wait(6)

      util.do_dash_rel(750, 190)

      util.do_fade_rel(840, 215)
      util.do_dash_rel(840, 215)

      util.do_fade_rel(650, 150)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(650, 150)
        self.click_dialog(590, 350, False)
        util.do_dash_rel(1150, 400, 2)
        util.do_fade_rel(1150, 400, 2)
      else:
        util.do_dash_rel(650, 150, 1.5)
        util.do_dash_rel(1150, 400, 1.5)
        util.do_dash_rel(1150, 400, 2)

      # Attack Monsters (Crag Crab)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_CRAG_CRAB, 2.0, True)
      util.cancel_aura(2.0)

      # Attack Boss (Watchman Tolerant)
      self.find_kill_special_boss(consts.UNIT_TOLERANT)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: util.do_fade_rel(1150, 400, 4.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(375, 150, 700, 150, 0.5)

      util.do_dash_rel(475, 100)
      util.do_fade_rel(475, 100)
      util.do_dash_rel(475, 100, 4)

      # Attack Monsters (Border Crab)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 2.0, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(1200, 235)
      util.do_fade_rel(1200, 235)
      util.do_dash_rel(1200, 235)
      util.do_fade_rel(1200, 235, 3)

      util.do_dash_rel(775, 185, 4)
      util.do_fade_rel(775, 185)

      # Attack Monsters (Border Crab)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 2.0, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(575, 235)
      util.do_fade_rel(155, 170, 2)
      util.do_dash_rel(155, 170, 2)

      # Attack Monsters (Border Crab)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 2.0, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(155, 170)
      util.do_fade_rel(155, 170)

      util.do_dash_rel(835, 120, 3)
      util.do_fade_rel(835, 120, 2)

      util.do_dash_rel(575, 180, 2)

      # Attack Monsters (Border Crab)
      self.attack_monsters(consts.UNIT_BORDER_CRAB, 2.0, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(590, 255, 1.5)
      util.do_dash_rel(890, 250)

      util.do_fade_rel(770, 175)
      util.do_dash_rel(770, 175, 2)

      util.do_fade_rel(740, 210)

      # Attack Monsters (Crag Crab)
      self.attack_monsters(consts.UNIT_CRAG_CRAB, 2.0, False)

      if util.get_party_member_status() == consts.IS_FALSE: util.do_dash_rel(750, 240)

      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Boss (Crasio)
      self.find_kill_special_boss(consts.UNIT_CRASIO, True, 3)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else:
        atk.plunder_box_party()
        util.do_dash_rel(750, 240, 1.5)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(990, 225)

      util.do_fade_rel(1075, 80)
      util.do_dash_rel(1075, 80)
      util.do_fade_rel(1075, 80)
      util.do_dash_rel(1075, 80)
      util.do_fade_rel(1075, 80)
      self.click_portal(520, 415, False, 2)

      util.do_dash_rel(510, 130)
      util.do_fade_rel(510, 130)
      util.do_dash_rel(510, 130)
      util.do_fade_rel(510, 130)

      util.do_dash_rel(325, 260)
      util.do_fade_rel(500, 110)
      util.do_dash_rel(500, 110)
      util.do_fade_rel(500, 110)

      util.do_dash_rel(500, 110)

      util.do_fade_rel(725, 135)
      util.do_dash_rel(725, 135)
      util.do_fade_rel(725, 135)

      util.do_dash_rel(425, 115)
      util.do_fade_rel(425, 115)
      util.do_dash_rel(425, 115)
      util.do_fade_rel(425, 115)
      util.do_dash_rel(425, 115)

      util.do_fade_rel(615, 100)
      util.do_dash_rel(615, 100)
      util.do_fade_rel(615, 100)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(935, 105)
        util.do_fade_rel(935, 105)

        util.do_dash_rel(750, 115)
        util.do_fade_rel(560, 190)
        util.do_dash_rel(560, 190)

        self.click_dialog(570, 390, False)

        util.do_dash_rel(700, 635)
        util.do_fade_rel(700, 635)
        util.do_dash_rel(485, 675)
        util.do_fade_rel(390, 680)
        util.do_dash_rel(390, 680)
      else:
        util.wait(8)

      # Attack Boss (Grogo)
      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GROGO)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: util.wait(4)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(515, 565, 1.5)
      else: util.wait(2)

      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.do_dash_rel(515, 55)
      util.do_fade_rel(515, 55)
      util.do_dash_rel(515, 55)
      util.do_fade_rel(515, 55)

      util.do_dash_rel(255, 170)
      util.do_fade_rel(255, 170)
      util.do_dash_rel(255, 170)
      util.do_fade_rel(255, 170)

      util.do_dash_rel(75, 335)
      util.do_fade_rel(75, 335)
      util.do_dash_rel(75, 335)

      util.move_scroll(375, 150, 1000, 150, 0.5)

      util.do_fade_rel(930, 215)
      util.do_dash_rel(930, 215)
      util.do_fade_rel(930, 215)
      util.do_dash_rel(930, 215)

      util.do_fade_rel(795, 75)
      util.do_dash_rel(795, 75)
      util.do_fade_rel(795, 75)
      util.do_dash_rel(795, 75)
      util.do_fade_rel(795, 75)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(1045, 120)
        util.do_fade_rel(1045, 120)
        util.do_dash_rel(1045, 120)

        util.do_fade_rel(705, 90)
        util.do_dash_rel(705, 90)

        self.click_dialog(675, 350)

        util.do_dash_rel(575, 675)
        util.do_fade_rel(575, 675)

        util.do_dash_rel(220, 695)

        util.do_fade_rel(510, 555)

        util.do_dash_rel(505, 170)
        util.do_fade_rel(505, 170)
      else:
        util.do_dash_rel(1045, 120, 9)

        util.do_dash_rel(505, 170)
        util.do_fade_rel(505, 170, 3.5)

      self.find_kill_special_boss(consts.UNIT_GROGO_II)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue


      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(765, 725)
        atk.plunder_box(True, 2)
      else: util.do_dash_rel(765, 725, 1.5)

      util.do_dash_rel(745, 610, 1.5)

      util.do_dash_rel(440, 625)

      util.move_scroll(1000, 150, 375, 150, 0.5)
      util.do_dash_rel(735, 85)
      util.do_fade_rel(735, 85)
      util.do_dash_rel(735, 85)
      util.do_fade_rel(735, 85)

      util.do_dash_rel(715, 85)
      util.do_fade_rel(715, 85)

      util.do_dash_rel(790, 160)
      util.do_fade_rel(790, 160)

      util.do_dash_rel(990, 115)
      util.do_fade_rel(990, 115)
      util.do_dash_rel(990, 115)
      util.do_fade_rel(990, 115)

      util.do_dash_rel(305, 330)

      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GARLIARDO)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: self.find_kill_box()
      else: atk.plunder_final_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(650, 270)

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.do_dash_rel(885, 95)
      util.do_fade_rel(885, 95)
      util.do_dash_rel(885, 95)
      util.do_fade_rel(885, 95)

      util.do_dash_rel(570, 80)
      util.do_fade_rel(570, 80)
      util.do_dash_rel(570, 80)

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.do_fade_rel(940, 85)
      util.do_dash_rel(940, 85)
      util.do_fade_rel(940, 85)
      util.do_dash_rel(940, 85)

      util.do_fade_rel(795, 75)
      util.do_dash_rel(795, 75)
      util.do_fade_rel(795, 75)
      util.do_dash_rel(795, 75)
      util.do_fade_rel(795, 75)

      util.do_dash_rel(735, 70)
      util.do_fade_rel(735, 70)
      util.do_dash_rel(735, 70)
      util.do_fade_rel(735, 70)
      util.do_dash_rel(735, 70)

      util.do_fade_rel(540, 85)
      util.do_dash_rel(540, 85)
      util.do_fade_rel(540, 85)

      if util.get_party_member_status() == consts.IS_FALSE: util.do_dash_rel(540, 85)

      util.set_last_cast_mode(3)
      self.find_kill_special_boss(consts.UNIT_GUARDIAN_GOLEM)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_TRUE: util.do_dash_rel(540, 85, 1.5)

      util.do_dash_rel(570, 145)
      util.do_fade_rel(570, 145)
      util.do_dash_rel(570, 145)

      self.click_portal(575, 410)
      util.move_scroll(750, 150, 375, 150, 0.5)

      if util.get_party_status() == consts.IS_TRUE:
        util.do_final_mode(1)
        util.set_last_cast_mode(2)
        self.attack_monsters(consts.UNIT_GNELL, 2.0, True)
      else:
        self.attack_monsters(consts.UNIT_GNELL, 2.0, False)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(630, 125)
      self.find_kill_special_boss(consts.UNIT_DARTHPENCIO, True, 3)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(630, 600)
      util.do_fade_rel(630, 600)
      util.do_dash_rel(630, 600)
      util.do_fade_rel(630, 600)

      util.do_dash_rel(630, 125)
      util.do_fade_rel(630, 125)
      util.do_dash_rel(630, 125)

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_TRUE: util.wait(2)

      util.do_dash_rel(630, 125)
      util.do_fade_rel(630, 125)

      util.do_dash_rel(630, 250)

      if util.get_party_member_status() == consts.IS_FALSE: util.do_fade_rel(630, 250)

      self.find_kill_special_boss(consts.UNIT_RULER_BARIALD)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_final_box()
      else: atk.plunder_final_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(wait_time)
    util.do_close_app_status()

      