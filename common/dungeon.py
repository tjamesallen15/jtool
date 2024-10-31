import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from abc import ABC, abstractmethod

import common.constants as consts
import common.util as util
import common.attack as atk

class Dungeon(ABC):
  # GLOBAL VARIABLES
  frame_root = []
  btn_start = []

  # UNIQUE VARIABLES
  val_sidestep_enabled = True
  val_sidestep_disabled = False

  def initialize(self, args):
    self.frame_root = args[consts.DATA_FRAME]
    self.btn_start = args[consts.DATA_BUTTON]

    shortcut.add_hotkey(consts.HOTKEY_TERMINATE, util.terminate)
    self.btn_start.config(state=consts.STATE_DISABLED)
    self.frame_root.update()

    self.run_dungeon(args[consts.DATA_RUNS])

    self.btn_start.config(state=consts.STATE_NORMAL)
    self.frame_root.update()

  @abstractmethod
  def run_dungeon(self, runs):
    pass

  def click_dungeon_portal(self, x, y):
    portal_found = False

    util.move_click(x, y)
    try:
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BLOCKER_FOUND)
      atk.focus_monsters(consts.UNIT_BLOCKER, False, False, False)
      util.wait(1)
      util.move_click(x, y, 1)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BLOCKER_NOT_FOUND)

    try:
      enterdg = pyauto.locateOnScreen(consts.IMG_ENTER_DG, grayscale=False, confidence=.9)
      portal_found = True
      util.log_action(consts.MSG_BUTTON_FOUND)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BUTTON_NOT_FOUND)

    if portal_found == False:
      util.move_click(x, y)
      try:
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BLOCKER_FOUND)
        atk.focus_monsters(consts.UNIT_BLOCKER, False, False, False)
        util.wait(1)
        util.move_click(x, y, 1)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BLOCKER_NOT_FOUND)

      try:
        enterdg = pyauto.locateOnScreen(consts.IMG_ENTER_DG, grayscale=False, confidence=.9)
        portal_found = True
        util.log_action(consts.MSG_BUTTON_FOUND)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BUTTON_NOT_FOUND)

    if portal_found == False:
      util.move_click(x, y)
      try:
        mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
        util.log_action(consts.MSG_BLOCKER_FOUND)
        atk.focus_monsters(consts.UNIT_BLOCKER, False, False, False)
        util.wait(1)
        util.move_click(x, y, 1)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BLOCKER_NOT_FOUND)

      try:
        enterdg = pyauto.locateOnScreen(consts.IMG_ENTER_DG, grayscale=False, confidence=.9)
        portal_found = True
        util.log_action(consts.MSG_BUTTON_FOUND)
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BUTTON_NOT_FOUND)

  def enter_dungeon(self, delay=1):
    entering = True
    while entering:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        entering = False

      if entering == False:
        break

      try:
        enterdg = pyauto.locateOnScreen(consts.IMG_ENTER_DG, grayscale=False, confidence=.9)
        util.log_action(consts.MSG_BUTTON_FOUND)
        util.move_click_rel(15, 15, enterdg, 1)
        entering = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_BUTTON_NOT_FOUND)

    util.wait(delay)

  def challenge_dungeon(self, delay=0):
    challenging = True
    while challenging:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        challenging = False

      if challenging == False:
        break

      if util.get_party_member_status() == consts.IS_FALSE:
        try:
          challengedg = pyauto.locateOnScreen(consts.IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
          util.log_action(consts.MSG_BUTTON_FOUND)
          util.move_click_rel(15, 15, challengedg, 0.2)
          challenging = False
          break
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BUTTON_NOT_FOUND)
      else:
        try:
          challengedg = pyauto.locateOnScreen(consts.IMG_CHALLENGE_DG, grayscale=False, confidence=.9)
          util.log_action(consts.MSG_BUTTON_FOUND)
        except pyauto.ImageNotFoundException:
          util.log_action(consts.MSG_BUTTON_NOT_FOUND)
          challenging = False
          break

    if delay != 0: util.wait(delay)

  def end_dungeon(self):
    ending = True
    end_check_track = 0
    while ending:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        ending = False

      if ending == False:
        break

      end_check_track += 1
      if (end_check_track >= 100):
        ending = False
        break

      try:
        ending_dungeon = pyauto.locateOnScreen(consts.IMG_END_DG, grayscale=False, confidence=.9, region=util.get_middle_region())
        util.move_click_rel(50, 15, ending_dungeon, 0.2)
        ending = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_CHECK_END_DG)

  def dice_dungeon(self):
    dicing = True
    while dicing:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        dicing = False

      if dicing == False:
          break

      try:
        dice_roll = pyauto.locateOnScreen(consts.IMG_DICE_ROLL, grayscale=False, confidence=.9, region=util.get_middle_region())
        util.move_click_rel(50, 15, dice_roll, 0.2)
        dicing = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_DICE_ROLL)

    confirming = True
    while confirming:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        confirming = False

      if confirming == False:
          break

      try:
        dice_confirm = pyauto.locateOnScreen(consts.IMG_DICE_OKAY, grayscale=False, confidence=.9, region=util.get_middle_region())
        util.move_click_rel(10, 5, dice_confirm, 0.2)
        confirming = False
        break
      except pyauto.ImageNotFoundException:
        util.log_action(consts.MSG_DICE_ROLL_OKAY)

  def click_portal(self, x, y, deviate=False, delay=0.5):
    check_portal = True
    while check_portal:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        check_portal = False

      if check_portal == False:
        break

      try:
        util.move_click(x, y, 0.2)
        if deviate == consts.IS_TRUE:
          util.move_click(x - 10, y, 0.2)
          util.move_click(x + 10, y, 0.2)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        check_portal = False
      except pyauto.ImageNotFoundException:
        pass

    util.wait(delay)

  def click_dialog(self, x, y, deviate=False):
    check_dialog = True
    while check_dialog:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        check_dialog = False

      if check_dialog == False:
        break

      try:
        util.move_click(x, y, 0.2)
        if deviate == consts.IS_TRUE:
          util.move_click(x - 10, y, 0.2)
          util.move_click(x + 10, y, 0.2)
        dialog = pyauto.locateOnScreen(consts.IMG_CHECK_DIALOG, grayscale=False, confidence=.9, region=util.get_dialog_region())
        util.log_action(consts.MSG_CHECK_DIALOG_FOUND)
        util.move_click_rel(10, 10, dialog, 0.5)
        check_dialog = False
      except pyauto.ImageNotFoundException:
        pass

