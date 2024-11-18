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
      util.do_key_release()
      util.go_skill_slot(0.2)
      util.do_buffs()

      # Click Dungeon
      util.do_dash_rel(628, 482)
      self.click_dungeon_portal(600, 351)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon()

      util.move_scroll(700, 150, 375, 150)
      util.do_dash_rel(616, 268)
      util.do_fade_rel(608, 307)
      util.do_dash_rel(606, 314)
      self.click_portal(606, 328)

      util.do_fade_rel(577, 301)

      # First Boss
      util.set_last_cast_mode(3)
      self.find_kill_semi_boss(consts.UNIT_FLA_3571)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(670, 607)
      util.move_scroll(375, 150, 1000, 150)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(644, 161)
      util.do_fade_rel(629, 225)
      util.do_dash_rel(620, 243)
      util.do_fade_rel(495, 276)
      util.do_dash_rel(500, 291)
      util.do_fade_rel(845, 209)
      util.do_dash_rel(820, 205)
      util.do_fade_rel(584, 243)

      # Attack Monad Group
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      if util.get_party_status() == consts.IS_TRUE: self.find_focus_until_boss(consts.UNIT_MONAD_FRAGMENT, True, consts.TYPE_SEMI)
      else:
        atk.attack_monsters(consts.UNIT_MONAD_FRAGMENT, sidestep=self.val_sidestep_disabled, type=consts.TYPE_SEMI)
        util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(655, 505)
      util.do_fade_rel(547, 640)
      util.do_dash_rel(547, 640)
      util.do_fade_rel(412, 524)
      util.do_dash_rel(412, 524)
      util.do_fade_rel(586, 474)
      util.do_dash_rel(783, 537)
      util.do_fade_rel(577, 594)
      util.do_dash_rel(637, 607)
      util.do_fade_rel(636, 607)
      util.do_dash_rel(577, 601)

      util.countdown_timer(30)

      util.do_dash_rel(644, 161)
      util.do_fade_rel(629, 225)
      util.do_dash_rel(620, 243)
      util.do_fade_rel(495, 276)
      util.do_dash_rel(500, 291)
      util.do_fade_rel(845, 209)
      util.do_dash_rel(820, 205)
      util.do_fade_rel(584, 243)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      if util.get_party_status() == consts.IS_TRUE: self.find_focus_until_boss(consts.UNIT_MONAD_FRAGMENT, True, consts.TYPE_SEMI)
      else:
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

      util.do_dash_rel(661, 311)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_fade_rel(684, 233)
      util.do_dash_rel(684, 241)
      util.do_fade_rel(652, 261)
      self.click_portal(652, 294)

      util.do_dash_rel(631, 596)
      util.move_scroll(375, 150, 1100, 150)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      if util.get_party_status() == consts.IS_TRUE: self.find_focus_until_boss(consts.UNIT_SEEKER, True, consts.TYPE_SEMI)
      else:
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

      util.do_fade_rel(707, 393)
      util.do_dash_rel(648, 121)
      util.do_fade_rel(616, 169)
      util.do_dash_rel(626, 197)
      util.do_fade_rel(617, 277)
      util.do_dash_rel(615, 226)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_SERVANT, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_fade_rel(625, 614, 2, True)
      util.do_dash_rel(656, 560, 4, True)
      util.do_fade_rel(584, 364, 3, True)

      atk.attack_monsters(consts.UNIT_SERVANT, sidestep=self.val_sidestep_disabled, type=consts.TYPE_SEMI)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(637, 170, veradrix=True)
      util.do_fade_rel(624, 218, 2, veradrix=True)
      util.do_fade_rel(637, 617, 2, veradrix=True)
      util.do_dash_rel(647, 638, 2, veradrix=True)
      util.do_fade_rel(695, 547, 2, veradrix=True)
      util.do_dash_rel(632, 579, 4, veradrix=True)
      util.do_fade_rel(637, 268, veradrix=True)
      util.do_dash_rel(646, 522, veradrix=True)

      self.find_kill_semi_boss(consts.UNIT_VITO)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_fade_rel(604, 308)
      util.do_dash_rel(610, 228)
      util.do_fade_rel(640, 249)
      util.do_dash_rel(636, 333)

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(581, 232)
      util.do_fade_rel(577, 263)
      self.click_portal(606, 295)
      util.move_scroll(500, 150, 375, 150, 5)

      util.do_dash_rel(159, 245)
      util.do_fade_rel(255, 260)
      util.do_dash_rel(296, 270)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(910, 706)
      util.do_fade_rel(643, 590)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(654, 625)
      util.do_fade_rel(728, 611)
      util.do_dash_rel(665, 590)
      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      atk.focus_monsters(consts.UNIT_PLUMA, sidestep=self.val_sidestep_disabled)
      util.cancel_aura(2.0)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(575, 546, 5)
      util.do_fade_rel(586, 304)

      self.find_kill_special_boss(consts.UNIT_PERIUS)
      if util.get_party_member_status() == consts.IS_FALSE: util.do_fast_plunder(10)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(604, 151)
      util.do_fade_rel(626, 244)
      util.do_dash_rel(618, 237)

      if util.get_party_member_status() == consts.IS_FALSE:
        util.move_scroll(375, 150, 800, 150)
        atk.plunder_final_box()
      else:
        util.move_scroll(375, 150, 800, 150)
        atk.plunder_box_party()

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