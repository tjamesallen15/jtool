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
      util.moveClick(350, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(400, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(450, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(500, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break

    try:
      util.moveClick(550, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

    if pathing == False:
      break      

    try:
      util.moveClick(600, 250)
      util.doDash(0.5)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgMobsFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoMobsFound)

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
      util.moveClick(350, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(400, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(450, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(500, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(550, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
      util.logAction(util.msgBossFound)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoBossFound)

    if pathing == False:
      break

    try:
      util.moveClick(600, 250)
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      util.doSelect(0.1)
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
      boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9)
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
    if gateCounter >= 12:
      try:
        util.moveClick(350, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(400, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(450, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(500, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(550, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(600, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(650, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        util.logAction(util.msgMobsFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoMobsFound)

      if pathing == False:
        break

      try:
        util.moveClick(700, 250)
        util.doDash(0.5)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
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
      print(gateCounter)
      util.moveClick(350, 250)
      util.moveClick(450, 250)
      util.moveClick(500, 250)
      util.moveClick(550, 250)
      util.moveClick(600, 250)
      util.moveClick(650, 250)
      util.moveClick(700, 250)

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

    util.move(620, 260)
    util.doDash(1)

    util.attackBoss()

    util.move(580, 260)
    util.doFade(0.5)

    util.lootBox()

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

    util.move(880, 200)
    util.doDash(1)
    util.doFade(0.5)

    util.move(800, 420)
    util.doFade(0.5)

    # First Semi Boss Sequence
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
        boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.attackSemiBoss(0)
    util.move(880, 200)
    util.doDash(1)
    util.doFade(0.5)

    # Second Semi Boss Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitLavaArcher)
      try:
        boss = pyauto.locateOnScreen(util.imgSemiBoss, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.attackSemiBoss(0)

    util.moveClick(290, 400)
    util.moveClick(295, 400)
    util.moveClick(300, 400)
    util.moveClick(310, 400)
    util.moveClick(315, 400)
    util.moveClick(320, 400, 2)

    # Gate Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFindLavaGate(util.unitLavaGate)
      try:
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.focusMobs(util.unitLavaGate, 0)

    util.move(375, 150)
    pyauto.mouseDown(button="right")
    util.move(660, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    time.sleep(1)

    util.move(300, 320)
    util.doDash(1)
    util.doFade(0.5)
  
    # Boss Sequence
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

    util.attackBoss()
    util.lootBox()
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