import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut
import time
import sys

from tkinter import *
from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
pynboard = Controller()

# GLOBAL VARIABLES
select = 'z'
dash = '1'
fade = '2'
attack = ['3', '4', '5']
buffAttack = ['6']
loot = '7'
fury = '8'
pots = '9'
bmaura = '0'
bm3atk = '-'
bm3 = '='
lootSpace = Key.space

# GLOBAL VALIDATION
cabalwindow = []
rootFrame = []
macroLbl = []
startButton = []
combo = True
pathing = True
moving = True
boxing = True
macro = True

# GLOBAL MESSAGES
msgStartDg = "Starting Dungeon"
msgEndDg = "End Dungeon"
msgExit = "Macro Exit"
msgTerminate ="Macro Terminate"
msgBackTrack = "Backtrack, "
msgPathFind = "Pathfind, "
msgAttackMobs = "Attack, "
msgAttackBoss = "Boss Attack"
msgMobsFound = "Mobs Found, "
msgBossFound = "Boss Found"
msgBossKilled = "Boss Killed"
msgNoMobsFound = "No Mobs Found"
msgNoBossFound = "No Boss Found"
msgMobsCleared = "Mobs Cleared"
msgNoVineFound = "No Vine Found"
msgBoxFound = "Box Found"
msgNoBoxFound = "No Box Found"
msgPathStop = "Pathing stop, proceeds to attack"
msgAction = "Action, "

# GLOBAL PICTURES
imgCabalWindow = "cabalwindow.jpg"
imgChallengeDg = "challengedg.jpg"
imgDungeon = "dungeon.jpg"
imgEnterDg = "enterdg.jpg"
imgEndDg = "enddg.jpg"
imgExitDg = "exitdg.jpg"
imgDualBoss = "dualboss.jpg"
imgBoss = "boss.jpg"
imgSemiBoss = "semiboss.jpg"
imgMobs = "mobs.jpg"
imgDiceRoll = "rolladice.jpg"
imgBox = "box.jpg"
imgWarp = "warp.jpg"
imgVine1 = "vineblock1.jpg"
imgVine2 = "vineblock2.jpg"

# GLOBAL UNITS
unitMushFlower = "Mushed and Ectoflower"
unitMossToad = "Mossites and Toad"
unitLumberMoth = "Lumber and Moth"

def initialize(frame, btn, lbl, runs=1):
  global rootFrame
  rootFrame = frame

  global startButton
  startButton = btn
  
  global macroLbl
  macroLbl = lbl
  
  startButton.config(state="disabled")
  runDungeon(int(runs))

def logAction(message):
  msgBuilder = StringVar()
  msgBuilder = msgAction + message
  macroLbl.config(text=msgBuilder)
  rootFrame.update()

def terminate():
  logAction(msgExit)
  global macro
  macro = False

def doHardBuffs():
  pyauto.moveTo(cabalwindow[0] + 470, cabalwindow[1] + 670)
  pyauto.click(button="right")
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 670)
  pyauto.click(button="right")
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 540, cabalwindow[1] + 670)
  pyauto.click(button="right")
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 570, cabalwindow[1] + 670)
  pyauto.click(button="right")
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 640, cabalwindow[1] + 360)

def cancelAura():
  pyauto.moveTo(cabalwindow[0] + 175, cabalwindow[1] + 100)
  pyauto.click(button="right")

def doDash():
  pynboard.press(dash)
  pynboard.release(dash)

def doFade():
  pynboard.press(fade)
  pynboard.release(fade)

def doSelect():
  pynboard.press(select)
  pynboard.release(select)

def lootBox():
  pynboard.press(select)
  pynboard.release(select)
  pynboard.press(bm3atk)
  pynboard.release(bm3atk)
  pynboard.press(attack[0])
  pynboard.release(attack[0])
  pynboard.press(attack[1])
  pynboard.release(attack[1])
  pynboard.press(attack[2])
  pynboard.release(attack[2])
  pynboard.press(bm3atk)
  pynboard.release(bm3atk)
  for x in range(4):
    pynboard.press(loot)
    pynboard.release(loot)
    time.sleep(0.5)
    pynboard.press(lootSpace)
    pynboard.release(lootSpace)
    time.sleep(0.5)

def autoEssentials():
  pynboard.press(lootSpace)
  pynboard.release(lootSpace)
  pynboard.press(fury)
  pynboard.release(fury)
  pynboard.press(pots)
  pynboard.release(pots)
  pynboard.press(loot)
  pynboard.release(loot)

  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

