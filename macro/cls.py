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

class Celestia(Dungeon, Special):

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
      util.move(628, 482)
      util.do_dash()
      self.click_dungeon_portal(600, 351)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()

      util.move_scroll(700, 150, 375, 150)
      util.move(616, 268)
      util.do_dash()
      util.move(608, 307)
      util.do_fade()
      util.move(606, 314)
      util.do_dash()
      self.click_portal(606, 328)

      util.move(577, 301)
      util.do_fade()

      # First Boss
      util.set_last_cast_mode(3)
      self.find_kill_semi_boss(consts.UNIT_FLA_3571)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(670, 607)
      util.do_dash()

      util.move_scroll(375, 150, 1000, 150)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(644, 161)
      util.do_dash()
      util.move(629, 225)
      util.do_fade()
      util.move(620, 243)
      util.do_dash()
      util.move(495, 276)
      util.do_fade()
      util.move(500, 291)
      util.do_dash()
      util.move(845, 209)
      util.do_fade()
      util.move(820, 205)
      util.do_dash()
      util.move(584, 243)
      util.do_fade()

      # Attack Monad Group
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.attack_monsters(consts.UNIT_MONAD_FRAGMENT, sidestep=self.val_sidestep_disabled, type=consts.TYPE_SEMI)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(655, 505)
      util.do_dash()
      util.move(547, 640)
      util.do_fade()
      util.move(547, 640)
      util.do_dash()
      util.move(412, 524)
      util.do_fade()
      util.move(412, 524)
      util.do_dash()
      util.move(586, 474)
      util.do_fade()
      util.move(783, 537)
      util.do_dash()
      util.move(577, 594)
      util.do_fade()
      util.move(637, 607)
      util.do_dash()
      util.move(636, 607)
      util.do_fade()
      util.move(577, 601)
      util.do_dash()

      util.countdown_timer(30)

      util.move(644, 161)
      util.do_dash()
      util.move(629, 225)
      util.do_fade()
      util.move(620, 243)
      util.do_dash()
      util.move(495, 276)
      util.do_fade()
      util.move(500, 291)
      util.do_dash()
      util.move(845, 209)
      util.do_fade()
      util.move(820, 205)
      util.do_dash()
      util.move(584, 243)
      util.do_fade()

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.attack_monsters(consts.UNIT_MONAD_FRAGMENT, sidestep=self.val_sidestep_disabled, type=consts.TYPE_SEMI)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Monad
      self.find_kill_semi_boss(consts.UNIT_MONAD)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(661, 311)
      util.do_dash()
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(684, 233)
      util.do_fade()
      util.move(684, 241)
      util.do_dash()
      util.move(652, 261)
      util.do_fade()
      self.click_portal(652, 294)

      util.move(631, 596)
      util.do_dash()
      util.move_scroll(375, 150, 1100, 150)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.focus_monsters(consts.UNIT_SEEKER, 6)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Aion
      self.find_kill_semi_boss(consts.UNIT_AION)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(707, 393)
      util.do_fade()
      util.move(648, 121)
      util.do_dash()
      util.move(616, 169)
      util.do_fade()
      util.move(626, 197)
      util.do_dash()
      util.move(617, 277)
      util.do_fade()
      util.move(615, 226)
      util.do_dash()

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_SERVANT, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(625, 614)
      util.do_fade(2)
      util.force_veradrix()
      util.move(656, 560)
      util.do_dash(3)
      util.force_veradrix()
      util.move(584, 364)
      util.do_fade(3)
      util.force_veradrix()

      atk.attack_monsters(consts.UNIT_SERVANT, sidestep=self.val_sidestep_disabled, type=consts.TYPE_SEMI)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(637, 170)
      util.do_dash()
      util.move(624, 218)
      util.do_fade(2)
      util.move(637, 617)
      util.do_fade(2)
      util.move(647, 638)
      util.do_dash(2)
      util.move(695, 547)
      util.do_fade(2)
      util.move(632, 579)
      util.do_dash(4)
      util.move(637, 268)
      util.do_fade()

      self.find_kill_semi_boss(consts.UNIT_VITO)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(609, 256)
      util.do_fade(1.5)
      util.move(607, 265)
      util.do_fade()
      util.move(672, 251)
      util.do_dash()

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(569, 198)
      util.do_dash()
      util.move(548, 205)
      util.do_fade()
      util.move(576, 203)
      util.do_dash()
      self.click_portal(614, 291)
      util.move_scroll(500, 150, 375, 150, 5)

      util.move(159, 245)
      util.do_dash()
      util.move(255, 260)
      util.do_fade()
      util.move(296, 270)
      util.do_dash()
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(910, 706)
      util.do_dash()
      util.move(643, 590)
      util.do_fade()
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(654, 625)
      util.do_dash()
      util.move(728, 611)
      util.do_fade()
      util.move(665, 590)
      util.do_dash()
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(575, 546)
      util.do_dash(5)
      util.move(586, 304)
      util.do_fade()

      self.find_kill_special_boss(consts.UNIT_PERIUS)
      util.do_plunder(2)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(604, 151)
      util.do_dash()
      util.move(626, 244)
      util.do_fade()
      util.move(618, 237)
      util.do_dash()

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_final_box()
      else: atk.plunder_final_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move_scroll(375, 150, 800, 150)

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(wait_time)

    util.do_close_app_status()