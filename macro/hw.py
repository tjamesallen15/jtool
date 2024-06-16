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

def pathFindGateOnly(unit=util.unitBlank):
  pathing = True
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    util.logAction(util.msgPathFind + unit)
    # util.moveClick(675, 450)

    if unit == util.unitGateThree:
      try:
        util.moveClick(450, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(500, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(600, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(650, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(700, 260)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(750, 260)
        util.doSelect(0.1)
        util.doFade(0.5)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

    else:
      try:
        util.moveClick(600, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(580, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(620, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(540, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      try:
        util.moveClick(660, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

def pathFindLegrinGate(unit=util.unitBlank):
  pathing = True
  boss = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    util.logAction(util.msgPathFind + unit)
    try:
      util.moveClick(600, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

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
      util.moveClick(580, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

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
      util.moveClick(620, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

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
  
  if boss == 0:
    util.focusGate(util.unitLegrin)

def pathFind(unit=util.unitBlank):
  global sidestep
  pathing = True
  boss = 0
  bossCheck = 0
  boxFound = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if unit == util.unitBox:
      try:
        util.move(680, 160)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        util.doDeselectPack()
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      try:
        util.move(660, 160)
        util.doDash(0.5)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        util.doDeselectPack()
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      try:
        util.move(640, 160)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        util.doDeselectPack()
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

    elif unit == util.unitLeo or unit == util.unitEspi:
      try:
        util.moveClick(700, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(650, 260, 0.5)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(600, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(550, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      try:
        util.moveClick(500, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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

    else:
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
        util.moveClick(580, 260, 0.5)
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

      try:
        util.moveClick(620, 260)
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
        util.moveClick(560, 260)
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
        util.moveClick(640, 260)
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

    bossCheck += 1
    if bossCheck >= 3 and unit == util.unitDraco:
      util.moveClick(800, 260)
      util.doFade(0.5)
      bossCheck = 0

  if boss == 0 and boxFound == 0 and unit != util.unitEspi:
    interval = 0.3
    util.attackMobs(unit, util.atkType, interval, sidestep)
  elif boss == 0 and boxFound == 0 and unit == util.unitEspi:
    interval = 0.3
    if util.atkType == 0:
      interval = 0.8

    util.attackMobs(unit, util.atkType, interval, sidestep)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter + 1)

    # Click Cabal Window
    util.goCabalWindow()

    time.sleep(1)
    util.autoEssentials()
    util.goSkillSlot(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    
    # Click Dungeon
    util.move(500, 300)
    util.doDash(1)
    util.moveClick(595, 335, 0.5)
    util.moveClick(595, 335, 0.5)

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

    util.move(740, 420)
    util.doFade(0.5)
    util.doBuffs()

    # Gate I
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFindGateOnly(util.unitGateOne)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    util.move(800, 300)
    util.doDash(1)
    util.doFade(0.5)

    util.doAura()

    util.move(500, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # First Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFindLegrinGate(util.unitLegrin)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.doDeselectPack()
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # First Boss
    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)

    util.move(440, 560)
    util.doDash(1)
    util.doFade(0.5)

    util.doDeselectPack()
    util.doShortBuffs()
    util.attackBoss()
    util.lootBox(2)

    util.move(660, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Gate II
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFindGateOnly(util.unitGateTwo)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)

    util.focusGate(util.unitGateTwo)
    
    util.doDeselectPack()
    util.moveClick(400, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Second Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFind(util.unitLeo)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Boss
    util.doDeselectPack()
    util.attackBoss()
    util.lootBox(2)

    util.move(620, 150)
    util.doDash(1)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(660, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Gate III
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFindGateOnly(util.unitGateThree)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()

    util.move(1000, 360)
    util.doDash(1)
    util.doFade(0.5)
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    util.move(600, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.focusGate(util.unitGateThree)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)

    util.move(1000, 350)
    util.doDash(1)
    util.doFade(1)

    # Third Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFind(util.unitEspi)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Third Boss
    util.doDeselectPack()
    util.attackBoss()
    util.lootBox(2)

    util.move(440, 200)
    util.doDash(1)
    util.doFade(0.5)

    # Gate IV
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFindGateOnly(util.unitGateFour)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)
    util.doFade(1.5)

    util.move(800, 360)
    util.doFade(0.5)

    util.doSelect(0.1)
    util.focusGate(util.unitGateFour)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    util.move(200, 150)
    util.doDash(1)
    util.doFade(0.5)

    # Fourth Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFind(util.unitDraco)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        util.doDeselectPack()
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Final Boss
    util.doDeselectPack()

    util.move(400, 160)
    util.doDash(1)
    util.doFade(0.5)
    
    util.move(1000, 300)
    util.doDash(1)
    util.doFade(1)

    util.move(650, 160)
    util.doFade(1)

    util.doBattleMode()
    util.doShortBuffs()
    util.doSelect(0.1)
    util.attackBoss()

    util.setBattleMode(False)

    # Box Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      pathFind(util.unitBox)
      try:
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9)
        util.doDeselectPack()
        util.logAction(util.msgBoxFound)
        moving = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

    util.move(660, 160)
    util.doDash(1)
    util.doFade(0.5)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 250)
    util.moveClick(700, 360)
    util.finalLootBox(3)

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
