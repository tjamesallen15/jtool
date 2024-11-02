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

      # Click Dungeon
      util.move(677, 361)
      util.move(735, 361, 0.5)
      self.click_dungeon_portal(735, 361)

      # Enter Dungeon
      self.enter_dungeon()
      self.challenge_dungeon(1)

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
      self.find_kill_boss(consts.IMG_BLOODY_SWEEPER, consts.UNIT_BLOODY_SWEEPER)

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

      if util.get_attack_type() == consts.IS_MELEE: util.wait(7)
      else: util.wait(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(consts.UNIT_BLOODY_HORN, 4, 6, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      self.focus_monsters(consts.UNIT_BLOODY_HORN, 4, 1, True)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(625, 440)
      util.do_fade()

      util.move_click(1050, 435, 5)

      util.move(660, 450)
      if util.get_attack_type() == consts.IS_MELEE: util.do_fade(3)
      else: util.do_fade()
      util.cancel_aura(1.5)

      # Attack Second Boss (Bloody Fang)
      self.find_kill_boss(consts.IMG_BLOODY_FANG, consts.UNIT_BLOODY_FANG)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      util.move(825, 600)
      util.do_dash()
      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      util.move(720, 500)
      util.do_dash()
      util.do_fade()
      util.do_dash()
      util.do_fade()

      # First Portal
      self.click_portal(650, 400, True)
      util.move_scroll(1000, 150, 375, 150, 0.5)

      util.move(525, 175)
      util.do_dash()
      util.do_fade()
      if util.get_attack_type() == consts.IS_MELEE: util.wait(6)
      else: util.wait(4)

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.focus_monsters(consts.UNIT_KORAIDER, 3, 1, True)

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

      if util.get_attack_type() == consts.IS_MELEE:
        util.move(400, 475)
        util.do_dash()

      self.focus_monsters(consts.UNIT_MUTANT_KORAIDER, 2, 1, True)

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
      if util.get_attack_type() == consts.IS_MELEE:
        util.wait(8)

        util.move(600, 600)
        util.do_fade()
      else: util.wait(3)

      # Attack Third Boss
      util.move_scroll(700, 150, 375, 150, 0.5)
      self.find_kill_boss(consts.IMG_BEELZEBUB, consts.UNIT_BEELZEBUB)
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

      if util.get_party_member_status() == consts.IS_FALSE: atk.plunder_box()
      else: atk.plunder_box_party()

      util.move(100, 325)
      util.do_dash()

      util.move(300, 400)
      util.do_fade()

      if util.get_party_member_status() == consts.IS_FALSE: util.wait(12)
      util.wait(3)

      util.move_scroll(700, 150, 375, 150, 0.5)
      util.move_click(755, 210, 5)
      util.move_click(510, 200, 7)
      util.move_click(800, 300, 3)
      util.move_scroll(375, 150, 700, 150, 0.5)

      util.move_click(775, 130, 4)

      if util.get_party_member_status() == consts.IS_FALSE:
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
      self.attack_monsters(consts.UNIT_ELECTRISHIA, 1, True)

      util.move(450, 550)
      util.do_dash()
      util.do_fade()
      util.do_dash()

      util.do_final_mode()
      util.set_last_cast_mode(3)
      self.attack_monsters(consts.UNIT_ELECTRISHIA, 1, True)

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

      if util.get_party_status() == consts.IS_TRUE: util.wait(5)
      else: util.wait(2)

      util.move(675, 300)
      util.do_fade(5)
      util.do_dash()

      util.move_scroll(700, 150, 375, 150, 0.5)
      # util.move(650, 420)
      # util.do_fade()

      # Attack Fourth Boss (Electula)
      self.find_kill_boss(consts.IMG_ELECTULA, consts.UNIT_ELECTULA)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # util.move(1000, 425)
      util.move(835, 425)
      util.do_dash()
      util.do_fade()
      if util.get_party_member_status() == consts.IS_FALSE:
        util.do_select(0.1)
        atk.plunder_box()
      else:
        atk.plunder_box_party()

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

      if util.get_party_member_status() == consts.IS_TRUE: util.move_click(900, 235, 7)
      else: util.move_click(900, 235, 4)

      # Attack First Ant Hill
      util.move(1050, 340)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      util.move(690, 380)
      util.do_dash()
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Second Ant Hill
      util.move(1050, 470)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Third Ant Hill
      util.move(690, 290)
      util.do_dash()
      util.force_veradrix()
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      # Attack Fourth Ant Hill
      util.move(340, 300)
      util.do_dash()
      util.do_fade()
      util.force_veradrix()
      self.find_focus_monsters(consts.IMG_FULL_ANT_HILL, consts.UNIT_ANT_HILL)

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
      else:
        atk.plunder_box_party()

      util.move(620, 200)
      util.do_dash()
      util.do_fade()

      # Second Portal
      self.click_portal(580, 300, True)
      util.move(660, 275)
      util.do_dash()

      # Attack Final Boss
      self.find_kill_special_boss(consts.UNIT_OMERAI)

      # Check Macro State
      if not util.get_macro_state():
        run_counter += 1000
        continue

      if util.get_party_member_status() == consts.IS_FALSE:
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
      util.log_time()
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