class Special(ABC):
  def find_kill_boss(self, unit_image, unit_name, cancel=True, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(unit_image, grayscale=False, confidence=.7, region=util.get_archer_region())
        atk.focus_high_boss(unit_name, False, True, False)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    if cancel == consts.IS_TRUE: util.cancel_aura(1.2)
    util.wait(delay)

  def find_kill_special_boss(self, unit_name, cancel=True, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_archer_region())
        atk.focus_high_boss(unit_name, False, True, True)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    if cancel == consts.IS_TRUE: util.cancel_aura(1.2)
    util.wait(delay)

  def find_kill_mobs(self, unit_image, unit_name, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        mobs = pyauto.locateOnScreen(unit_image, grayscale=False, confidence=.7, region=util.get_archer_region())
        atk.focus_high_monsters(unit_name, False)
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    util.wait(delay)

  def find_kill_box(self, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass


    atk.plunder_box(False)
    util.wait(delay)

  def find_kill_final_box(self, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass


    atk.plunder_final_box(False)
    util.wait(delay)

  def find_kill_box_party(self, delay=0.5):
    finding = True
    while finding:
      if not util.get_macro_state():
        util.log_action(consts.MSG_TERMINATE)
        finding = False

      if finding == False:
        break

      try:
        util.do_select(0.1)
        box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
        finding = False
        break
      except pyauto.ImageNotFoundException:
        pass

    atk.plunder_box_party(False)
    util.wait(delay)

  def attack_monsters(self, unit_name, delay=1, aura=False):
    atk.attack_monsters(unit_name, aura, 0.3, False)
    util.wait(delay)

  def focus_monsters(self, unit_name, reps=4, delay=1, aura=False):
    for x in range(reps):
      atk.focus_monsters(unit_name, True, aura, False)

    util.wait(delay)
