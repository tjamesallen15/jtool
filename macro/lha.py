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

def pathFind(unit):
  pathing = True
  boss = 0
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
      util.moveClick(600, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

    try:
      util.moveClick(700, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

    try:
      util.moveClick(750, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

    try:
      util.moveClick(800, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

    try:
      util.moveClick(850, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

    try:
      util.moveClick(900, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    time.sleep(0.2)

    if pathing == False:
      break

def pathFindBoss():
  pathing = True
  boss = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if pathing == False:
      break

    try:
      util.moveClick(600, 250)
      util.doDash(1)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(650, 250)
      util.doFade(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(700, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(900, 250)
      util.doFade(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

def pathFindLavaGate(unit=util.unitBlank):
  pathing = True
  boss = 0
  gateCounter = 0
  while pathing:
    if not util.macro:
      util.logAction(util.msgTerminate)
      pathing = False
      sys.exit()
      break

    if pathing == False:
      break

    util.logAction(util.msgPathFind + unit)
    if gateCounter >= 10:
      try:
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break
    else:
      gateCounter += 1
      util.moveClick(350, 250)
      util.moveClick(450, 250)
      util.moveClick(500, 250)
      util.moveClick(550, 250)
      util.moveClick(600, 250)
      util.moveClick(650, 250)
      util.moveClick(700, 250)

def positionDarkArcher():
  util.move(620, 100)
  util.doDash(1)
  util.doFade(0.5)

  util.move(620, 100)
  util.doDash(1)
  util.doFade(0.5)

  util.move(750, 100)
  util.doDash(1)
  util.doFade(0.5)

  util.move(620, 100)
  util.doDash(1)
  util.doFade(0.5)

  util.move(800, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(920, 200)
  util.doDash(1)
  util.doFade(0.5)

def positionGateKeeper():
  util.move(620, 550)
  util.doFade(0.5)

  util.move(820, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(820, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(840, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(615, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(615, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(615, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(615, 200)
  util.doDash(1)
  util.doFade(0.5)

  util.move(350, 420)
  util.doDash(1)
  util.doFade(0.5)

def positionLavaGate():
  util.moveClick(450, 600)
  util.moveClick(450, 600)
  util.moveClick(450, 600)
  util.moveClick(450, 600)
  util.moveClick(250, 500)

def positionBoss():
  util.move(720, 400)
  util.doFade(0.5)

  util.move(375, 150)
  pyauto.mouseDown(button="right")
  util.move(660, 150)
  pyauto.mouseUp(button="right")
  pyauto.scroll(-10000)

  time.sleep(1)

  util.move(300, 420)
  util.doDash(1)
  util.doFade(0.5)

  util.move(300, 420)
  util.doDash(1)
  util.doFade(0.5)

  util.move(480, 160)
  util.doDash(1)
  util.doFade(0.5)

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

    util.moveClick(650, 260)

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

    util.move(620, 260)
    util.doDash(1)

    # First Boss
    util.attackBoss()
    util.move(580, 260)
    util.doFade(0.5)
    util.lootBox(2)

    # First Semi Boss Sequence
    positionDarkArcher()
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitDarkArcher)
      try:
        boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # First Semi Boss
    util.attackSemiBoss(0)

    # Second Semi Boss Sequence
    positionGateKeeper()
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
        boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Semi Boss
    util.attackSemiBoss(0)

    # Gate Sequence
    positionLavaGate()
    pathFindLavaGate(util.unitLavaGate)
    util.focusMobs(util.unitLavaGate, 1, 0)

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
        mobs = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)
    
    util.focusMobs(util.unitLavaGate, 1, 0)

    # Boss Sequence
    positionBoss()
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

    # Final Boss
    util.doBattleMode()
    util.doShortBuffs()
    util.attackBoss()
    util.lootBox(2)
    util.setBattleMode(False)

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()

    runCounter += 1
    util.logAction(util.msgEndDg)
    time.sleep(3)