import time
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from tkinter import *
from tkinter import ttk
from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

import common.guard as guard
import common.config as config
import common.features as features
import common.leash as leash
import common.constants as consts
import common.util as util
import common.attack as atk

from common.dungeon import Dungeon

from macro.hva import HazardousValleyAwakened
from macro.hvenh import HazardousValley
from macro.sca import SteamerCrazyAwakened
from macro.hw import HolyWindmill
from macro.cfa import CatacombsFrostAwakened
from macro.lha import LavaHellfireAwakened
from macro.tm import TerminusMachina
from macro.pca import PanicCaveAwakened
from macro.hk import HolyKeldrasil
from macro.s1p import SienaB1FPrideus
from macro.ci import ChaosInfinity
from macro.hvv import HazardousValleyVeradrix
from macro.rh import RadiantHall
from macro.potf import PurifierOfTheForest
from macro.mi import MirageIsland

pynboard = Controller()

CONNECTOR = ", "
KEY_1 = "1"
KEY_2 = "2"
KEY_EQ = "="
LBL_ATTACK = "Attack"
LBL_PAREN_PREFIX = "("
LBL_PAREN_SUFFIX = ")"
LBL_MOVE_PREFIX = "util.move("
LBL_MOVE_SUFFIX = ")"
LBL_DASH_CON = "util.do_dash()"
LBL_FADE_CON = "util.do_fade()"

LBL_DASH_CON_REL_PREFIX = "util.do_dash_rel("
LBL_DASH_CON_REL_SUFFIX = ")"

LBL_FADE_CON_REL_PREFIX = "util.do_fade_rel("
LBL_FADE_CON_REL_SUFFIX = ")"

cabal_window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
util.set_cabal_window(cabal_window)
util.go_cabal_window()
util.initialize_region()

def on_press(key):
  window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
  if key == keyboard.Key.esc: return False
  try: k = key.char
  except: k = key.name

  if k == KEY_1:
      x, y = pyauto.position()
      true_x = str(x - window[0])
      true_y = str(y - window[1])
      # print(LBL_MOVE_PREFIX + true_x + CONNECTOR + true_y + LBL_MOVE_SUFFIX + LBL_DASH_CON)
      print(LBL_DASH_CON_REL_PREFIX + true_x + CONNECTOR + true_y + LBL_DASH_CON_REL_SUFFIX)
  elif k == KEY_2:
      x, y = pyauto.position()
      true_x = str(x - window[0])
      true_y = str(y - window[1])
      # print(LBL_MOVE_PREFIX + true_x + CONNECTOR + true_y + LBL_MOVE_SUFFIX + LBL_FADE_CON)
      print(LBL_FADE_CON_REL_PREFIX + true_x + CONNECTOR + true_y + LBL_FADE_CON_REL_SUFFIX)
  elif k == KEY_EQ: print(LBL_ATTACK)

  if key == Key.space:
      x, y = pyauto.position()
      true_x = str(x - window[0])
      true_y = str(y - window[1])
      print(LBL_PAREN_PREFIX + true_x + CONNECTOR + true_y + LBL_PAREN_SUFFIX)

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

class Drafter(Dungeon):
  def run_dungeon(self, runs):
    return super().run_dungeon(runs)

  def initialize(self):
    pyauto.displayMousePosition(cabal_window[0], cabal_window[1])

Drafter().initialize()