def doAura():
  pynboard.press(bm3)
  pynboard.release(bm3)
  autoEssentials()
  pynboard.press(bmaura)
  pynboard.release(bmaura)
  autoEssentials()
  pynboard.press(bm3)
  pynboard.release(bm3)

def doAttack():
  pynboard.press(bm3atk)
  pynboard.release(bm3atk)
  autoEssentials()
  pynboard.press(bm3atk)
  pynboard.release(bm3atk)
  autoEssentials()
  pynboard.press(bm3atk)
  pynboard.release(bm3atk)
  pynboard.press(attack[0])
  pynboard.release(attack[0])
  autoEssentials()
  pynboard.press(attack[1])
  pynboard.release(attack[1])
  autoEssentials()
  pynboard.press(attack[2])
  pynboard.release(attack[2])
  autoEssentials()

def attackMobs(unit="NA"):
  combo = True
  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break
    
    doAura()
    try:
      doSelect()
      time.sleep(0.1)

      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgAttackMobs + unit)

      doAttack()
      time.sleep(0.3)

      doAttack()
      time.sleep(0.3)
    except pyauto.ImageNotFoundException:
      logAction(msgMobsCleared)
      combo = False
      break

def attackBoss():
  combo = True
  doSelect()
  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      break

    doAura()
    try:
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgAttackBoss)
      doAttack()
      time.sleep(0.1)
      doAttack()
      time.sleep(0.1)
    except pyauto.ImageNotFoundException:
      logAction(msgBossKilled)
      combo = False
      break

def pathFind(unit):
  pathing = True
  boss = 0
  while pathing:
    if not macro:
      logAction(msgTerminate)
      pathing = False
      sys.exit()
      break

    logAction(msgPathFind + unit)

    if unit == unitMossToad:
      try:
        vineblock = pyauto.locateOnScreen(imgVine1, grayscale=False, confidence=.9)
      except pyauto.ImageNotFoundException:
        logAction(msgNoVineFound)
      else:
        pathBackTrack(unitMossToad)

      try:
        vineblock = pyauto.locateOnScreen(imgVine2, grayscale=False, confidence=.9)
      except pyauto.ImageNotFoundException:
        logAction(msgNoVineFound)
      else:
        pathBackTrack(unitMossToad)
    
    try:
      pyauto.moveTo(cabalwindow[0] + 600, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 600, cabalwindow[1] + 260)
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect()
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 500, cabalwindow[1] + 260)
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      doDash()
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)
    
    try:
      doSelect()
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 400, cabalwindow[1] + 260)
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      doDash()
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect()
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 300, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 300, cabalwindow[1] + 260)
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      doDash()
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect()
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 200, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 200, cabalwindow[1] + 260)
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      doDash()
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect()
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    if unit == unitLumberMoth:
      try:
        pyauto.moveTo(cabalwindow[0] + 200, cabalwindow[1] + 460)
        pyauto.click(cabalwindow[0] + 200, cabalwindow[1] + 460)
        doSelect()
        mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
        doDash()
        logAction(msgMobsFound + unit)
        pathing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)

      try:
        doSelect()
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        logAction(msgBossFound)
        pathing = False
        boss = 1
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)

  if boss == 0:
    attackMobs(unit)

