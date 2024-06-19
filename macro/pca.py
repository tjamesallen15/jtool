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

def pathFind(unit=util.unitBlank):
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
      gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
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
      gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
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
      gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
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
      gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
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
      gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
      util.logAction(util.msgGateFound + unit)
      pathing = False
      util.logAction(util.msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      util.logAction(util.msgNoGateFound)

    if pathing == False:
      break

    if unit == util.unitGateTwo:
      try:
        util.moveClick(750, 260)
        util.doSelect(0.1)
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
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
        gate = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

  util.attackMobs(util.unitBlank, 0, 0.3, 0)

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
    util.doBuffs()

    # util.moveClick(720, 360)

    # # Enter Dungeon
    # util.enterDungeon()
    # util.challengeDungeon()
    
    # util.move(700, 150)
    # pyauto.mouseDown(button="right")
    # util.move(375, 150)
    # pyauto.mouseUp(button="right")
    # pyauto.scroll(-10000)

    # print("1")
    # util.move(610, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("2")
    # util.move(610, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("3")
    # util.move(610, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("4")
    # util.move(610, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("5")
    # util.move(560, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("6")
    # util.move(610, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("7")
    # util.move(680, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("8")
    # util.move(640, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("9")
    # util.move(570, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("10")
    # util.move(770, 150)
    # util.doDash(1)
    # util.doFade(0.5)


    # print("11")
    # util.move(640, 150)
    # util.doDash(1)
    # util.doFade(0.5)


    # print("13")
    # util.move(500, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("14")
    # util.move(570, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("15")
    # util.move(500, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("16")
    # util.move(640, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("17")
    # util.move(680, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # print("18")
    # util.move(640, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # time.sleep(6)

    # print("19")
    # util.move(660, 150)
    # util.doDash(1)
    # util.doFade(0.5)

    # util.move(610, 440)
    # util.doFade(0.5)

    # util.attackBoss()
    # util.lootBox(2)

    # util.move(380, 300)
    # util.doDash(1)

    # util.moveClick(600, 420)
    # checking = True
    # dialogCount = 0
    # while checking:
    #   if dialogCount == 3:
    #     checking = False
    #     break

    #   try:
    #     dialog = pyauto.locateOnScreen(util.imgCheckDialog, grayscale=False, confidence=.9)
    #     util.logAction(util.msgCheckDialogFound)
    #     util.moveClickRel(10, 10, dialog, 2)
    #     dialogCount += 1
    #   except pyauto.ImageNotFoundException:
    #     util.logAction(util.msgNoCheckDialogFound)

    # util.move(375, 150)
    # pyauto.mouseDown(button="right")
    # util.move(700, 150)
    # pyauto.mouseUp(button="right")
    # pyauto.scroll(-10000)

    # time.sleep(1)

    # util.move(375, 150)
    # pyauto.mouseDown(button="right")
    # util.move(700, 150)
    # pyauto.mouseUp(button="right")
    # pyauto.scroll(-10000)

    # util.move(440, 150)
    # util.doDash(1)
    # util.doFade(0.5)

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

      pathFind()
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)