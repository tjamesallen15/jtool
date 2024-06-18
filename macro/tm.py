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
          util.moveClick(400, 260)
          util.doSelect(0.1)
          mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
          mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
        bossFound = 1
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break
  
  if unit == util.unitEspada or unit == util.unitEspadaII or unit == util.unitEspadaIII:
    util.focusMobs(unit, 1, 0)

  if bossFound == 0 and util.atkType == 0 and unit == util.unitRedonno:
    util.focusMobs(unit, 1, 0)
  elif bossFound == 0:
    util.attackMobs(unit)

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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    if unit == util.unitGateFour:
      try:
        util.moveClick(800, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

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
      util.moveClick(300, 260)
      util.doSelect(0.1)
      gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
      util.logAction(util.msgGateFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)
  
  if bossFound == 0:
    util.focusGate(util.unitPowerSupply, 0)

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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      mobs = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
    util.doBattleMode()
    util.doShortBuffs()
    util.attackBoss()
    util.lootBox(2)
    util.setBattleMode(False)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(700, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(620, 200)
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

      if counter > 4:
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

    util.move(520, 200)
    util.doDash(1)
    util.doFade(0.5)

    util.move(630, 200)
    util.doDash(1)
    util.doFade(0.5)

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

      if counter > 5:
        moving = False
        break

      pathFind(util.unitEspada)
      counter += 1
      print(str(counter))


    util.doSelect(0.1)
    util.focusGate(util.unitPowerSupply, 0)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(900, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

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

      if counter > 4:
        moving = False
        break

      pathFind(util.unitEspadaII)
      counter += 1
      print(str(counter))

    util.doSelect(0.1)
    util.focusGate(util.unitPowerSupply, 0)

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

      if counter > 5:
        moving = False
        break

      pathFind(util.unitEspadaIII)
      counter += 1
      print(str(counter))

    util.doSelect(0.1)
    util.focusGate(util.unitPowerSupply, 0)

    util.move(580, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(900, 300)
    util.doDash(1)
    util.doFade(0.5)

    util.lootBox(2)

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
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Boss
    util.doBattleMode()
    util.doShortBuffs()
    util.attackBoss()
    util.lootBox(2)
    util.setBattleMode(False)

    util.move(580, 260)
    util.doDash(1)
    util.doFade(0.5)

    util.move(570, 550)
    util.doDash(1)
    util.doFade(0.5)

    util.move(570, 550)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(660, 260)
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
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
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
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)
    
    # Third Boss
    util.attackBoss()
    util.lootBox(2)

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
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.focusGate(util.unitGateFour)

    util.doBattleMode()
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
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
    util.lootBox(2)
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