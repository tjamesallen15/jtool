import time
import math

import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from tkinter import *
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import common.constants as consts
import common.util as util

def attack_monsters(unit=consts.UNIT_EMPTY, aura=True, interval=consts.VAL_INTERVAL_DEFAULT, sidestep=True, type=consts.TYPE_BOSS):
  combo = True
  fade_count = 0

  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    if sidestep == consts.IS_TRUE:
      if (fade_count == 20):
        fade_count = 0
        util.move_click(700, 440, 0.2)
        util.do_fade(0.1)
      else:
        fade_count += 1

    util.do_select(0.1)
    try:
      if type == consts.TYPE_BOSS: pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      elif type == consts.TYPE_SEMI: pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      elif type == consts.TYPE_SHADE: pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.do_deselect_pack()
      util.log_action(consts.MSG_BOSS_FOUND)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_ATTACK + unit)

    if combo == False:
      break

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)
      util.do_attack(interval)
      util.do_attack(interval, True)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTERS_CLEARED)
      combo = False
      break

def attack_shade_monsters(unit=consts.UNIT_EMPTY, aura=True, interval=consts.VAL_INTERVAL_DEFAULT, sidestep=True, type=consts.TYPE_BOSS):
  combo = True
  fade_count = 0

  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    if sidestep == consts.IS_TRUE:
      if (fade_count == 20):
        fade_count = 0
        util.move_click(700, 440, 0.2)
        util.do_fade(0.1)
      else:
        fade_count += 1

    util.do_select(0.1)
    try:
      if type == consts.TYPE_BOSS: pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      elif type == consts.TYPE_SEMI: pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.do_deselect_pack()
      util.log_action(consts.MSG_BOSS_FOUND)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_ATTACK + unit)

    if combo == False:
      break

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)
      util.do_attack(interval)
      util.do_attack(interval, True)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTERS_CLEARED)
      combo = False
      break

def attack_boss(unit=consts.UNIT_EMPTY, select=True, aura=True, strict=False, cont=True):
  combo = True

  if util.get_battle_mode_status() and util.get_char_class() == consts.VAL_CLASS_FA and select == consts.IS_TRUE:
    util.do_select(0.1)
    util.do_select(0.1)
  elif select == consts.IS_TRUE:
    util.do_select(0.1)

  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    try:
      boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      if unit == consts.UNIT_EMPTY: util.log_action(consts.MSG_ATTACK_BOSS)
      else: util.log_action(consts.MSG_ATTACK + unit)

      util.do_attack(0.1, strict, cont)
      util.do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BOSS_KILLED)
      combo = False
      break

def attack_semi_boss(select=True, aura=True, strict=False, cont=True):
  combo = True

  if select == consts.IS_TRUE: util.do_select(0.1)

  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False
      break

    if combo == False:
      break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    try:
      boss = pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK_BOSS)
      util.do_attack(0.1, strict, cont)
      util.do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BOSS_KILLED)
      combo = False
      break

def attack_backtrack(unit=consts.UNIT_EMPTY, aura=True, select=True, sidestep=True):
  combo = True
  fade_count = 0

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    if sidestep == consts.IS_TRUE:
      if (fade_count == 20):
        fade_count = 0
        util.move_click(700, 440, 0.2)
        util.do_fade(0.1)
      else:
        fade_count += 1

    try:
      if select == consts.IS_TRUE: util.do_select(0.1)
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)

      util.do_attack(0.1)
      util.do_attack(0.1)

      if select == consts.IS_TRUE:
        util.do_deselect_pack()
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

    try:
      if select == consts.IS_TRUE: util.do_select(0.1)
      box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BOX_FOUND)
      plunder_box(select, 3)
      if select == consts.IS_TRUE: util.do_deselect_pack()
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BOX_NOT_FOUND)
      combo = False
      break

def focus_monsters(unit=consts.UNIT_EMPTY, select=True, aura=True, sidestep=True):
  combo = True
  fade_count = 0

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    if sidestep == consts.IS_TRUE:
      if (fade_count == 20):
        fade_count = 0
        util.move_click(700, 440, 0.2)
        util.do_fade(0.1)
      else:
        fade_count += 1

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)

      util.do_attack(0.1)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTER_CLEARED)
      combo = False

def focus_shade_monsters(unit=consts.UNIT_EMPTY, select=True, aura=True, sidestep=True):
  combo = True
  fade_count = 0

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    if sidestep == consts.IS_TRUE:
      if (fade_count == 20):
        fade_count = 0
        util.move_click(700, 440, 0.2)
        util.do_fade(0.1)
      else:
        fade_count += 1

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)

      util.do_attack(0.1)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTER_CLEARED)
      combo = False

def focus_gate(unit=consts.UNIT_EMPTY, select=True):
  combo = True

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    try:
      gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)
      util.do_attack(0.3)
      util.do_attack(0.3)
    except pyauto.ImageNotFoundException:
      combo = False
      util.log_action(consts.MSG_GATE_CLEARED)
      break

def focus_gate_party(unit=consts.UNIT_EMPTY, select=True):
  checking = True

  if select == consts.IS_TRUE: util.do_select(0.1)
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_GATE_FOUND + unit)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_GATE_CLEARED)
      break

  util.wait(1.5)

