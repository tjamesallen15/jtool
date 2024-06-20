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
    util.moveClick(675, 450)
    util.logAction(util.msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)

    try:
      util.moveClick(600, 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(500, 260, 0.5)
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
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    if unit == util.unitMossToad:
      try:
        util.moveClick(475, 260)
        util.doFade()
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

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
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(450, 260)
        util.doFade()
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

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
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

    try:
      util.moveClick(400, 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(300, 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(200, 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    if unit == util.unitLumberMoth:
      try:
        util.moveClick(200, 360)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBossFound)
        pathing = False
        bossFound = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

  if bossFound == 0:
    util.attackMobs(unit)

def pathBackTrack(unit):
  backtracking = True
  bossFound = 0
  backTrackCancel = 0
  while backtracking:
    if not util.macro:
      util.logAction(util.msgTerminate)
      backtracking = False
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
      util.moveClick(650, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if backtracking == False:
      break

    try:
      util.moveClick(700, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if backtracking == False:
      break

    try:
      util.moveClick(750, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if backtracking == False:
      break

    try:
      util.moveClick(800, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if backtracking == False:
      break

    try:
      util.moveClick(850, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if backtracking == False:
      break

  util.attackMobs(unit)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    runCounter += 1
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter)

    # Click Cabal Window
    util.goCabalWindow()

    # Click Dungeon
    util.move(677, 361)
    util.move(735, 361, 0.5)
    util.moveClick(735, 361, 0.5)

    # Enter Dungeon
    util.enterDungeon()
    util.challengeDungeon()

    util.move(250, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.goSkillSlot(0.5)
    util.doBuffs()

    # Initial Position
    util.move(850, 600)
    util.doDash(0.1)

    # Mush and Flower Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitMushFlower)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(850, 600)
    util.doDash(0.1)

    # First Boss
    util.doShortBuffs()

    util.attackBoss()
    util.move(450, 450)
    util.doFade(0.5)
    util.lootBox()

    util.moveClick(400, 260)
    util.doDash(0.5)

    # Mossite and Toad Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitMossToad)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Boss
    util.doDeselectPack()
    util.move(800, 360)
    util.doDash(1)
    util.move(500, 300)
    util.doFade(0.1)

    secondBoss = True
    while secondBoss:
      if not util.macro:
        util.logAction(util.msgTerminate)
        secondBoss = False
        sys.exit()
        break

      if secondBoss == False:
        break

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        secondBoss = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.attackBoss()
    util.doDeselectPack()
    util.move(500, 100)
    util.doFade(0.5)
    util.lootBox()

    # Lumber and Moth Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitLumberMoth)
      try:
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Position for First Orphidia
    util.doDeselectPack()
    util.move(800, 260)
    util.doDash(0.5)

    util.moveClick(500, 260)
    util.moveClick(400, 320)
    util.doDash(1)
    util.doDash(1)
    util.doFade(0.1)

    util.move(320, 540)
    util.doDeselectPack()
    util.doDash(0.5)

    util.move(400, 400)
    util.doFade(0.5)

    # First Orphidia
    try:
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(675, 600)
    util.doDash(0.5)

    util.doBattleMode()

    # Second and Third Orphidia
    bossTracker = 0
    bossCount = 0
    shortBuffsCounter = 0
    while bossCount < 2:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      bossTracker += 1
      if bossTracker >= 60:
        bossTracker = 0
        bossCount += 10
        break

      if (bossCount == 1 and shortBuffsCounter == 0 and util.shortBuffsAllowed == 1):
        shortBuffsCounter = 1
        util.doShortBuffs()

      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        bossCount += 1
        util.attackBoss()
        util.doDeselectPack()
        if (bossCount == 1):
          time.sleep(5)
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Pathfind Treasure Boxes
    boxing = True
    while boxing:
      if not util.macro:
        util.logAction(util.msgTerminate)
        boxing = False
        sys.exit()
        break

      util.logAction(util.msgPathFind + util.unitBox)
      util.moveClick(550, 160)
      time.sleep(1)

      util.doDash(0.5)
      util.moveClick(650, 160, 0.3)
      util.moveClick(750, 160, 0.3)
      util.moveClick(850, 160, 0.3)
      util.moveClick(950, 160, 0.3)
      util.moveClick(950, 480)
      util.doDash(1)
      util.doFade(0.5)

      try:
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        boxing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

    # Loot Treasure Boxes
    boxCounter = 0
    while boxCounter < 10:
      if not util.macro:
        util.logAction(util.msgTerminate)
        boxCounter = False
        sys.exit()
        break

      if boxCounter > 10:
        break

      try:
        util.doSelect(0.1)
        boxCounter += 1
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        util.logAction(util.msgPathStop)
        boxCounter += 2
        util.finalLootBox()
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      try:
        checkenddg = pyauto.locateOnScreen(util.imgEndDg, grayscale=False, confidence=.9)
        boxCounter += 10
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgCheckEndDg)

    util.setBattleMode(False)

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()
    util.logAction(util.msgEndDg)
    time.sleep(3)
