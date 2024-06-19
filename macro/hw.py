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

    if pathing == False:
        break

    util.logAction(util.msgPathFind + unit)

    if unit == util.unitGateThree:
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
        util.moveClick(650, 260)
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
        util.doDash(0.5)
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
        util.doFade(0.5)
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgGateFound + unit)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoGateFound)

      if pathing == False:
        break

    else:
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
        break

      if unit == util.unitGateTwo:
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

def pathFindLegrinGate(unit=util.unitBlank):
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
  
  if bossFound == 0:
    util.focusGate(util.unitLegrin)

def pathFind(unit=util.unitBlank):
  global sidestep
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

    backTrackCheck += 1
    util.logAction(util.msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)

    if unit == util.unitBox:
      try:
        util.move(680, 160)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      if pathing == False:
        break

      try:
        util.move(660, 160)
        util.doDash(0.5)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      if pathing == False:
        break

      try:
        util.move(640, 160)
        util.doSelect(0.1)
        box = pyauto.locateOnScreen(util.imgHolyBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

      if pathing == False:
        break

    elif unit == util.unitLeo:
      try:
        util.moveClick(600, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(550, 260, 0.5)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(500, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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

    elif unit == util.unitEspi:
      try:
        util.moveClick(700, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(650, 260, 0.5)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(600, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(550, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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
        util.moveClick(500, 260)
        util.doSelect(0.1)
        leo = pyauto.locateOnScreen(util.imgMobs, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        pathing = False
        util.logAction(util.msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

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

    elif unit == util.unitDraco:
      util.doDeselectPack()
      util.move(200, 250)
      util.doDash(1)
      util.doFade(0.5)

      try:
        util.moveClick(600, 260)
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

      try:
        util.moveClick(580, 260, 0.5)
        util.doFade(0.5)
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

    bossCheck += 1
    if bossCheck >= 3 and unit == util.unitDraco:
      util.moveClick(800, 260)
      util.doFade(0.5)
      bossCheck = 0

  interval = 0.3
  if unit == util.unitBox:
    util.attackMobs(unit, 0, interval, sidestep)
  elif bossFound == 0 and boxFound == 0 and unit != util.unitEspi:
    util.attackMobs(unit, 1, interval, sidestep)
  elif bossFound == 0 and boxFound == 0 and unit == util.unitEspi:
    if util.atkType == 0:
      interval = 0.8
    util.attackMobs(unit, 1, interval, sidestep)

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

    if unit == util.unitLeo:
      try:
        util.moveClick(400, 450)
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
        util.moveClick(350, 450)
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
        util.moveClick(300, 450)
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
        util.moveClick(900, 450)
        util.doDash(1)
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
        util.moveClick(950, 450)
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
        util.moveClick(1000, 450)
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

    elif unit == util.unitEspi:
      try:
        util.moveClick(700, 550)
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
        util.moveClick(650, 550)
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
        util.moveClick(600, 550)
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
        util.moveClick(550, 550)
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
        util.moveClick(500, 550)
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
    shortcut.add_hotkey("ctrl+r", util.terminate)
    util.logAction(util.msgStartDg)
    util.logRun(runCounter + 1)

    # Click Cabal Window
    util.goCabalWindow()

    util.releaseKeys(1)
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

    # Enter Dungeon
    util.enterDungeon()
    util.challengeDungeon()

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

      if moving == False:
        break

      pathFindGateOnly(util.unitGateOne)
      try:
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
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

      if moving == False:
        break

      pathFindLegrinGate(util.unitLegrin)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBossFound)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # First Boss
    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)
    util.doFade(0.5)

    util.move(440, 560)
    util.doDash(1)
    util.doFade(0.5)

    util.doDeselectPack()
    util.doShortBuffs()
    util.attackBoss()
    util.lootBox()

    util.move(660, 150)
    pyauto.mouseDown(button="right")
    util.move(375, 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    util.move(500, 250)
    util.doDash(1)

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
        gate = pyauto.locateOnScreen(util.imgGate, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    util.doDeselectPack()
    util.move(620, 150)
    util.doDash(1)

    util.focusGate(util.unitGateTwo)
    
    util.doDeselectPack()
    util.move(400, 240)
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

      if moving == False:
        break

      pathFind(util.unitLeo)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Second Boss
    util.doDeselectPack()

    util.move(620, 150)
    util.doDash(1.2)
    util.move(620, 150)
    util.doDash(1.2)
    util.move(620, 150)
    util.doDash(1.2)
    util.move(820, 550)
    util.doDash(1)

    util.doBattleMode()
    util.attackBoss()
    util.setBattleMode(False)
    util.lootBox()

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
    util.doFade(0.5)

    # Third Sequence
    moving = True
    while moving:
      if not util.macro:
        util.logAction(util.msgTerminate)
        moving = False
        sys.exit()
        break

      if moving == False:
        break

      pathFind(util.unitEspi)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Third Boss
    util.doDeselectPack()
    util.move(620, 500)
    util.doDash(1)
    util.doFade(0.5)

    util.attackBoss()
    util.lootBox()

    util.move(520, 100)
    util.doDash(1)
    util.doFade(0.5)

    util.move(520, 200)
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

    util.move(200, 250)
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

      if moving == False:
        break

      pathFind(util.unitDraco)
      try:
        boss = pyauto.locateOnScreen(util.imgBoss, grayscale=False, confidence=.9, region=util.getHpBar())
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBossFound)

    # Final Boss
    util.doDeselectPack()
    util.doDeselectPack()

    util.move(400, 160)
    util.doDash(1)
    util.doFade(0.5)
    
    util.move(1000, 300)
    util.doDash(1)
    util.doFade(1)

    util.move(610, 160)
    util.doFade(1)

    util.doBattleMode()
    util.doShortBuffs()

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

      if moving == False:
        break

      pathFind(util.unitBox)
      try:
        box = pyauto.locateOnScreen(util.imgBox, grayscale=False, confidence=.9, region=util.getHpBar())
        util.logAction(util.msgBoxFound)
        moving = False
        util.logAction(util.msgMoveStop)
        break
      except pyauto.ImageNotFoundException:
        util.logAction(util.msgNoBoxFound)

    util.doDeselectPack()

    util.move(660, 160)
    util.doDash(1)
    util.doFade(0.5)
    util.doDash(1)
    util.doFade(0.5)

    util.move(700, 250)
    util.moveClick(700, 360)
    util.finalLootBox()

    # Start to End Dungeon
    util.endDungeon()
    util.diceDungeon()

    runCounter += 1
    util.logAction(util.msgEndDg)
    time.sleep(3)
