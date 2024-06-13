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
deselect = Key.esc
lootSpace = Key.space

# GLOBAL VALIDATION
cabalwindow = []
rootFrame = []
runNumberLbl = []
macroLbl = []
startButton = []
combo = True
pathing = True
moving = True
boxing = True
macro = True
isBattleMode = False
battleMode = 0
buffsAllowed = 1
shortBuffsAllowed = 1

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
msgCheckBoss = "Checking Boss"
msgBoxFound = "Box Found"
msgNoBoxFound = "No Box Found"
msgPathStop = "Pathing stop, attacking"
msgCheckEndDg = "Check End Dungeon"
msgAction = ""
msgRunNumber =  "Run #: "
msgBackTrack = "Backtrack #: "
msgChallengeDungeon = "Challenge Dungeon"
msgEnterDungeon = "Enter Dungeon"
msgNoButtonFound = "No Button Found"
msgBuffs = "Buffing"
msgShortBuffs = "Buffing Shorts"
msgBattleModeTwo = "Doing Mode 2"
msgDiceRoll = "Check Dice Roll"

# GLOBAL PICTURES
imgCabalWindow = "img/cabalwindow.jpg"
imgChallengeDg = "img/challengedg.jpg"
imgDungeon = "img/dungeon.jpg"
imgEnterDg = "img/enterdg.jpg"
imgEndDg = "img/enddg.jpg"
imgExitDg = "img/exitdg.jpg"
imgDualBoss = "img/dualboss.jpg"
imgBoss = "img/boss.jpg"
imgSemiBoss = "img/semiboss.jpg"
imgMobs = "img/mobs.jpg"
imgDiceRoll = "img/rolladice.jpg"
imgBox = "img/box.jpg"
imgWarp = "img/warp.jpg"
imgVine1 = "img/vineblock1.jpg"
imgVine2 = "img/vineblock2.jpg"

# GLOBAL UNITS
unitMushFlower = "Mushed and Ectoflower"
unitMossToad = "Mossites and Toad"
unitLumberMoth = "Lumber and Moth"
unitBox = "Box"

def initialize(frame, btn, mlbl, rlbl, mode=0, buff=1, sbuffs=1, runs=1):
  global rootFrame
  rootFrame = frame

  global startButton
  startButton = btn
  
  global macroLbl
  macroLbl = mlbl

  global runNumberLbl
  runNumberLbl = rlbl 

  global battleMode
  battleMode = int(mode)

  global isBattleMode
  isBattleMode = False

  global buffsAllowed
  buffsAllowed = int(buff)

  global shortBuffsAllowed
  shortBuffsAllowed = int(sbuffs)
  
  startButton.config(state="disabled")
  rootFrame.update()
  runDungeon(int(runs))
  startButton.config(state="active")
  rootFrame.update()

def logRun(runNumber):
  runBuilder = StringVar()
  runBuilder = msgRunNumber + str(runNumber)
  print(runBuilder)
  runNumberLbl.config(text=runBuilder)
  rootFrame.update()

def logAction(message):
  msgBuilder = StringVar()
  msgBuilder = msgAction + message
  print(msgBuilder)
  macroLbl.config(text=msgBuilder)
  rootFrame.update()

def terminate():
  logAction(msgExit)
  global macro
  macro = False

def goSkillSlot():
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

def doBattleMode():
  logAction(msgBattleModeTwo)
  cancelAura()
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 790, cabalwindow[1] + 670)
  pyauto.click(button="right")

  global isBattleMode
  isBattleMode = True
  time.sleep(5)

def doContBattleMode():
  pyauto.moveTo(cabalwindow[0] + 790, cabalwindow[1] + 670)
  pyauto.click(button="right")

def doBuffs():
  logAction(msgBuffs)
  pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 670)
  pyauto.click(button="right")
  time.sleep(0.5)

  pyauto.moveTo(cabalwindow[0] + 430, cabalwindow[1] + 670)
  pyauto.click(button="right")

def doShortBuffs():
  logAction(msgShortBuffs)
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
  pyauto.click(button="right")
  time.sleep(0.5)

def cancelAura():
  pyauto.moveTo(cabalwindow[0] + 175, cabalwindow[1] + 100)
  pyauto.click(button="right")

def doDash(sec=0):
  pynboard.press(dash)
  pynboard.release(dash)
  
  if (sec != 0):
    time.sleep(sec)

