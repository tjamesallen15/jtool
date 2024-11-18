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

class PurifierOfTheForest(Dungeon, Special):

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

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Click Dungeon
      util.move(677, 361)
      util.move(735, 361, 0.5)
      self.click_dungeon_portal(735, 361)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon(1)

      util.do_dash_rel(1035, 350)

      util.do_fade_rel(985, 390)
      util.do_dash_rel(985, 390)
      util.do_fade_rel(985, 390)

      util.do_dash_rel(900, 370)
      util.do_fade_rel(830, 630)
      util.do_dash_rel(825, 560)

       # Attack First Boss (Bloody Sweeper)
      util.set_last_cast_mode(3)
      self.find_kill_boss(consts.IMG_BLOODY_SWEEPER, consts.UNIT_BLOODY_SWEEPER)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(678, 259)
      util.do_fade_rel(847, 294)
      util.do_dash_rel(888, 318)
      util.do_fade_rel(925, 368)
      util.do_dash_rel(1002, 405)
      util.do_fade_rel(1002, 405, 2)
      util.do_dash_rel(1002, 405, 4)
      util.do_fade_rel(824, 598)
      util.do_dash_rel(614, 592)
      util.do_fade_rel(465, 539)
      util.do_dash_rel(434, 477, 4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      if util.get_party_status() == consts.IS_TRUE: self.focus_monsters(consts.UNIT_BLOODY_HORN, 12, 6, True)
      else: self.focus_monsters(consts.UNIT_BLOODY_HORN, 8, 6, True)
      util.cancel_aura(2.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Second Boss (Bloody Fang)
      self.find_kill_boss(consts.IMG_BLOODY_FANG, consts.UNIT_BLOODY_FANG)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(990, 320)
      util.do_fade_rel(718, 396)

      util.wait(2)
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(848, 668)
      util.do_fade_rel(721, 554)

      # First Portal
      self.click_portal(656, 386, True)
      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.do_dash_rel(525, 175)
      util.do_fade_rel(525, 175)
      if util.get_attack_type() == consts.IS_MELEE: util.wait(6)
      else: util.wait(4)

      util.do_fade_rel(657, 482)

      util.do_final_mode()
      util.set_last_cast_mode(3)

      if util.get_party_status() == consts.IS_TRUE: self.focus_monsters(consts.UNIT_KORAIDER, 6, 1, True)
      else: self.focus_monsters(consts.UNIT_KORAIDER, 3, 1, True)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(610, 306)
      util.do_fade_rel(804, 282)
      util.do_dash_rel(803, 322)
      util.do_fade_rel(1042, 575)
      util.do_dash_rel(1043, 563)
      util.do_fade_rel(1039, 560, 4)

      if util.get_char_class() == consts.VAL_CLASS_FA:
        self.focus_monsters(consts.UNIT_MUTANT_KORAIDER, 2, 1, True)

      util.do_dash_rel(970, 550, 3)
      util.do_dash_rel(1084, 282, 4)
      util.do_fade_rel(938, 313, 3)
      util.do_dash_rel(935, 315, 2)

      if util.get_party_status() == consts.IS_TRUE: self.focus_monsters(consts.UNIT_MUTANT_KORAIDER, 4, 1, True)
      else: self.focus_monsters(consts.UNIT_MUTANT_KORAIDER, 2, 1, True)
      util.do_dash_rel(935, 315, 2)
      util.cancel_aura(2.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Beelzebub Boss
      util.do_fade_rel(560, 352)
      util.do_dash_rel(773, 244)
      util.do_fade_rel(717, 261)
      util.do_dash_rel(726, 226)
      util.do_fade_rel(703, 264)
      util.do_dash_rel(754, 267)
      util.do_fade_rel(792, 285)
      util.do_dash_rel(688, 150)
      util.do_fade_rel(626, 168)
      util.do_dash_rel(617, 188)
      util.do_fade_rel(615, 296, 10)

      # Attack Third Boss
      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(consts.IMG_BEELZEBUB, consts.UNIT_BEELZEBUB)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(774, 344)

      if util.get_party_member_status() == consts.IS_FALSE:
        atk.plunder_box()
        util.wait(4)
      else:
        atk.plunder_box_party()
        util.wait(12)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Electrishia Base
      util.do_dash_rel(710, 178)
      util.do_fade_rel(710, 233)
      util.do_dash_rel(706, 248)
      util.do_fade_rel(668, 291)
      util.do_dash_rel(520, 287)
      util.do_fade_rel(518, 320)
      util.do_dash_rel(597, 279)
      util.do_fade_rel(744, 308)
      util.do_dash_rel(763, 322)
      util.do_fade_rel(936, 409)
      util.do_dash_rel(920, 439)
      util.do_fade_rel(846, 474, 1.5)
      util.do_fade_rel(664, 478)
      util.do_dash_rel(931, 541)
      util.do_fade_rel(740, 492)

      util.move_scroll(375, 150, 700, 150, 0.5)
      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_dash_rel(910, 200, 3)
        util.do_fade_rel(910, 200, 4)

        util.do_dash_rel(910, 200, 2)
        util.do_fade_rel(910, 200, 3)

        util.do_dash_rel(450, 550, 3)
      else:
        util.do_dash_rel(910, 200)
        util.do_fade_rel(910, 200)

        util.do_dash_rel(910, 200)
        util.do_fade_rel(910, 200)

        util.do_dash_rel(450, 550)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, True, delay=1.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(450, 550)
      util.do_fade_rel(450, 550)
      util.do_dash_rel(450, 550)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, True, delay=1.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Web Gate
      util.do_dash_rel(910, 200)
      util.do_fade_rel(910, 200)
      util.do_dash_rel(910, 200)

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, True, delay=1.0)

      util.do_fade_rel(910, 200)
      util.do_dash_rel(910, 200)
      util.do_fade_rel(910, 200)
      util.do_dash_rel(910, 200)
      util.do_fade_rel(910, 200)
      util.cancel_aura(2.0)

      util.move_scroll(375, 150, 700, 150, 0.5)
      self.go_web_gate()

      check_gate = True
      while check_gate:
        if not util.get_macro_state():
          util.log_action(consts.MSG_TERMINATE)
          check_gate = False

        if check_gate == False:
          break

        try:
          util.do_select(0.1)
          gate = pyauto.locateOnScreen(consts.IMG_WEB_GATE, grayscale=False, confidence=.7, region=util.get_archer_region())
          check_gate = False
          break
        except pyauto.ImageNotFoundException:
          util.do_deselect_pack()
          self.go_web_gate()

      # Attack Web Gate
      if util.get_party_leader_status() == consts.IS_TRUE: util.wait(2)
      if util.get_party_member_status() == consts.IS_FALSE: atk.focus_gate(consts.UNIT_WEB_GATE, 0)
      else:
        web_gate = True
        while web_gate:
          if not util.get_macro_state():
            util.log_action(consts.MSG_TERMINATE)
            web_gate = False

          if web_gate == False:
            break

          try:
            gate = pyauto.locateOnScreen(consts.IMG_WEB_GATE, grayscale=False, confidence=.7, region=util.get_archer_region())
          except pyauto.ImageNotFoundException:
            util.wait(6)
            web_gate = False
            break

      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE: util.do_fade_rel(675, 300, 7)
      else: util.do_fade_rel(675, 300, 2)

      util.do_dash_rel(675, 300)
      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(consts.IMG_ELECTULA, consts.UNIT_ELECTULA)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(835, 425)
      util.do_fade_rel(835, 425)
      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_select(0.1)
        atk.plunder_box()
      else: atk.plunder_box_party()

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Ant Base
      util.countdown_timer(10)
      util.move_scroll(375, 150, 700, 150, 0.5)
      util.do_dash_rel(549, 180)
      util.do_fade_rel(539, 262)

      util.do_dash_rel(573, 286)
      util.do_fade_rel(675, 255)

      util.do_dash_rel(629, 293)
      util.do_fade_rel(842, 338)
      util.do_dash_rel(842, 338)
      util.do_fade_rel(863, 377)
      util.do_dash_rel(759, 389, 1.5)

      util.set_last_cast_mode(3)

      util.do_dash_rel(910, 466)
      util.do_fade_rel(876, 537)
      util.do_dash_rel(799, 581)
      util.do_fade_rel(686, 586)
      util.do_dash_rel(704, 571)

      util.move_scroll(375, 150, 700, 150, 0.5)

      util.do_dash_rel(849, 349, veradrix=True)
      util.do_fade_rel(611, 384)
      # Attack First Ant Hill
      self.find_focus_rel_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(971, 510, veradrix=True)
      util.do_fade_rel(666, 439)
      # Attack Second Ant Hill
      self.find_focus_rel_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(759, 276, veradrix=True)
      util.do_fade_rel(660, 399)
      # Attack Third Ant Hill
      self.find_focus_rel_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(323, 310, veradrix=True)
      util.do_fade_rel(504, 355)
      # Attack Fourth Ant Hill
      self.find_focus_rel_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(832, 361, veradrix=True)

      if util.get_attack_type() == consts.IS_MELEE:
        util.do_fade_rel(607, 259, 1.5)
        util.do_fade_rel(614, 283)
      else: util.do_fade_rel(607, 259)

      util.cancel_aura(1)
      # Attack Fifth Boss (Queen Ripley)
      self.find_kill_boss(consts.IMG_QUEEN_RIPLEY, consts.UNIT_QUEEN_RIPLEY)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
        finding = True
        while finding:
          if not util.get_macro_state():
            util.log_action(consts.MSG_TERMINATE)
            finding = False

          if finding == False:
            break

          try:
            util.force_veradrix()
            util.do_select(0.1)
            box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
            atk.plunder_box(False)
            finding = False
            break
          except pyauto.ImageNotFoundException:
            pass
      else: atk.plunder_box_party()

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.do_dash_rel(592, 170, veradrix=True)
      util.do_fade_rel(599, 217, veradrix=True)
      util.do_dash_rel(604, 230, veradrix=True)
      util.do_fade_rel(604, 232, veradrix=True)

      # Second Portal
      self.click_portal(627, 316, True)
      util.move_click(632, 387)
      util.do_deselect()

      if util.get_party_member_status() == consts.IS_TRUE:
        util.do_fade_rel(666, 291)
        util.do_dash_rel(666, 291)
      else:
        util.do_fade_rel(626, 291)
        util.do_dash_rel(626, 291)

       # Attack Final Boss
      self.find_kill_special_boss(consts.UNIT_OMERAI)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_plunder(3)
        util.wait(4)

        util.do_dash_rel(512, 633)
        util.do_fade_rel(486, 617)
        util.do_dash_rel(560, 607)
      else:
        util.do_fast_plunder()
        util.wait(8)

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_final_box()
      else: atk.plunder_box_party()

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

  def go_web_gate(self):
    util.do_fade_rel(735, 200, veradrix=True)
    util.do_dash_rel(735, 200)
    util.do_fade_rel(735, 200, veradrix=True)
    util.do_dash_rel(735, 200)
    util.do_fade_rel(735, 200, veradrix=True)

    util.do_dash_rel(820, 200)
    util.do_fade_rel(820, 200, veradrix=True)
    util.do_dash_rel(820, 200)
    util.do_fade_rel(820, 200, veradrix=True)

    util.do_dash_rel(250, 200)
    util.do_fade_rel(250, 200, veradrix=True)

    util.do_dash_rel(350, 300)
    util.do_fade_rel(350, 300, veradrix=True)

    util.do_dash_rel(415, 275)
    util.do_fade_rel(435, 275, veradrix=True)

    util.do_dash_rel(550, 275)

    util.do_fade_rel(475, 300, veradrix=True)
    util.do_dash_rel(475, 300)