def pathBackTrack(unit):
  pathing = True
  boss = 0
  while pathing:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break

    logAction(msgBackTrack + unit)
    try:
      pyauto.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 650, cabalwindow[1] + 560)
      doDash()
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 700, cabalwindow[1] + 560)
      doDash()
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 750, cabalwindow[1] + 560)
      doDash()
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 800, cabalwindow[1] + 560)
      doDash()
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 850, cabalwindow[1] + 560)
      doDash()
      doSelect()
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

  attackMobs(unit)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    # MAIN
    shortcut.add_hotkey("esc", terminate)
    logAction(msgStartDg)

    pynboard.press(Key.f3)
    pynboard.release(Key.f3)

    global cabalwindow
    cabalwindow = pyauto.locateOnScreen(imgCabalWindow, grayscale=False, confidence=.5)
    pyauto.moveTo(cabalwindow[0] + 50, cabalwindow[1] + 15)
    pyauto.click(cabalwindow[0] + 50, cabalwindow[1] + 15)

    # AHV
    # AHV ENTER FREE VIEW
    pyauto.moveTo(cabalwindow[0] + 677, cabalwindow[1] + 361)
    pyauto.moveTo(cabalwindow[0] + 690, cabalwindow[1] + 361)
    time.sleep(1)
    
    pyauto.click(cabalwindow[0] + 690, cabalwindow[1] + 361)
    time.sleep(1)

    enterdg = pyauto.locateOnScreen(imgEnterDg, grayscale=False, confidence=.9)
    pyauto.moveTo(enterdg[0] + 15, enterdg[1] + 15)
    pyauto.click(enterdg[0] + 15, enterdg[1] + 15)
    time.sleep(2)

    challengedg = pyauto.locateOnScreen(imgChallengeDg, grayscale=False, confidence=.9)
    pyauto.moveTo(challengedg[0] + 15, challengedg[1] + 15)
    pyauto.click(challengedg[0] + 15, challengedg[1] + 15)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 150)
    pyauto.mouseDown(button="right")
    pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 600)
    pynboard.press(dash)
    pynboard.release(dash)
    time.sleep(1)

    # Mush and Flower Sequence
    moving = True
    while moving:
      if not macro:
          logAction(msgTerminate)
          moving = False
          sys.exit()
          break

      pathFind(unitMushFlower)
      try:
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        moving = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)

    pyauto.moveTo(cabalwindow[0] +  850, cabalwindow[1] + 600)
    pynboard.press(dash)
    pynboard.release(dash)

    # First Boss
    doHardBuffs()
    attackBoss()
    lootBox()

    # Mossites and Toad Sequence
    moving = True
    while moving:
      pathFind(unitMossToad)
      try:
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        moving = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)

    # Second Boss
    attackBoss()
    lootBox()

    # Lumber and Moth Sequence
    moving = True
    while moving:
      if not macro:
          logAction(msgTerminate)
          moving = False
          sys.exit()
          break

      pathFind(unitLumberMoth)
      try:
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        moving = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)

    pyauto.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 550, cabalwindow[1] + 260)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 450, cabalwindow[1] + 260)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 350, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 350, cabalwindow[1] + 260)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 250, cabalwindow[1] + 260)
    time.sleep(1)

    pyauto.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 660)
    pyauto.click(cabalwindow[0] + 250, cabalwindow[1] + 660)

    time.sleep(1)

    # First Orphidia
    try:
      doSelect
      mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.8)
      attackBoss()
    except pyauto.ImageNotFoundException:
      logAction(msgNoBossFound)
    
    time.sleep(1)
    pyauto.moveTo(cabalwindow[0] + 675, cabalwindow[1] + 600)
    pyauto.moveTo(cabalwindow[0] + 675, cabalwindow[1] + 600)
    time.sleep(0.2)

    doDash()
    time.sleep(0.2)

    # Second and Third Orphidia
    bossCount = 0
    while bossCount < 2:
      if not macro:
          logAction(msgTerminate)
          moving = False
          sys.exit()
          break
      
      if (bossCount == 1):
        doHardBuffs()
    
      try:
        doSelect()
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.8)
        bossCount += 1
        attackBoss()
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)
    
    # Pathfind Treasure Boxes
    boxing = True
    while boxing:
      pyauto.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 550, cabalwindow[1] + 160)
      time.sleep(0.5)

      pyauto.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 650, cabalwindow[1] + 160)
      time.sleep(0.5)

      pyauto.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 750, cabalwindow[1] + 160)
      time.sleep(0.5)

      pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 850, cabalwindow[1] + 160)
      time.sleep(0.5)

      pyauto.moveTo(cabalwindow[0] + 950, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 950, cabalwindow[1] + 160)
      time.sleep(0.5)

      pyauto.moveTo(cabalwindow[0] + 950, cabalwindow[1] + 360)
      pyauto.click(cabalwindow[0] + 950, cabalwindow[1] + 360)

      doDash()
      time.sleep(0.5)

      doFade()
      time.sleep(0.5)

      try:
        doSelect()
        mobs = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9)
        logAction(msgBoxFound)
        boxing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBoxFound)

    time.sleep(2)

    # Loot Treasure Boxes
    lootBox()
    time.sleep(0.5)

    lootBox()
    time.sleep(0.5)

    lootBox()
    time.sleep(0.5)

    cancelAura()

    # Start to End Dungeon
    enddungeon = pyauto.locateOnScreen(imgEndDg, grayscale=False, confidence=.9)
    pyauto.moveTo(enddungeon[0] + 50, enddungeon[1] + 15)
    pyauto.click(enddungeon[0] + 50, enddungeon[1] + 15)

    rolladice = pyauto.locateOnScreen(imgDiceRoll, grayscale=False, confidence=.9)
    pyauto.moveTo(rolladice[0] + 50, rolladice[1] + 15)
    pyauto.click(rolladice[0] + 50, rolladice[1] + 15)

    time.sleep(1)
    pyauto.click(rolladice[0] + 50, rolladice[1] + 15)

    runCounter += 1
    logAction(msgEndDg)
    time.sleep(3)