def doFade(sec=0):
  pynboard.press(fade)
  pynboard.release(fade)
  
  if (sec != 0):
    time.sleep(sec)

def doSelect(sec=0):
  pynboard.press(select)
  pynboard.release(select)

  if (sec != 0):
    time.sleep(sec)

def doDeselect(sec=0):
  pynboard.press(deselect)
  pynboard.release(deselect)

  if (sec != 0):
    time.sleep(sec)

def doDeselectPack():
  doDeselect()
  doDeselect(0.1)
  doDeselect(0.1)

def lootBox():
  doSelect(0.1)
  doSelect(0.1)
  checkBox = True
  while checkBox:
    try:
      doSelect(0.1)
      box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9)
      logAction(msgBoxFound)
      checkBox = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoBoxFound)

  if isBattleMode:
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    autoEssentials()
  else:
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

def finalLootBox():
  doSelect(0.1)
  doSelect(0.1)
  checkBox = True
  while checkBox:
    try:
      doSelect(0.1)
      box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9)
      logAction(msgBoxFound)
      checkBox = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoBoxFound)

  if isBattleMode:
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    lootEssentials()
  else:
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

def lootEssentials():
  pynboard.press(lootSpace)
  pynboard.release(lootSpace)
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
  if isBattleMode:
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    autoEssentials()
    doContBattleMode()
  else:
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
  fadeCount = 0

  doDeselectPack()
  doSelect(0.1)
  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break
    
    try:
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      doDeselect()
      logAction(msgBossFound)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgAttackMobs + unit)

    doAura()
    try:
      doSelect(0.1)

      if (fadeCount == 20):
        fadeCount = 0
        pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 440)
        pyauto.click(cabalwindow[0] + 700, cabalwindow[1] + 440)
        time.sleep(0.2)
        doFade(0.1)
      else:
        fadeCount += 1

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
  doSelect(0.1)
  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      break

    if isBattleMode == False:
      doAura()

    try:
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
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
  backTrackCheck = 0
  while pathing:
    if not macro:
      logAction(msgTerminate)
      pathing = False
      sys.exit()
      break

    logAction(msgPathFind + unit)

    backTrackCheck += 1
    pyauto.moveTo(cabalwindow[0] + 675, cabalwindow[1] + 450)
    pyauto.click(cabalwindow[0] + 675, cabalwindow[1] + 450)
    print(msgBackTrack + str(backTrackCheck))
    if (backTrackCheck >= 10):
      backTrackCheck = 0
      pathBackTrack(unit)
    
    try:
      pyauto.moveTo(cabalwindow[0] + 600, cabalwindow[1] + 260)
      pyauto.click(cabalwindow[0] + 600, cabalwindow[1] + 260)
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect(0.1)
      logAction(msgCheckBoss)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
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
      time.sleep(0.5)
      doDash(0.5)
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)
    
    try:
      doSelect(0.1)
      logAction(msgCheckBoss)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    if unit == unitMossToad:
      try:
        pyauto.moveTo(cabalwindow[0] + 475, cabalwindow[1] + 260)
        pyauto.click(cabalwindow[0] + 475, cabalwindow[1] + 260)
        doFade()
        doSelect(0.1)
        mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
        logAction(msgMobsFound + unit)
        pathing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)
      
      try:
        doSelect(0.1)
        logAction(msgCheckBoss)
        boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        logAction(msgBossFound)
        pathing = False
        boss = 1
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)

      try:
        pyauto.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 260)
        pyauto.click(cabalwindow[0] + 450, cabalwindow[1] + 260)
        doFade()
        doSelect(0.1)
        mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
        logAction(msgMobsFound + unit)
        pathing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)
      
      try:
        doSelect(0.1)
        logAction(msgCheckBoss)
        boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
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
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect(0.1)
      logAction(msgCheckBoss)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
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
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect(0.1)
      logAction(msgCheckBoss)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
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
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      pathing = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      doSelect(0.1)
      logAction(msgCheckBoss)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      logAction(msgBossFound)
      pathing = False
      boss = 1
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    if unit == unitLumberMoth:
      try:
        pyauto.moveTo(cabalwindow[0] + 200, cabalwindow[1] + 360)
        pyauto.click(cabalwindow[0] + 200, cabalwindow[1] + 360)
        doSelect(0.1)
        mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
        logAction(msgMobsFound + unit)
        pathing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoMobsFound)

      try:
        doSelect(0.1)
        logAction(msgCheckBoss)
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
  backtracking = True
  boss = 0
  backTrackCancel = 0
  while backtracking:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break

    backTrackCancel += 1
    print(msgBackTrack + str(backTrackCancel))
    if (backTrackCancel >= 10):
      backTrackCancel = 0
      backtracking = False

    logAction(msgBackTrack + unit)
    try:
      pyauto.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 650, cabalwindow[1] + 560)
      doDash()
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      backtracking = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 700, cabalwindow[1] + 560)
      doDash()
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      backtracking = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 750, cabalwindow[1] + 560)
      doDash()
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      backtracking = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 800, cabalwindow[1] + 560)
      doDash()
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      backtracking = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

    try:
      pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 560)
      pyauto.click(cabalwindow[0] + 850, cabalwindow[1] + 560)
      doDash()
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9)
      logAction(msgMobsFound + unit)
      backtracking = False
      logAction(msgPathStop)
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoMobsFound)

  attackMobs(unit)

