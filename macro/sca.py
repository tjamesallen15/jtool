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
portalCounter = 0

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

def pathFind(unit):
  global portalCounter
  pathing = True
  bossFound = 0
  backTrackCheck = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if pathing == False:
      break

    util.logAction(util.msgPathFind + unit)
    backTrackCheck += 1
    util.moveClick(620, 460)
    util.logAction(util.msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)
    
    try:
      util.moveClick(620, 250)

      if portalCounter % 2 != 0:
        util.doDash(0.5)

      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(620, 250)
      dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9, region=util.getHpBar())
      portalCounter += 1
      util.logAction(util.msgCheckDialogFound)
      util.moveClickRel(10, 10, dialog, 2)

      if portalCounter % 2 == 0:
        util.doDash(0.1)
      else:
        util.move(620, 460)
        util.doFade(0.5)

      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoCheckDialogFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    try:
      util.moveClick(590, 250)
      if portalCounter % 2 != 0:
        util.doDash(0.5)

      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(590, 250)
      dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9, region=util.getHpBar())
      portalCounter += 1
      util.logAction(util.msgCheckDialogFound)
      util.moveClickRel(10, 10, dialog, 2)

      if portalCounter % 2 == 0:
        util.doDash(0.1)
      else:
        util.move(620, 460)
        util.doFade(0.5)
      
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoCheckDialogFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    try:
      util.moveClick(650, 250)
      if portalCounter % 2 != 0:
        util.doDash(0.5)

      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(650, 250)
      dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9, region=util.getHpBar())
      portalCounter += 1
      util.logAction(util.msgCheckDialogFound)
      util.moveClickRel(10, 10, dialog, 2)

      if portalCounter % 2 == 0:
        util.doDash(0.1)
      else:
        util.move(620, 460)
        util.doFade(0.5)

      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoCheckDialogFound)
  
    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

  if bossFound == 0:
    util.attackMobs(unit)

def pathBackTrack(unit):
  backtracking = True
  bossFound = 0
  backTrackCancel = 0
  while backtracking:
    if not util.macro:
      util.logAction(util.msgTerminate)
      combo = False
      sys.exit()
      break

    if backtracking == False:
      break

    backTrackCancel += 1
    util.logAction(util.msgBackTrack + str(backTrackCancel))
    if (backTrackCancel >= 10):
      backTrackCancel = 0
      backtracking = False

    util.logAction(util.msgBackTrack + unit)
    try:
      util.moveClick(620, 460)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(620, 460)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(620, 460)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(620, 460)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

  attackMobs(unit)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter + 1)

    # Click Cabal Window
    util.goCabalWindow()
    util.releaseKeys()

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Click Dungeon
    util.moveClick(600, 240)

    # Enter Dungeon
    util.enterDungeon()
    util.challengeDungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.goSkillSlot(0.5)
    util.doBuffs()

    # Mechape Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitMechape)
      try:
        boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    time.sleep(1)

    # First Boss
    util.doDeselectPack()
    util.doDeselectPack()

    time.sleep(1)
    util.doBattleMode()
    util.attackSemiBoss()
    util.lootBox(2)

    util.setBattleMode(False)

    # Tricus Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitTricus)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)
    
    time.sleep(1)

    # Final Boss
    util.doDeselectPack()
    util.doDeselectPack()
    util.doDash(1)
    util.doShortBuffs()
    util.attackBoss()
    util.doLoot()

    util.move(620, 350)
    util.doDash(0.5)

    util.move(640, 350)
    util.doFade(0.5)

    util.lootBox(2)

    util.setBattleMode(False)
    util.cancelAura(1)
  
    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()

    runCounter += 1
    util.logAction(util.msgEndDg)
    time.sleep(3)
