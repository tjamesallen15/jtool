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

def pathFind(unit=util.unitBlank):
  pathing = True
  bossFound = 0
  bossCheck = 0
  boxFound = 0
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
    if unit == util.unitLihonar or unit == util.unitEspada or unit == util.unitEspadaII or unit == util.unitEspadaIII:

      if unit != util.unitEspadaII:
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

        if pathing == False:
          break

        try:
          util.moveClick(500, 260)
          util.doSelect(0.1)
          mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
          util.logAction(util.msgMobsFound + unit)
          pathing = False
          util.logAction(util.msgPathStop)
          break
        except pyauto.ImageNotFoundException:
          util.logAction(util.msgNoMobsFound)

        if pathing == False:
          break

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

      if pathing == False:
        break

      try:
        util.moveClick(580, 260)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(620, 260)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(560, 260)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(640, 260)
        util.doSelect(0.1)
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      pathing == False
      break
    else:
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
        util.moveClick(580, 260, 0.5)
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
        util.moveClick(620, 260)
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
        util.moveClick(560, 260)
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
        util.moveClick(640, 260)
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

  if unit == util.unitEspada or unit == util.unitEspadaII or unit == util.unitEspadaIII:
    util.focusMobs(unit, 1, 0, sidestep)

  if bossFound == 0 and util.atkType == 0 and unit == util.unitRedonno:
    util.focusMobs(unit, 1, 0, sidestep)
  elif bossFound == 0 and util.atkType == 0 and unit == util.unitPoerte:
    util.focusMobs(unit, 1, 0, sidestep)
  elif bossFound == 0:
    util.attackMobs(unit, 1, 0.3, sidestep)

def pathFindGateOnly(unit=util.unitBlank):
  pathing = True
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if pathing == False:
        break

    util.logAction(util.msgPathFind + unit)
    try:
      util.moveClick(600, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    try:
      util.moveClick(580, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    try:
      util.moveClick(620, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    try:
      util.moveClick(540, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    try:
      util.moveClick(660, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      breakx

    if unit == util.unitGateFour:
      try:
        util.moveClick(450, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(500, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(550, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(700, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(750, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(800, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

      try:
        util.moveClick(850, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

def pathFindPowerSupply(unit=util.unitBlank):
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
    try:
      util.moveClick(600, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    try:
      util.moveClick(580, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    try:
      util.moveClick(620, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    try:
      util.moveClick(300, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

def pathFindBoss():
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

    try:
      util.moveClick(600, 260)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(620, 260)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(580, 160)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(660, 160)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(540, 160)
      util.doSelect(0.1)
      util.logAction(util.msgCheckBoss)
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      bossFound = 1
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    runCounter += 1
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter)

    # Click Cabal Window
    util.goCabalWindow()
    util.releaseKeys()
    util.goSkillSlot(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Click Dungeon
    util.moveClick(600, 240)

    util.enterDungeon()
    util.challengeDungeon()

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.goSkillSlot(0.5)
    util.doBuffs()

    # Mech Lion Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitMechLion)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # First Boss
    util.doShortBuffs()
    util.doBattleMode()
    util.attackBoss()
    util.lootBox()
    util.setBattleMode(False)

    util.move(700, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(670, 200)
    util.doDash(1)
    util.doFade(0.5)

    util.focusGate(util.unitGateOne)

    # Lihonar Sequence
    moving = True
    counter = 0
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      if counter > 6:
        moving = False
        break

      pathFind(util.unitLihonar)
      counter += 1
      print(str(counter))

    util.move(600, 400)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(350, 200)
    util.doDash(1)
    util.doFade(0.5)

    util.move(350, 200)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # time.sleep(1)

    # util.move(400, 500)
    # util.doFade(0.5)

    # util.move(630, 200)
    # util.doDash(1)
    # util.doFade(0.5)

    # Gate II
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFindGateOnly(util.unitGateTwo)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.focusGate(util.unitGateTwo)

    util.move(660, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(660, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Espada Sequence
    moving = True
    counter = 0
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      if counter > 6:
        moving = False
        break

      pathFind(util.unitEspada)
      counter += 1
      print(str(counter))


    util.move(320, 550)
    util.doDash(1)
    util.doFade(0.5)

    util.focusGate(util.unitPowerSupply)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(900, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(400, 360)
    util.doFade(0.5)

    util.move(550, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(550, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Espada II Sequence
    moving = True
    counter = 0
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      if counter > 6:
        moving = False
        break

      pathFind(util.unitEspadaII)
      counter += 1
      print(str(counter))

    util.focusGate(util.unitPowerSupply)

    util.move(600, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    # Espada III Sequence
    moving = True
    counter = 0
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      if counter > 4:
        moving = False
        break

      pathFind(util.unitEspadaIII)
      counter += 1
      print(str(counter))

    util.focusGate(util.unitPowerSupply)

    util.move(580, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(900, 300)
    util.doDash(1)
    util.doFade(0.5)

    util.lootBox()

    util.move(640, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Poerte Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitPoerte)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Boss
    util.doShortBuffs()
    util.doBattleMode()
    util.attackBoss()
    util.lootBox()
    util.setBattleMode(False)

    util.move(580, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(570, 550)
    util.doDash(1)
    util.doFade(0.5)

    util.move(580, 550)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(650, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Gate III
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFindGateOnly(util.unitGateThree)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.focusGate(util.unitGateThree)

    # Redonno Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitRedonno)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Third Boss
    util.doBattleMode()
    util.attackBoss()
    util.setBattleMode(False)
    util.lootBox()

    if util.battleMode == 1:
      time.sleep(20)

    util.move(720, 260)
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

      if moving == False:
        break

      pathFindGateOnly(util.unitGateFour)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.focusGate(util.unitGateFour)

    # Final Boss
    util.doBattleMode()
    util.doAuraStrict()
    util.doShortBuffs()

    # Final Boss Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFindBoss()
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(560, 260)
    util.doDash(1)
    util.doFade(0.5)

    # Final Boss
    util.attackBoss()
    util.finalLootBox()
    util.setBattleMode(False)

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()
    util.logAction(util.msgEndDg)
    time.sleep(3)