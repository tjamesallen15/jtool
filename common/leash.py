import time
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import common.util as util
pynboard = Controller()

inventory_matrix = []
x_start_point = 1050
y_start_point = 375

val_inventory = "i"
val_escape = Key.esc
train_macro = True

def generate_matrix():
  global inventory_matrix
  rows = 8
  cols = 8
  for i in range(rows):
    y_point = (y_start_point) + i * 28
    for j in range(cols):
      x_point = (x_start_point) + j * 27
      inventory_matrix.append([x_point, y_point])

def get_inventory_matrix():
  return inventory_matrix

def terminate():
  set_train_state(False)

def get_train_state():
  return train_macro

def set_train_state(val):
  global train_macro
  train_macro = val

def close_window():
  pynboard.press(val_escape)
  pynboard.release(val_escape)
  time.sleep(0.5)

def open_inventory():
  pynboard.press(val_inventory)
  pynboard.release(val_inventory)

def click_npc(x, y):
  util.move(x, y)
  util.move_click(x, y)
  util.move_click(30, 540)
  util.move_click(30, 500, 0.5)
  util.move_click(30, 500)
  time.sleep(0.5)

def click_pet():
  util.move_click(1050, 375)
  util.move_click(50, 200)
  time.sleep(0.5)

def click_core(slot):
  util.move_click(get_inventory_matrix()[slot][0], get_inventory_matrix()[slot][1], 0.1)
  util.move_click(175, 200)
  time.sleep(0.5)

def click_train():
  util.move(100, 400)
  util.move_click(100, 400, 8)

def click_untrain():
  open_inventory()
  util.move_right_click(1075, 375)
  util.move_click(1050, 375)
  util.move_click(890, 300)
  util.move_click(750, 345)

def click_test_npc(x, y):
  util.move(x, y)
  util.move_click(x, y)

def pet_train(x, y, mcr=0, crt=0, cdi=0, crr=0, eva=0):
  shortcut.add_hotkey(util.HOTKEY_TERMINATE, terminate)
  set_train_state(True)
  if mcr != 0 or crt != 0 or cdi != 0 or crr != 0 or eva != 0:
    index = 2
    pet_training = True
    skill_found = False
    while pet_training:
      if not get_train_state():
        pet_training = False

      if index >= 64:
        pet_training = False

      if pet_training == False:
        break

      click_npc(x, y)
      click_pet()
      click_core(index)
      click_train()

      if mcr == util.STATE_ONE:
        try:
          skill_icon = pyauto.locateOnScreen(util.IMG_MAX_CRIT_RATE, grayscale=False, confidence=.9, region=util.get_train_region())
          skill_found = True
        except pyauto.ImageNotFoundException:
          pass

      if crt == util.STATE_ONE and skill_found == False:
        try:
          skill_icon = pyauto.locateOnScreen(util.IMG_CRIT_RATE, grayscale=False, confidence=.9, region=util.get_train_region())
          skill_found = True
        except pyauto.ImageNotFoundException:
          pass

      if cdi == util.STATE_ONE and skill_found == False:
        try:
          skill_icon = pyauto.locateOnScreen(util.IMG_CRIT_DAMAGE, grayscale=False, confidence=.9, region=util.get_train_region())
          skill_found = True
        except pyauto.ImageNotFoundException:
          pass

      if crr == util.STATE_ONE and skill_found == False:
        try:
          skill_icon = pyauto.locateOnScreen(util.IMG_CRIT_RESIST, grayscale=False, confidence=.9, region=util.get_train_region())
          skill_found = True
        except pyauto.ImageNotFoundException:
          pass

      if eva == util.STATE_ONE and skill_found == False:
        try:
          skill_icon = pyauto.locateOnScreen(util.IMG_EVA, grayscale=False, confidence=.9, region=util.get_train_region())
          skill_found = True
        except pyauto.ImageNotFoundException:
          pass

      if skill_found == True:
        pet_training =  False
      else:
        close_window()
        click_untrain()

      if pet_training == False:
        break

      index += 1