def runDungeon(runs=1):
  runCounter = 0
  while runCounter < runs:
    shortcut.add_hotkey("ctrl+r", terminate)
    logAction(msgStartDg)
    logRun(runCounter + 1)

    global cabalwindow
    cabalwindow = pyauto.locateOnScreen(imgCabalWindow, grayscale=False, confidence=.9)
    pyauto.moveTo(cabalwindow[0] + 50, cabalwindow[1] + 15)
    pyauto.click(cabalwindow[0] + 50, cabalwindow[1] + 15)

    pyauto.moveTo(cabalwindow[0] + 677, cabalwindow[1] + 361)
    pyauto.moveTo(cabalwindow[0] + 735, cabalwindow[1] + 361)
    time.sleep(0.5)

    pyauto.click(cabalwindow[0] + 735, cabalwindow[1] + 361)
    time.sleep(0.5)

    isEntering = True
    while isEntering:
      try:
        enterdg = pyauto.locateOnScreen(imgEnterDg, grayscale=False, confidence=.9)
        pyauto.moveTo(enterdg[0] + 15, enterdg[1] + 15)
        pyauto.click(enterdg[0] + 15, enterdg[1] + 15)
        time.sleep(2)
        isEntering = False
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoButtonFound)

    isChallenging = True
    while isChallenging:
      try:
        challengedg = pyauto.locateOnScreen(imgChallengeDg, grayscale=False, confidence=.9)
        pyauto.moveTo(challengedg[0] + 15, challengedg[1] + 15)
        pyauto.click(challengedg[0] + 15, challengedg[1] + 15)
        time.sleep(1)
        isChallenging = False
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoButtonFound)

    pyauto.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 150)
    pyauto.mouseDown(button="right")
    pyauto.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 150)
    pyauto.mouseUp(button="right")
    pyauto.scroll(-10000)

    goSkillSlot()
    time.sleep(0.5)

    if buffsAllowed == 1:
      doBuffs()

    # Initial Position
    pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 600)
    doDash(0.1)

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

    doDeselectPack()
    pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 600)
    doDash(0.1)

    # First Boss
    if shortBuffsAllowed == 1:
      doShortBuffs()

    attackBoss()
    pyauto.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 450)
    doFade(0.5)
    lootBox()

    pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 400, cabalwindow[1] + 260)
    doDash(0.5)

    # Mossites and Toad Sequence
    moving = True
    while moving:
      pathFind(unitMossToad)
      try:
        boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        moving = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)

    # Second Boss
    doDeselectPack()
    pyauto.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 360)
    doDash(1)
    pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 300)
    doFade(0.1)

    secondBoss = True
    while secondBoss:
      try:
        doSelect(0.1)
        mobs = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        secondBoss = False
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)
    
    attackBoss()
    doDeselectPack()
    pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 100)
    doFade(0.5)
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

    doDeselectPack()
    pyauto.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 260)
    doDash(0.5)

    pyauto.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 260)
    pyauto.click(cabalwindow[0] + 500, cabalwindow[1] + 260)

    pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 320)
    pyauto.click(cabalwindow[0] + 400, cabalwindow[1] + 320)
    doDash(1)
    doDash(1)
    doFade(0.1)

    pyauto.moveTo(cabalwindow[0] + 320, cabalwindow[1] + 540)
    doDeselectPack()
    doDash(0.5)

    pyauto.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 400)
    doFade(0.5)

    # First Orphidia
    try:
      doSelect(0.1)
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
      attackBoss()
    except pyauto.ImageNotFoundException:
      logAction(msgNoBossFound)

    pyauto.moveTo(cabalwindow[0] + 675, cabalwindow[1] + 600)
    doDash(0.5)

    if battleMode == 1:
      doBattleMode()

    # Second and Third Orphidia
    bossCount = 0
    shortBuffsCounter = 0
    while bossCount < 2:
      if not macro:
          logAction(msgTerminate)
          moving = False
          sys.exit()
          break
      
      if (bossCount == 1 and shortBuffsCounter == 0 and shortBuffsAllowed == 1):
        shortBuffsCounter = 1
        doShortBuffs()

      try:
        doSelect(0.1)
        boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9)
        bossCount += 1
        attackBoss()
        doDeselectPack()
        if (bossCount == 1):
          time.sleep(5)
      except pyauto.ImageNotFoundException:
        logAction(msgNoBossFound)
    
    # Pathfind Treasure Boxes
    boxing = True
    while boxing:
      if not macro:
          logAction(msgTerminate)
          boxing = False
          sys.exit()
          break

      logAction(msgPathFind + unitBox)
      pyauto.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 550, cabalwindow[1] + 160)
      time.sleep(1)

      doDash(0.5)
      pyauto.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 650, cabalwindow[1] + 160)
      time.sleep(0.3)

      pyauto.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 750, cabalwindow[1] + 160)
      time.sleep(0.3)

      pyauto.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 850, cabalwindow[1] + 160)
      time.sleep(0.3)

      pyauto.moveTo(cabalwindow[0] + 950, cabalwindow[1] + 160)
      pyauto.click(cabalwindow[0] + 950, cabalwindow[1] + 160)
      time.sleep(0.3)

      pyauto.moveTo(cabalwindow[0] + 950, cabalwindow[1] + 480)
      pyauto.click(cabalwindow[0] + 950, cabalwindow[1] + 480)

      doDash(1)
      doFade(0.5)

      try:
        doSelect(0.1)
        box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9)
        logAction(msgBoxFound)
        boxing = False
        logAction(msgPathStop)
        break
      except pyauto.ImageNotFoundException:
        logAction(msgNoBoxFound)

    # Loot Treasure Boxes
    boxCounter = 0
    while boxCounter < 10:
      if not macro:
          logAction(msgTerminate)
          boxCounter = False
          sys.exit()
          break

      try:
        doSelect(0.1)
        boxCounter += 1
        box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9)
        logAction(msgBoxFound)
        logAction(msgPathStop)
        boxCounter += 2
        finalLootBox()
      except pyauto.ImageNotFoundException:
        logAction(msgNoBoxFound)

      try:
        checkenddg = pyauto.locateOnScreen(imgEndDg, grayscale=False, confidence=.9)
        boxCounter += 10
        break
      except pyauto.ImageNotFoundException:
        logAction(msgCheckEndDg)

    global isBattleMode
    isBattleMode = False
    cancelAura()
    time.sleep(3)
  
    # Start to End Dungeon
    isEnding = True
    endCheckTrack = 0
    while isEnding:
      if not macro:
          logAction(msgTerminate)
          isEnding = False
          sys.exit()
          break

      endCheckTrack += 1
      if (endCheckTrack >= 60):
        isEnding = False
        break

      try:
        enddungeon = pyauto.locateOnScreen(imgEndDg, grayscale=False, confidence=.9)
        pyauto.moveTo(enddungeon[0] + 50, enddungeon[1] + 15)
        pyauto.click(enddungeon[0] + 50, enddungeon[1] + 15)
        time.sleep(0.5)
        isEnding = False
        break
      except pyauto.ImageNotFoundException:
        logAction(msgCheckEndDg)
    
    isDicing = True
    while isDicing:
      if not macro:
          logAction(msgTerminate)
          isDicing = False
          sys.exit()
          break

      try:
        rolladice = pyauto.locateOnScreen(imgDiceRoll, grayscale=False, confidence=.9)
        pyauto.moveTo(rolladice[0] + 50, rolladice[1] + 15)
        pyauto.click(rolladice[0] + 50, rolladice[1] + 15)
        time.sleep(0.8)
        pyauto.click(rolladice[0] + 50, rolladice[1] + 15)
        isDicing = False
        break
      except pyauto.ImageNotFoundException:
        logAction(msgDiceRoll)

    runCounter += 1
    logAction(msgEndDg)
    time.sleep(3)
