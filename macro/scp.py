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

class SteamerCrazyPremium(Dungeon):

  def run_dungeon(self, runs):
    run_counter = 0
    while run_counter < runs:
      util.check_run_restart(run_counter)
      run_counter += 1
      self.portal_counter = 0
      util.log_action(consts.MSG_START_DG)
      util.log_run(run_counter)

      # Click Cabal Window
      util.go_cabal_window()
      util.release_keys()
      util.go_skill_slot(0.2)
      util.do_buffs()

      util.move_scroll(375, 150, 700, 150)

      # Click Dungeon
      self.click_dungeon_portal(600, 250)

      # Enter Dungeon
      self.enter_dungeon(0.3)
      self.challenge_dungeon()

      util.do_final_mode(1)
      util.do_aura(2)
      util.move(625, 200)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_APE, True, sidestep=self.val_sidestep_disabled)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()

      atk.attack_monsters(consts.UNIT_FLOATER, True, sidestep=self.val_sidestep_disabled)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()

      util.move(625, 700)
      util.do_fade()

      util.move(625, 700)
      util.do_dash()
      util.move(625, 700)
      util.do_fade()
      util.move(625, 700)
      util.do_dash()
      util.move(625, 700)
      util.do_fade()
      util.move(625, 700)
      util.do_dash()
      util.move(625, 700)
      util.do_fade()
      util.move(625, 700)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_COPTER, True, sidestep=self.val_sidestep_disabled)

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      atk.focus_gate(consts.UNIT_OBSTACLE)

      util.move(625, 150)
      util.do_dash()

      atk.attack_boss(consts.UNIT_PENNA, True, False, False)
      atk.plunder_box()

      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()
      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      atk.attack_monsters(consts.UNIT_STEAKY, True, sidestep=self.val_sidestep_disabled)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()

      atk.focus_gate(consts.UNIT_OBSTACLE)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()

      util.do_battle_mode()
      self.find_kill_low_special_boss(consts.UNIT_STEAMER)
      util.set_battle_mode(False)
      self.find_kill_final_box()

      util.move(625, 250)
      util.do_fade()

      self.click_exit(640, 230)

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)
      util.log_time(1)
    util.do_close_app_status()