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
      util.release_keys()
      util.go_skill_slot(0.2)
      util.cancel_buffs()
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

      util.move(1035, 350)
      util.do_dash()

      util.move(985, 390)
      util.do_fade()
      util.do_dash()
      util.do_fade()

      util.move(900, 370)
      util.do_dash()
      util.move(830, 630)
      util.do_fade()
      util.move(825, 560)
      util.do_dash()

       # Attack First Boss (Bloody Sweeper)
      util.set_last_cast_mode(3)
      self.find_kill_boss(consts.IMG_BLOODY_SWEEPER, consts.UNIT_BLOODY_SWEEPER)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(678, 259)
      util.do_dash()
      util.move(847, 294)
      util.do_fade()
      util.move(888, 318)
      util.do_dash()
      util.move(925, 368)
      util.do_fade()
      util.move(1002, 405)
      util.do_dash()
      util.move(1002, 405)
      util.do_fade(2)
      util.move(1002, 405)
      util.do_dash(4)
      util.move(824, 598)
      util.do_fade()
      util.move(614, 592)
      util.do_dash()
      util.move(465, 539)
      util.do_fade()
      util.move(434, 477)
      util.do_dash(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(consts.UNIT_BLOODY_HORN, 6, 6, True)
      util.cancel_aura(2.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Second Boss (Bloody Fang)
      self.find_kill_boss(consts.IMG_BLOODY_FANG, consts.UNIT_BLOODY_FANG)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(990, 320)
      util.do_dash()

      util.move(718, 396)
      util.do_fade()

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(848, 668)
      util.do_dash()

      util.move(721, 554)
      util.do_fade()

      # First Portal
      self.click_portal(656, 386, True)
      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.move(525, 175)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == consts.IS_MELEE: util.wait(6)
      else: util.wait(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(consts.UNIT_KORAIDER, 3, 1, True)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(804, 282)
      util.do_fade()
      util.move(803, 322)
      util.do_dash()
      util.move(1042, 575)
      util.do_fade()
      util.move(1043, 563)
      util.do_dash()
      util.move(1039, 560)
      util.do_fade()
      util.move(970, 550)
      util.do_dash(3)
      util.move(1084, 282)
      util.do_dash(2)
      util.move(938, 313)
      util.do_fade(3)
      util.move(935, 315)
      util.do_dash(2)

      self.focus_monsters(consts.UNIT_MUTANT_KORAIDER, 2, 1, True)
      util.cancel_aura(2.0)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Beelzebub Boss
      util.move(560, 352)
      util.do_fade()
      util.move(773, 244)
      util.do_dash()
      util.move(717, 261)
      util.do_fade()
      util.move(726, 226)
      util.do_dash()
      util.move(703, 264)
      util.do_fade()
      util.move(754, 267)
      util.do_dash()
      util.move(792, 285)
      util.do_fade()
      util.move(688, 150)
      util.do_dash()
      util.move(626, 168)
      util.do_fade()
      util.move(617, 188)
      util.do_dash()
      util.move(615, 296)
      util.do_fade(10)

      # Attack Third Boss
      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(consts.IMG_BEELZEBUB, consts.UNIT_BEELZEBUB)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(774, 344)
      util.do_dash()

      if util.get_party_member_status() == consts.IS_FALSE:
        atk.plunder_box()
        util.wait(4)
      else:
        atk.plunder_box_party()
        util.wait(8)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Electrishia Base
      util.move(710, 178)
      util.do_dash()
      util.move(710, 233)
      util.do_fade()
      util.move(706, 248)
      util.do_dash()
      util.move(668, 291)
      util.do_fade()
      util.move(520, 287)
      util.do_dash()
      util.move(518, 320)
      util.do_fade()
      util.move(597, 279)
      util.do_dash()
      util.move(744, 308)
      util.do_fade()
      util.move(763, 322)
      util.do_dash()
      util.move(936, 409)
      util.do_fade()
      util.move(920, 439)
      util.do_dash()
      util.move(846, 474)
      util.do_fade(1.5)
      util.move(664, 478)
      util.do_fade()
      util.move(931, 541)
      util.do_dash()
      util.move(740, 492)
      util.do_fade()

      util.move_scroll(375, 150, 700, 150, 0.5)
      if util.get_party_member_status() == consts.IS_FALSE:
        util.move(910, 200)
        util.do_dash(2)
        util.do_fade(4)

        util.do_dash(2)
        util.do_fade(3)

        util.move(450, 550)
        util.do_dash()
      else:
        util.move(910, 200)
        util.do_dash()
        util.do_fade()

        util.do_dash()
        util.do_fade()

        util.move(450, 550)
        util.do_dash()

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, 1, True)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(450, 550)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.do_final_mode(1)
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, 1, True)

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
      else: util.wait(8)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_status() == consts.IS_TRUE: util.wait(5)
      else: util.wait(2)

      util.move(675, 300)
      util.do_fade(5)
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(consts.IMG_ELECTULA, consts.UNIT_ELECTULA)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(835, 425)
      util.do_dash()
      util.do_fade()
      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_select(0.1)
        atk.plunder_box()
      else: atk.plunder_box_party()

      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Move to Ant Base
      util.wait(10)
      util.move_scroll(375, 150, 700, 150, 0.5)
      util.move(549, 180)
      util.do_dash()
      util.move(539, 262)
      util.do_fade()

      util.move(573, 286)
      util.do_dash()
      util.move(675, 255)
      util.do_fade()

      util.move(629, 293)
      util.do_dash()
      util.move(842, 338)
      util.do_fade()
      util.move(842, 338)
      util.do_dash()
      util.move(863, 377)
      util.do_fade()
      util.move(759, 389)
      util.do_dash()

      util.do_final_mode(2)
      util.do_final_mode(2)
      util.do_aura(2)
      util.set_last_cast_mode(3)

      util.move(910, 466)
      util.do_dash()
      util.move(876, 537)
      util.do_fade()
      util.move(799, 581)
      util.do_dash()
      util.move(686, 586)
      util.do_fade()
      util.move(704, 571)
      util.do_dash()

      util.move_scroll(375, 150, 700, 150, 0.5)

      util.move(849, 349)
      util.do_dash()
      util.force_veradrix()
      util.move(611, 384)
      util.do_fade()
      # Attack First Ant Hill
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(971, 510)
      util.do_dash()
      util.force_veradrix()
      util.move(666, 439)
      util.do_fade()
      # Attack Second Ant Hill
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(759, 276)
      util.do_dash()
      util.force_veradrix()
      util.move(660, 399)
      util.do_fade()
      # Attack Third Ant Hill
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(323, 310)
      util.do_dash()
      util.force_veradrix()
      util.move(504, 355)
      util.do_fade()
      # Attack Fourth Ant Hill
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(832, 361)
      util.do_dash()
      util.force_veradrix()

      if util.get_attack_type() == consts.IS_MELEE:
        util.move(607, 259)
        util.do_fade(1.5)
        util.move(614, 283)
        util.do_fade()
      else:
        util.move(607, 259)
        util.do_fade()

      util.cancel_aura(2.0)
      # Attack Fifth Boss (Queen Ripley)
      self.find_kill_boss(consts.IMG_QUEEN_RIPLEY, consts.UNIT_QUEEN_RIPLEY)

      util.move(643, 528)
      util.do_fade()

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

      util.move(592, 170)
      util.do_dash()
      util.move(599, 217)
      util.do_fade()
      util.move(604, 230)
      util.do_dash()
      util.move(604, 232)
      util.do_fade()

      # Second Portal
      self.click_portal(627, 316, True, 0.5)
      util.move(626, 291)
      util.do_dash()
      util.move(626, 291)
      util.do_dash()
      util.move(626, 291)
      util.do_fade()

       # Attack Final Boss
      self.find_kill_special_boss(consts.UNIT_OMERAI)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_plunder(3)
        util.wait(4)
      else:
        util.wait(4)

      util.move(512, 633)
      util.do_dash()

      util.move(486, 617)
      util.do_fade()

      util.move(560, 607)
      util.do_dash()

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