def focus_monster_boss(unit=consts.UNIT_EMPTY, select=True, aura=True, strict=False, cont=True):
  combo = True

  if select == consts.IS_TRUE: util.do_select(0.1)

  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    if aura == consts.IS_TRUE:
      util.do_final_mode()
      util.do_aura()

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_ATTACK + unit)

      util.do_attack(0.1, strict, cont)
      util.do_attack(0.1, strict, cont)
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTER_CLEARED)
      combo = False
      break

def focus_high_monsters(unit=consts.UNIT_EMPTY, select=True):
  combo = True

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
        break

    try:
      mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_archer_region())
      util.log_action(consts.MSG_ATTACK + unit)
      util.do_special_attack()
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_MONSTER_CLEARED)
      combo = False

def focus_high_boss(unit=consts.UNIT_EMPTY, select=True, aura=True, type=consts.TYPE_BOSS):
  combo = True
  cast_mode = True
  mode_time = time.time()
  mode = 2

  if util.get_last_cast_mode() == consts.STATE_TWO: mode = 3
  elif util.get_last_cast_mode() == consts.STATE_THREE: mode = 2
  else: mode = 2

  if select == consts.IS_TRUE: util.do_select(0.1)
  while combo:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      combo = False

    if combo == False:
      break

    check_time = time.time()
    sec_difference = math.ceil(check_time - mode_time)

    if sec_difference >= 30 and sec_difference <= 35 and aura == consts.IS_TRUE:
      util.do_aura()
      util.do_aura()
      util.do_aura()
      util.force_veradrix()
      util.do_short_buffs()

    if sec_difference % 30 == 0:
      util.do_hard_debuff()
      util.do_debuff()

    if sec_difference >= 95:
      cast_mode = True
      cast_mode = True
      util.cancel_aura(1.5)

    if mode == consts.STATE_THREE and cast_mode == True:
      util.do_final_mode()
      util.set_last_cast_mode(mode)
      mode = 2
      cast_mode = False
      mode_time = time.time()
      util.set_mode_exist(False)
      util.set_battle_counter(0)
    elif mode == consts.STATE_TWO and cast_mode == True:
      util.force_battle_mode()
      util.set_last_cast_mode(mode)
      mode = 3
      cast_mode = False
      mode_time = time.time()
      util.set_mode_exist(False)
      util.set_battle_counter(0)

    try:
      if type == consts.TYPE_BOSS: pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_archer_region())
      elif type == consts.TYPE_SEMI: pyauto.locateOnScreen(consts.IMG_SEMI_BOSS, grayscale=False, confidence=.9, region=util.get_archer_region())
      elif type == consts.TYPE_SHADE: pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_archer_region())
      elif type == consts.TYPE_MONSTER: pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_archer_region())
      util.log_action(consts.MSG_ATTACK + unit)
      util.do_special_attack()
    except pyauto.ImageNotFoundException:
      util.log_action(consts.MSG_BOSS_KILLED)
      combo = False

def plunder_box(select=True, reps=4, loot=True, delay=1.0):
  util.log_action(consts.MSG_CHECK_BOX)
  if delay != 0: util.wait(delay)
  if select == consts.IS_TRUE: util.do_select(0.1)

  checking = True
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BOX_FOUND)
      util.do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_BOX_NOT_FOUND)

  if loot == consts.IS_TRUE:
    util.do_plunder(reps)

def plunder_box_party(select=True, reps=4, loot=True, delay=1.0):
  util.log_action(consts.MSG_CHECK_BOX)
  if delay != 0: util.wait(delay)
  if select == consts.IS_TRUE: util.do_select(0.1)

  checking = True
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BOX_FOUND)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_BOX_NOT_FOUND)

  if loot == consts.IS_TRUE:
    util.party_roll_box(reps)

def plunder_final_box_party(select=True, reps=5, loot=True, delay=1.0):
  util.log_action(consts.MSG_CHECK_BOX)
  if delay != 0: util.wait(delay)
  if select == consts.IS_TRUE: util.do_select(0.1)

  checking = True
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BOX_FOUND)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_BOX_NOT_FOUND)

  if loot == consts.IS_TRUE:
    util.party_roll_box(reps)

def plunder_final_box(select=True, reps=5, loot=True, delay=1.0):
  util.log_action(consts.MSG_CHECK_BOX)
  if delay != 0: util.wait(delay)
  if select == consts.IS_TRUE: util.do_select(0.1)

  checking = True
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
      util.log_action(consts.MSG_BOX_FOUND)
      util.do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_BOX_NOT_FOUND)

  if loot == consts.IS_TRUE: util.do_plunder(reps)

def plunder_ref_box(select=True, reps=4, ref=consts.IMG_BOX, loot=True, delay=1.0):
  util.log_action(consts.MSG_CHECK_BOX)
  if delay != 0: util.wait(delay)
  if select == consts.IS_TRUE: util.do_select(0.1)

  checking = True
  while checking:
    if not util.get_macro_state():
      util.log_action(consts.MSG_TERMINATE)
      checking = False

    if checking == False:
      break

    try:
      box = pyauto.locateOnScreen(ref, grayscale=False, confidence=.8, region=util.get_full_region())
      util.log_action(consts.MSG_BOX_FOUND)
      util.do_attack(0.1)
    except pyauto.ImageNotFoundException:
      checking = False
      util.log_action(consts.MSG_BOX_NOT_FOUND)

  if loot == consts.IS_TRUE: util.do_plunder(reps)
