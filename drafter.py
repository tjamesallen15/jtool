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

class Drafter():
  def initialize(self):
    cabal_window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
    util.set_cabal_window(cabal_window)
    util.go_cabal_window()
    pyauto.displayMousePosition(cabal_window[0], cabal_window[1])

Drafter().initialize()
