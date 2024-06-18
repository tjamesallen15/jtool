import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut
import time
import sys

import util

from tkinter import *
from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
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

def positionSecondBoss():
  util.move(700, 350)
  util.doFade(0.5)

  util.move(200, 320)
  util.doDash(1.2)
  util.move(200, 520)
  util.doDash(1.2)

  util.move(600, 520)
  util.doDash(1.2)

  util.move(200, 320)
  util.doDash(1.2)

  util.move(200, 420)
  util.doDash(1.2)

  util.move(620, 280)
  util.doFade(0.5)

def positionFinalBoss():
  util.move(250, 520)
  util.doDash(1.2)

  util.move(550, 600)
  util.doDash(1.2)

  util.move(350, 520)
  util.doDash(1.2)

  util.move(350, 520)
  util.doDash(1.2)

  util.move(350, 520)
  util.doDash(1.2)

  util.move(620, 650)
  util.doDash(1.2)

  util.move(350, 620)
  util.doDash(1.2)

  util.move(350, 560)
  util.doDash(1.2)

  util.move(350, 560)
  util.doDash(1.2)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter + 1)

    # Click Cabal Window
    util.goCabalWindow()
    util.releaseKeys()
    util.goSkillSlot(0.5)

    util.doBuffs()

    util.move(500, 500)
    util.doDash(1)
    util.move(500, 300)
    util.doFade(0.5)

    util.moveClick(570, 300)

    entering = True
    while entering:
      if not util.macro:
        util.logAction(util.msgTerminate)
        entering = False
        sys.exit()
        break

      try:
        enterdg = pyauto.locateOnScreen(util.imgEnterDg, grayscale=False, confidence=.9)
        util.moveClickRel(15, 15, enterdg, 1)
        entering = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoButtonFound)

    challenging = True
    while challenging:
      if not util.macro:
        util.logAction(util.msgTerminate)
        challenging = False
        sys.exit()
        break

      try:
        challengedg = pyauto.locateOnScreen(util.imgChallengeDg, grayscale=False, confidence=.9)
        util.moveClickRel(15, 15, challengedg, 1)
        challenging = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoButtonFound)

    # First Boss
    util.move(570, 300)
    util.doDash(1)

    time.sleep(1)
    util.attackBoss()
    time.sleep(1)
    util.cancelAura(2)
    
    util.move(400, 600)
    util.doDash(1)

    try:
      util.moveClick(570, 375)
      util.moveClick(570, 375)
      time.sleep(2)
      dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
      util.logAction(util.msgCheckDialogFound)
      util.moveClickRel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoCheckDialogFound)

    positionSecondBoss()

    util.focusMobs(util.unitSpector)

    util.move(800, 360)
    util.doFade(0.5)

    util.move(1000, 200)
    util.doDash(1.2)
    util.doFade(0.5)

    secondBoss = True
    while secondBoss:
      if secondBoss == False:
         break

      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        secondBoss = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)
        util.attackMobs(util.unitSpector, 0, 0.3, sidestep)

    time.sleep(1)
    util.attackBoss()
    util.lootBox()

    util.move(720, 385)
    util.doDash(1)

    checkDialog = True
    while checkDialog:
      if checkDialog == False:
        break

      try:
        util.moveClick(610, 300)
        util.moveClick(610, 305)
        util.moveClick(610, 310)
        time.sleep(1)
        dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
        util.logAction(util.msgCheckDialogFound)
        util.moveClickRel(10, 10, dialog, 2)
        checkDialog = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoCheckDialogFound)

    # Final Boss
    positionFinalBoss()
    util.doBattleMode()
    util.doShortBuffs()
    time.sleep(1)
    util.attackBoss()
    util.lootBox()

    util.move(600, 600)
    util.doDash(1.2)

    try:
      util.moveClick(540, 435)
      util.moveClick(540, 440)
      util.moveClick(540, 445)
      time.sleep(1)
      dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
      util.logAction(util.msgCheckDialogFound)
      util.moveClickRel(10, 10, dialog, 2)
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoCheckDialogFound)

    util.setBattleMode(False)

    # Start to End Dungeon
    ending = True
    endCheckTrack = 0
    while ending:
      if not util.macro:
        util.logAction(util.msgTerminate)
        ending = False
        sys.exit()
        break

      endCheckTrack += 1
      if (endCheckTrack >= 60):
        ending = False
        break

      try:
        enddungeon = pyauto.locateOnScreen(util.imgEndDg, grayscale=False, confidence=.9)
        util.moveClickRel(50, 15, enddungeon, 0.5)
        ending = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgCheckEndDg)
    
    dicing = True
    while dicing:
      if not util.macro:
        util.logAction(util.msgTerminate)
        dicing = False
        sys.exit()
        break

      try:
        rolladice = pyauto.locateOnScreen(util.imgDiceRoll, grayscale=False, confidence=.9)
        util.moveClickRel(50, 15, rolladice, 0.8)
        util.moveClickRel(50, 15, rolladice)
        dicing = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgDiceRoll)

    runCounter += 1
    util.logAction(util.msgEndDg)
    time.sleep(3)
