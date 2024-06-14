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
  boss = 0
  backTrackCheck = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    util.logAction(util.msgPathFind + unit)

    backTrackCheck += 1
    pyauto.moveTo(cabalwindow[0] + 675, cabalwindow[1] + 450)
    pyauto.click(cabalwindow[0] + 675, cabalwindow[1] + 450)
    print(util.msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)
    
    try:
      pyauto.moveTo(cabalwindow[0] + 600, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 600, cabalwindow[1] + 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 500, cabalwindow[1] + 260)
      time.sleep(0.5)
      util.doDash(0.5)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)
    
    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if unit == unitMossToad:
      try:
        pyauto.moveTo(cabalwindow[0] + 475, cabalwindow[1] + 260)
        pyauto.click(cabalwindow[0] + 475, cabalwindow[1] + 260)
        util.doFade()
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)
      
      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.logAction(util.msgBossFound)
        pathing = False
        boss = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      try:
        pyauto.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 260)
        pyauto.click(cabalwindow[0] + 450, cabalwindow[1] + 260)
        util.doFade()
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)
      
      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.logAction(util.msgBossFound)
        pathing = False
        boss = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 400, cabalwindow[1] + 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 300, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 300, cabalwindow[1] + 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 200, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 200, cabalwindow[1] + 260)
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if unit == unitLumberMoth:
      try:
        pyauto.moveTo(cabalwindow[0] + 200, cabalwindow[1] + 360)
        pyauto.click(cabalwindow[0] + 200, cabalwindow[1] + 360)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.logAction(util.msgBossFound)
        pathing = False
        boss = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

  if boss == 0:
    util.attackMobs(unit)

def pathBackTrack(unit):
  backtracking = True
  boss = 0
  backTrackCancel = 0
  while backtracking:
    if not util.macro:
      util.logAction(util.msgTerminate)
      combo = False
      sys.exit()
      break

    backTrackCancel += 1
    print(util.msgBackTrack + str(backTrackCancel))
    if (backTrackCancel >= 10):
      backTrackCancel = 0
      backtracking = False

    util.logAction(util.msgBackTrack + unit)
    try:
      pyauto.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 650, cabalwindow[1] + 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 700, cabalwindow[1] + 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 750, cabalwindow[1] + 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 800, cabalwindow[1] + 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 850, cabalwindow[1] + 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

  util.attackMobs(unit)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter + 1)

    # Click Cabal Window
    util.goCabalWindow()

    # Click Dungeon
    util.move(677, 361)
    util.move(735, 361, 0.5)
    util.moveClick(735, 361, 0.5)

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

    util.move(250, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.goSkillSlot(0.5)
    util.doBuffs()

    # Initial Position
    pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 600)
    util.doDash(0.1)

    # Mush and Flower Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFind(util.unitMushFlower)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(850, 600)
    util.doDash(0.1)

    # First Boss
    util.doShortBuffs()

    util.attackBoss()
    pyauto.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 450)
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

      pathFind(util.unitMossToad)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgPathStop)
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

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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

      pathFind(util.unitLumberMoth)
      try:
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgPathStop)
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
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9)
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

      try:
        util.doSelect(0.1)
        boxCounter += 1
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9)
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
    util.cancelAura(3)
  
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
