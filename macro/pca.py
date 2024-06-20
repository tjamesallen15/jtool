import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

import util
pynboard = Controller()

# GLOBAL VARIABLES
rootFrame = []
startButton = []

# UNIQUE VARIABLES
sidestep = 0

def initialize(frame, btn, runs=1):
  global rootFrame
  rootFrame = frame

  global startButton
  startButton = btn

  startButton.config(state="disabled")
  rootFrame.update()
  runDungeon(int(runs))
  startButton.config(state="active")
  rootFrame.update()

def positionNualle():
  util.move(610, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(610, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(610, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(610, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(560, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(610, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(680, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(640, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(570, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(770, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(640, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(500, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(570, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(500, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(640, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(680, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(640, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.doAuraStrict(1)
  util.doAura(1)
  time.sleep(4)

  util.move(660, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(610, 440)
  util.doFade(1)

  util.move(680, 380)
  util.doFade(1)

def positionFirstShadow():
  util.move(460, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(640, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(820, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(750, 300)
  util.doDash(1)

  util.move(600, 350)
  util.doFade(0.5)

  util.move(620, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(580, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(580, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.moveClick(580, 350, 2)

  util.move(760, 300)
  util.doDash(1)
  util.doFade(0.5)

  util.move(720, 200)
  util.doDash(1)

def positionSecondShadow():
  util.move(720, 200)
  util.doFade(1)

  util.move(720, 200)
  util.doFade(0.5)

  util.move(780, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(730, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(760, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(670, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(620, 200)
  util.doDash(1)
  util.doFade(0.5)

def positionThirdShadow():
  util.move(670, 230)
  util.doDash(1)
  util.doFade(0.5)

  util.move(690, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(690, 150)
  util.doDash(1)
  util.doFade(0.5)

  util.move(690, 150)
  util.doDash(1)

def runDungeon(runs=1):
  runCounter = 0
  triggerContinue = False
  while runCounter < runs:
    triggerContinue = False
    runCounter += 1
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter)

    # Click Cabal Window
    util.goCabalWindow()
    util.releaseKeys()
    util.goSkillSlot(0.5)
    util.doBuffs()

    util.moveClick(720, 360)

    # Enter Dungeon
    util.enterDungeon()
    util.challengeDungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    positionNualle()
    # First Boss Sequence
    util.forceShortBuffs()
    util.attackBoss()

    time.sleep(3)
    util.moveClick(590, 460)
    util.doFade(1)

    time.sleep(2)
    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(1000, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.lootBox(1)
    util.cancelAura(2)

    util.move(1000, 520)
    util.doDash(1)

    util.moveClick(580, 440)
    checking = True
    dialogCount = 0
    while checking:
      if not util.macro:
        util.logAction(util.msgTerminate)
        checking = False
        sys.exit()
        break

      if checking == False:
        break

      if dialogCount == 3:
        checking = False
        break

      try:
        dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
        util.logAction(util.msgCheckDialogFound)
        util.moveClickRel(10, 10, dialog, 2)
        dialogCount += 1
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoCheckDialogFound)
        util.forceExitDungeon()
        checking = False
        triggerContinue = True

    if triggerContinue:
      print("continue")
      continue

    positionFirstShadow()
    # First Shadow
    time.sleep(3)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiFear, 0, 0, 0)
    time.sleep(1)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiFear, 0, 0, 0)
    time.sleep(1)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiFear, 0, 0, 0)

    positionSecondShadow()
    # Second Shadow
    time.sleep(3)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiResignation, 0, 0, 0)
    time.sleep(1)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiResignation, 0, 0, 0)

    positionThirdShadow()
    # Third Shadow
    time.sleep(3)
    util.doSelect(0.1)
    util.focusMobs(util.unitShoworaiMadness, 0, 0, 0)

    util.moveClick(580, 430)
    checking = True
    while checking:
      if checking == False:
        break

      try:
        dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
        util.logAction(util.msgCheckDialogFound)
        util.moveClickRel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoCheckDialogFound)
        util.forceExitDungeon()
        checking = False
        triggerContinue = True

    if triggerContinue:
      print("continue")
      continue

    # Final Boss
    util.doBattleMode()
    util.attackBoss(1, 0)
    util.setBattleMode(False)

    time.sleep(1)
    util.moveClick(580, 430)
    checking = True
    while checking:
      if not util.macro:
        util.logAction(util.msgTerminate)
        checking = False
        sys.exit()
        break

      if checking == False:
        break

      try:
        dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
        util.logAction(util.msgCheckDialogFound)
        util.moveClickRel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoCheckDialogFound)
        util.forceExitDungeon()
        checking = False
        triggerContinue = True

    if triggerContinue:
      print("continue")
      continue

    util.moveClick(580, 430)
    util.moveClick(580, 300)
    checking = True
    while checking:
      if not util.macro:
        util.logAction(util.msgTerminate)
        checking = False
        sys.exit()
        break

      if checking == False:
        break

      try:
        dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
        util.logAction(util.msgCheckDialogFound)
        util.moveClickRel(10, 10, dialog, 2)
        checking = False
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoCheckDialogFound)
        util.forceExitDungeon()
        checking = False
        triggerContinue = True

    if triggerContinue:
      print("continue")
      continue

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()
    util.logAction(util.msgEndDg)
    time.sleep(3)
