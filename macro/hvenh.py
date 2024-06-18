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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)
    
    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    if unit == util.unitCutterToad:
      try:
        util.moveClick(450, 260)
        util.doFade()
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)
      
      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    if unit == util.unitBoarSnake:
      try:
        util.moveClick(200, 360)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      try:
        util.doSelect(0.1)
        util.logAction(util.msgCheckBoss)
        mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgBossFound)
        pathing = False
        bossFound = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

  interval = 0.3
  if unit == util.unitCutterToad:
    interval = 0.5

  if bossFound == 0:
    util.attackMobs(unit, 1, interval)

def pathFindBoss(unit):
  pathing = True
  bossFound = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if pathing == False:
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
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      util.doDeselectPack()
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.moveClick(650, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBoxFound)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBoxFound)

    if backtracking == False:
      break

    try:
      util.moveClick(700, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBoxFound)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBoxFound)

    if backtracking == False:
      break

    try:
      util.moveClick(750, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBoxFound)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBoxFound)

    if backtracking == False:
      break

    try:
      util.moveClick(800, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBoxFound)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBoxFound)

    if backtracking == False:
      break

    try:
      util.moveClick(850, 560)
      util.doDash()
      util.doSelect(0.1)
      mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgMobsFound + unit)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    try:
      util.doSelect(0.1)
      box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBoxFound)
      backtracking = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBoxFound)

    if backtracking == False:
      break

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

  # util.moveClick(850, 600)
  # util.doDash(1)

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

    util.releaseKeys()

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

      if moving == False:
        break

      pathFind(util.unitCutterToad)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
        moving = False
        util.logAction(util.msgMoveStop)
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
      if firstBoss == False:
         break

      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
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
    util.lootBox(2)

    # Boars and Snakes Sequence
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      if moving == False:
        break

      pathFind(util.unitBoarSnake)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Position for First Orphidia
    positionOrphidia()

    # First Orphidia
    try:
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.logAction(util.msgBossFound)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.lootBox(2)
    pathFindWhiteSnake()

    # Orphidia Sequence II
    moving = True
    while moving:
      if not util.macro:
          util.logAction(util.msgTerminate)
          moving = False
          sys.exit()
          break

      if moving == False:
        break

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgMobsFound)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

    # Position for Second Orphidia
    util.attackMobs(util.unitWhiteSnake)
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFindBoss(util.unitOrphidia)
      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgMoveStop)
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
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.lootBox(2)
    pathFindWhiteSnake()

    # Orphidia Sequence III
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      try:
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgMobsFound)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

    # Position for Third Orphidia
    util.attackMobs(util.unitWhiteSnake)
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break
      
      pathFindBoss(util.unitOrphidia)
      try:
        util.doSelect(0.1)
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgMoveStop)
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
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.hpBar)
      util.attackBoss()
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    util.move(640, 560)
    util.doFade(0.5)
    util.finalLootBox(3)

    util.setBattleMode(False)

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()

    runCounter += 1
    util.logAction(util.msgEndDg)
    time.sleep(3)
