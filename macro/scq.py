import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput import keyboard
from tkinter import *
from pynput.keyboard import Key, Listener, Controller

from common.dungeon import Dungeon

import common.constants as consts
import common.leash as leash
import common.util as util
import common.attack as atk

pynboard = Controller()

class SteamerCrazyQuest(Dungeon):

  def initialize(self, args):
    self.frame_root = args[consts.DATA_FRAME]
    self.btn_start = args[consts.DATA_BUTTON]

    shortcut.add_hotkey(consts.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    util.set_loot_status(False)
    self.run_dungeon(args[consts.DATA_RUNS])

    self.btn_start.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

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
      util.do_key_release()
      util.go_skill_slot(0.2)
      util.do_buffs()

      # GET Quest
      util.open_inventory()
      util.move_click(1230, 340, 0.2)
      quest_book = leash.get_inventory_matrix_defined(run_counter)
      util.click_combo(quest_book[0], quest_book[1], True, 0.5)
      util.move_click(647, 439, 0.2)
      util.do_deselect_pack()

      # FORT RUINA LOC
      try:
        util.open_map()
        map = pyauto.locateOnScreen(consts.IMG_MAP, grayscale=False, confidence=.8, region=util.get_screen_region())
        util.move_click_rel(260, 200, map, 0.2)
        util.move_click_rel(-85, 255, map, 2)
      except pyauto.ImageNotFoundException:
        pass

      util.move_scroll(250, 150, 900, 150, 0.5)

      util.do_dash_rel(647, 109)
      util.do_fade_rel(625, 112)
      util.do_dash_rel(625, 112)
      util.do_fade_rel(625, 112)
      util.do_dash_rel(625, 112)
      util.do_fade_rel(625, 112)
      util.do_dash_rel(625, 112)
      util.do_fade_rel(625, 112)
      util.do_dash_rel(625, 112)
      util.do_fade_rel(561, 148)
      util.do_dash_rel(561, 148)
      util.do_fade_rel(598, 135)
      util.do_dash_rel(603, 133)
      util.do_fade_rel(600, 138)
      util.do_dash_rel(563, 171)
      util.do_fade_rel(563, 171)

      util.do_dash_rel(523, 272)
      util.do_fade_rel(654, 220)
      util.do_dash_rel(608, 225)
      util.do_fade_rel(707, 304)
      util.do_dash_rel(726, 329)

      # Click Dungeon
      util.move_scroll(375, 150, 700, 150)
      self.click_dungeon_portal(599, 256)

      # Enter Dungeon
      self.enter_dungeon(0.3)
      self.challenge_dungeon()

      util.do_final_mode(1)
      util.do_aura(2)
      util.move(625, 200)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_APE, True, sidestep=self.val_sidestep_disabled)
      util.wait(1)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()

      atk.attack_monsters(consts.UNIT_FLOATER, True, sidestep=self.val_sidestep_disabled)
      util.wait(1)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()

      atk.attack_monsters(consts.UNIT_FLOATER, True, sidestep=self.val_sidestep_disabled)
      util.wait(1)

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
      util.wait(1)

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

      util.move(625, 150)
      util.do_dash()
      atk.plunder_box(loot=False)

      util.move(625, 150)
      util.do_fade()
      util.move(625, 150)
      util.do_dash()
      util.move(625, 150)
      util.do_fade()

      atk.attack_monsters(consts.UNIT_STEAKY, True, sidestep=self.val_sidestep_disabled)
      util.wait(1)

      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()
      util.move(625, 200)
      util.do_dash()
      util.move(625, 250)
      util.do_fade()

      atk.focus_gate(consts.UNIT_OBSTACLE)
      util.wait(1)

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
      util.do_fast_plunder(15)
      self.find_kill_final_box(loot=False)

      util.move(625, 250)
      util.do_fade()
      self.click_exit(640, 300, True, 80)

      # Start to End Dungeon
      util.check_notifications()
      self.end_dungeon()
      self.dice_dungeon()
      util.log_action(consts.MSG_END_DG)

      # GOING PORT LUX
      util.wait(3)
      util.open_inventory()
      util.move_click(1230, 340, 0.2)
      return_core = leash.get_inventory_matrix_defined(0)
      util.click_combo(return_core[0], return_core[1], True, 2)

      util.do_dash_rel(108, 344)
      util.do_fade_rel(306, 355)
      util.do_dash_rel(426, 394)

      util.do_fade_rel(402, 309)
      util.do_dash_rel(366, 416)
      util.do_fade_rel(681, 197)
      util.do_dash_rel(677, 260)

      util.do_fade_rel(865, 411)
      util.do_dash_rel(1039, 439)
      util.do_fade_rel(975, 372)
      util.do_dash_rel(1000, 417)
      util.do_fade_rel(1000, 417)
      util.do_dash_rel(944, 361)
      util.do_fade_rel(897, 385, 1.5)
      util.do_fade_rel(696, 386)
      util.do_dash_rel(696, 409)
      util.move_click(697, 382, 2)

      util.move_scroll(600, 150, 600, 350, 0.5)
      util.move_scroll(600, 150, 375, 150, 0.5)

      util.do_dash_rel(538, 229)
      util.do_fade_rel(451, 340)
      util.do_dash_rel(522, 380)
      util.move_click(482, 423, 2)

      util.do_dash_rel(349, 117)
      util.do_fade_rel(407, 152)
      util.do_dash_rel(426, 100)
      util.do_fade_rel(481, 169)
      util.do_dash_rel(512, 141)
      util.do_fade_rel(582, 210)
      util.do_dash_rel(572, 214)
      util.do_fade_rel(673, 216)
      util.do_dash_rel(633, 131)
      util.do_fade_rel(633, 131)
      util.do_dash_rel(633, 134)
      util.do_fade_rel(753, 238)
      util.do_dash_rel(753, 245)
      util.do_fade_rel(655, 357)
      util.move_click(668, 379, 0.5)
      util.move_click(84, 521, 0.5)
      util.move_click(80, 375, 0.5)
      util.move_click(14, 539, 0.5)
      util.move_click(120, 543, 0.5)
      util.do_deselect_pack()

      util.log_time(1)
    util.do_close_app_status()