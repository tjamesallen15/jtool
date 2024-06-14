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
difficulty = "Hazardous Valley (Easy)"
dungeonList = [
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)"
]

def initialize(frame, btn, diff, runs=1):
  global rootFrame
  rootFrame = frame

  global startButton
  startButton = btn

  global difficulty
  difficulty = diff
  
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
    util.moveClick(675, 450)
    print(util.msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)
    
    try:
      util.moveClick(600, 260)
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
      util.moveClick(500, 260, 0.5)
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

    if unit == util.unitCutterToad:
      # try:
      #   util.moveClick(475, 260)
      #   util.doFade()
      #   util.doSelect(0.1)
      #   mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      #   util.logAction(util.msgMobsFound + unit)
      #   pathing = False
      #   util.logAction(util.msgPathStop)
      #   break
      # except pyauto.ImageNotFoundException:
      #   util.logAction(util.msgNoMobsFound)
      
      # try:
      #   util.doSelect(0.1)
      #   util.logAction(util.msgCheckBoss)
      #   boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      #   util.logAction(util.msgBossFound)
      #   pathing = False
      #   boss = 1
      #   util.logAction(util.msgPathStop)
      #   break
      # except pyauto.ImageNotFoundException:
      #   util.logAction(util.msgNoMobsFound)

      try:
        util.moveClick(450, 260)
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
      util.moveClick(400, 260)
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
      util.moveClick(300, 260)
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
      util.moveClick(200, 260)
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

    if unit == util.unitBoarSnake:
      try:
        util.moveClick(200, 360)
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

def pathFindBoss(unit):
  pathing = True
  boss = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    util.logAction(util.msgPathFind + unit)
    util.moveClick(675, 450)

    util.moveClick(600, 260)
    util.doDash(0.5)
    util.doSelect(0.1)
    util.logAction(util.msgCheckBoss)

    util.moveClick(500, 260, 0.5)
    util.doDash(0.5)
    util.doSelect(0.1)
    util.logAction(util.msgCheckBoss)

    try:
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound)
      util.focusMobs(util.unitWhiteSnake)
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    util.moveClick(400, 260)
    util.moveClick(300, 260)
    util.moveClick(200, 260)

    try:
      util.moveClick(200, 360)
      util.doDash(0.5)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      util.doDeselectPack()
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.moveClick(200, 160)
      util.doDash(0.5)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      boss = 1
      util.logAction(util.msgPathStop)
      util.doDeselectPack()
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.moveClick(650, 560)
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
      util.moveClick(700, 560)
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
      util.moveClick(750, 560)
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
      util.moveClick(800, 560)
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
      util.moveClick(850, 560)
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

def positionOrphidia():
  util.doDeselectPack()
  util.move(400, 260)
  util.doDash(1)
  util.doFade(1.5)

  util.move(320, 540)
  util.doDeselectPack()
  util.doDash(0.5)

  util.move(400, 400)
  util.doFade(0.5)

def pathFindWhiteSnake():
  util.logAction(util.msgPathFind + util.unitWhiteSnake)
  util.moveClick(550, 160, 1)
  util.doDash(0.5)

  util.moveClick(650, 160, 0.3)
  util.moveClick(750, 160, 0.3)
  util.doDash(1)

  util.moveClick(850, 160, 1)
  util.doFade(0.5)

  util.moveClick(950, 480)
  util.doDash(1)
  util.doFade(0.5)

  util.moveClick(850, 570)
  util.doDash(1)
  util.doFade(0.5)

  util.moveClick(850, 600)
  util.doDash(1)
  util.doFade(0.5)

  util.moveClick(850, 600)
  util.doDash(1)

def moveToBox():
  util.moveClick(675, 450)
  util.moveClick(500, 260)
  time.sleep(1)

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

    if difficulty == dungeonList[0]:
      util.moveClick(440, 300, 1)
    elif difficulty == dungeonList[1]:
      util.moveClick(440, 280, 1)
    elif difficulty == dungeonList[2]:
      util.moveClick(440, 260, 1)

    entering = True
    while entering:
      try:
        enterdg = pyauto.locateOnScreen(util.imgEnterDg, grayscale=False, confidence=.9)
        util.moveClickRel(15, 15, enterdg, 1)
        entering = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoButtonFound)

    challenging = True
    while challenging:
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

    util.move(340, 260, 0.3)
    util.doDash(0.5)

    # Cutter and Toad Sequence
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      pathFind(util.unitCutterToad)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # First Boss
    util.doDeselectPack()
    util.move(800, 470)
    util.doDash(1)
    util.move(500, 300)
    util.doFade(0.1)

    firstBoss = True
    while firstBoss:
      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        firstBoss = False
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)
    
    util.attackBoss()
    util.doDeselectPack()
    util.moveClick(620, 260)
    util.doFade(1.5)
    util.doFade(0.5)

    moveToBox()
    util.lootBox()

    # Boars and Snakes Sequence
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      pathFind(util.unitBoarSnake)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Position for First Orphidia
    positionOrphidia()

    # First Orphidia
    try:
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.lootBox()
    pathFindWhiteSnake()

    # Boars and Snakes Sequence II
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

    # Position for Second Orphidia
    util.attackMobs(util.unitWhiteSnake)

    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      pathFindBoss(util.unitOrphidia)
      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(320, 540)
    util.doDash(1)
    util.doFade(1.5)

    # Second Orphidia
    try:
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.lootBox()
    pathFindWhiteSnake()

    # Boars and Snakes Sequence III
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

    # Position for Third Orphidia
    util.attackMobs(util.unitWhiteSnake)

    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break
      
      pathFindBoss(util.unitOrphidia)
      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(320, 540)
    util.doDash(1)
    util.doFade(1.5)

    # Third Orphidia
    try:
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.finalLootBox()

    global isBattleMode
    isBattleMode = False
    util.cancelAura(1)

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
