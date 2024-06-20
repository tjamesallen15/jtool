import time
import sys
from tkinter import *
import pyautogui as pyauto
import pyscreeze
import keyboard as shortcut

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard

pynboard = Controller()

# GLOBAL VARIABLES
select = 'z'
dash = '1'
fade = '2'
attack = ['3', '4', '5']
veradrix = '6'
loot = '7'
fury = '8'
pots = '9'
bmaura = '0'
bm3atk = '-'
bm3 = '='
deselect = Key.esc
lootSpace = Key.space

# GLOBAL VARIABLES
cabalwindow = []
rootFrame = []
runNumberLbl = []
macroLbl = []
macro = True
isBattleMode = False
battleMode = 0
buffsAllowed = 1
shortBuffsAllowed = 1
useVeradrix = 0
auraCounter = 0
atkType = 0
difficulty = "Hazardous Valley (Easy)"
dungeonList = [
  "Hazardous Valley (Hard)",
  "Hazardous Valley (Medium)",
  "Hazardous Valley (Easy)"
]
hpBar = []
hpBarMode = []

# GLOBAL MESSAGES
msgStartDg = "Starting Dungeon"
msgEndDg = "End Dungeon"
msgExit = "Macro Exit"
msgTerminate ="Macro Terminate"
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
msgMoveStop = "Moving stop, proceeding"
msgCheckEndDg = "Check End Dungeon"
msgAction = ""
msgRunNumber =  "Run #: "
msgBackTrack = "Backtrack #: "
msgChallengeDungeon = "Challenge Dungeon"
msgEnterDungeon = "Enter Dungeon"
msgNoButtonFound = "No Button Found"
msgBuffs = "Buffing"
msgShortBuffs = "Buffing Shorts"
msgBattleModeTwo = "Doing Mode II"
msgDiceRoll = "Check Dice Roll"
msgDiceRollOkay = "Check Dice Roll Okay"
msgCheckDialogFound =  "Check Dialog Found"
msgNoCheckDialogFound = "No Check Dialog Found"
msgGateFound = "Gate Found "
msgNoGateFound = "No Gate Found"

# GLOBAL IMAGES
imgAppIcon = "img/icon.png"
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
imgDiceOkay = "img/diceokay.jpg"
imgCheckDialog = "img/checkdialog.jpg"
imgBox = "img/box.jpg"
imgGate = "img/gate.jpg"
imgHolyBox = "img/holybox.jpg"

# GLOBAL UNITS
unitBlank = "--"
unitMushFlower = "Mushed and Ectoflower"
unitMossToad = "Mossite and Toad"
unitLumberMoth = "Lumber and Moth"
unitCutterToad = "Moscutter and Toad"
unitBoarSnake = "Boars and Snake"
unitWhiteSnake = "White Snake"
unitOrphidia = "Orphidia"
unitMechape = "Mechape"
unitArmun = "Armun"
unitTricus = "Tricus"
unitGateOne = "Gate One"
unitGateTwo = "Gate Two"
unitGateThree = "Gate Three"
unitGateFour = "Gate Four"
unitLegrin = "Legrin of Wind"
unitLeo = "Leo of Wind"
unitEspi = "Espi of Wind"
unitDraco = "Draco of Wind"
unitSpector = "Spector"
unitDarkArcher = "Dark Archer"
unitJason = "Gatekeeper Jason"
unitLavaGate = "Lava Gate"
unitMechLion = "Mech Lion"
unitLihonar = "Lihonar"
unitEspada = "Espada"
unitEspadaII = "Espada II"
unitEspadaIII = "Espada III"
unitPoerte = "Poerte"
unitRedonno = "Redonno"
unitPowerSupply = "Power Supply"
unitShoworaiFear = "Showorai's Fear"
unitShoworaiResignation = "Showorai's Resignation"
unitShoworaiMadness = "Showorai's Madness"
unitBox = "Box"

def initialize(window, frame, mlbl, rlbl):
  global cabalwindow
  cabalwindow = window

  global rootFrame
  rootFrame = frame
  
  global macroLbl
  macroLbl = mlbl

  global runNumberLbl
  runNumberLbl = rlbl

  global hpBar
  hpBar = (int(cabalwindow[0] + 475), int(cabalwindow[1] + 25), 45, 30)

  global hpBarMode
  hpBarMode = (int(cabalwindow[0] + 350), int(cabalwindow[1] + 25), 325, 30)


def setVariables(mode=0, buff=1, sbuffs=1, atk=0, vera=0):
  global battleMode
  battleMode = int(mode)

  global isBattleMode
  isBattleMode = False

  global buffsAllowed
  buffsAllowed = int(buff)

  global shortBuffsAllowed
  shortBuffsAllowed = int(sbuffs)

  global atkType
  atkType = int(atk)

  global useVeradrix
  useVeradrix = vera

def setCabalWindow(window):
  global cabalwindow
  cabalwindow = window

def goCabalWindow():
  moveClick(50, 15)

def move(x, y, sec=0):
  pyauto.moveTo(cabalwindow[0] + x, cabalwindow[1] + y)

  if (sec != 0):
    time.sleep(sec)

def moveRel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)

  if (sec != 0):
    time.sleep(sec)

def moveClick(x, y, sec=0):
  pyauto.moveTo(cabalwindow[0] + x, cabalwindow[1] + y)
  pyauto.click(cabalwindow[0] + x, cabalwindow[1] + y)

  if (sec != 0):
    time.sleep(sec)

def moveClickRel(x, y, ref, sec=0):
  pyauto.moveTo(ref[0] + x, ref[1] + y)
  pyauto.click(ref[0] + x, ref[1] + y)

  if (sec != 0):
    time.sleep(sec)

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

def getHpBar():
  if isBattleMode and atkType == 1:
    return hpBarMode
  else:
    return hpBar

def terminate():
  logAction(msgExit)
  global macro
  macro = False

def forceExitDungeon():
  moveClick(830, 710)
  moveClick(850, 430)
  moveClick(1030, 485)
  moveClick(620, 440)

  time.sleep(1)

def goSkillSlot(sec=0):
  pynboard.press(Key.f3)
  pynboard.release(Key.f3)

  if (sec != 0):
    time.sleep(sec)

def setBattleMode(val):
  cancelAura(1)
  if battleMode == 1:
    global isBattleMode
    isBattleMode = val

def doBattleMode():
  if battleMode == 1:
    logAction(msgBattleModeTwo)
    cancelAura(1)

    move(790, 670)
    pyauto.click(button="right")

    move(790, 670)
    pyauto.click(button="right")

    global isBattleMode
    isBattleMode = True
    time.sleep(5)

    pynboard.press(bmaura)
    pynboard.release(bmaura)
    time.sleep(1)

def doVeradrix():
  if useVeradrix == 1:
    pynboard.press(veradrix)
    pynboard.release(veradrix)

def doContBattleMode():
  move(790, 670)
  pyauto.click(button="right")

  doVeradrix()
  global auraCounter
  auraCounter += 1
  if auraCounter > 45:
    doAuraStrict()
    auraCounter = 0

def doBuffs():
  if buffsAllowed == 1:
    logAction(msgBuffs)
    move(400, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(430, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

def doShortBuffs():
  if shortBuffsAllowed == 1:
    logAction(msgShortBuffs)
    move(470, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(540, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(570, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

def forceShortBuffs():
    logAction(msgShortBuffs)
    move(470, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(500, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(540, 670)
    pyauto.click(button="right")
    time.sleep(0.5)

    move(570, 670)
    pyauto.click(button="right")
    time.sleep(0.5)    

def cancelAura(sec=0):
  move(175, 100)
  pyauto.click(button="right")

  if (sec != 0):
    time.sleep(sec)

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

def doLoot():
  doSelect(0.1)
  doSelect(0.1)
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
    time.sleep(0.3)
    pynboard.press(lootSpace)
    pynboard.release(lootSpace)
    time.sleep(0.3)

def lootBox(sec=3, select=1):
  checking = True
  boxCounter = 0
  while checking:
    if not macro:
      logAction(msgTerminate)
      checking = False
      sys.exit()
      break

    try:
      if select == 1:
        doSelect(0.1)
      box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgBoxFound)
    except pyauto.ImageNotFoundException:
      logAction(msgNoBoxFound)

    doLoot()
    boxCounter += 1
    if boxCounter > sec:
      boxCounter = 0
      break

def finalLootBox(sec=4):
  checking = True
  boxCounter = 0
  while checking:
    if not macro:
      logAction(msgTerminate)
      checking = False
      sys.exit()
      break

    try:
      doSelect(0.1)
      box = pyauto.locateOnScreen(imgBox, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgBoxFound)
    except pyauto.ImageNotFoundException:
      logAction(msgNoBoxFound)

    doLoot()
    boxCounter += 1
    if boxCounter > sec:
      boxCounter = 0
      break

def autoEssentials():
  pynboard.press(lootSpace)
  pynboard.release(lootSpace)
  pynboard.press(fury)
  pynboard.release(fury)
  pynboard.press(pots)
  pynboard.release(pots)
  pynboard.press(loot)
  pynboard.release(loot)

  doVeradrix()

  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

def lootEssentials():
  pynboard.press(lootSpace)
  pynboard.release(lootSpace)
  pynboard.press(pots)
  pynboard.release(pots)
  pynboard.press(loot)
  pynboard.release(loot)

  doVeradrix()

  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

def releaseKeys(sec=0):
  pynboard.release(Key.shift)
  pynboard.release(Key.alt)
  pynboard.release(Key.ctrl)

  if (sec != 0):
    time.sleep(sec)

def doAura(sec=0):
  pynboard.press(bm3)
  pynboard.release(bm3)
  autoEssentials()
  pynboard.press(bmaura)
  pynboard.release(bmaura)
  autoEssentials()
  pynboard.press(bm3)
  pynboard.release(bm3)

  if (sec != 0):
    time.sleep(sec)

def doAuraStrict(sec=0):
  pynboard.press(bmaura)
  pynboard.release(bmaura)
  pynboard.press(bmaura)
  pynboard.release(bmaura)

  if (sec != 0):
    time.sleep(sec)

def doAttack(sec=0):
  doVeradrix()

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

  if (sec != 0):
    time.sleep(sec)

def doAttackStrict(sec=0):
  if isBattleMode:
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
  else:
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    pynboard.press(bm3atk)
    pynboard.release(bm3atk)
    pynboard.press(attack[0])
    pynboard.release(attack[0])
    pynboard.press(attack[1])
    pynboard.release(attack[1])
    pynboard.press(attack[2])
    pynboard.release(attack[2])

  if (sec != 0):
    time.sleep(sec)

def enterDungeon():
  entering = True
  while entering:
    if not macro:
      logAction(msgTerminate)
      entering = False
      sys.exit()
      break

    try:
      enterdg = pyauto.locateOnScreen(imgEnterDg, grayscale=False, confidence=.9)
      moveClickRel(15, 15, enterdg, 1)
      entering = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoButtonFound)

def challengeDungeon():
  challenging = True
  while challenging:
    if not macro:
      logAction(msgTerminate)
      challenging = False
      sys.exit()
      break

    try:
      challengedg = pyauto.locateOnScreen(imgChallengeDg, grayscale=False, confidence=.9)
      moveClickRel(15, 15, challengedg, 1)
      challenging = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgNoButtonFound)

def endDungeon():
  ending = True
  endCheckTrack = 0
  while ending:
    if not macro:
      logAction(util.msgTerminate)
      ending = False
      sys.exit()
      break

    if ending == False:
      break

    endCheckTrack += 1
    if (endCheckTrack >= 60):
      ending = False
      break

    try:
      enddungeon = pyauto.locateOnScreen(imgEndDg, grayscale=False, confidence=.9)
      moveClickRel(50, 15, enddungeon, 0.5)
      ending = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgCheckEndDg)

def diceDungeon():
  dicing = True
  while dicing:
    if not macro:
      logAction(msgTerminate)
      dicing = False
      sys.exit()
      break

    try:
      rolladice = pyauto.locateOnScreen(imgDiceRoll, grayscale=False, confidence=.9)
      moveClickRel(50, 15, rolladice, 0.8)
      # moveClickRel(50, 15, rolladice)
      dicing = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgDiceRoll)

  confirming = True
  while confirming:
    if not macro:
      logAction(msgTerminate)
      confirming = False
      sys.exit()
      break

    try:
      diceconfirm = pyauto.locateOnScreen(imgDiceOkay, grayscale=False, confidence=.9)
      # moveClickRel(10, 15, rolladice, 0.8)
      moveClickRel(10, 5, diceconfirm)
      confirming = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgDiceRollOkay)

def focusGate(unit=unitBlank, select=1):
  combo = True
  fadeCount = 0

  if select == 1:
    doSelect(0.1)

  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break

    if combo == False:
      break

    try:
      if select == 1:
        doSelect(0.1)
      gate = pyauto.locateOnScreen(imgGate, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackMobs + unit)

      doAttack(0.3)
      doAttack(0.3)
    except pyauto.ImageNotFoundException:
      combo = False
      logAction(msgMobsCleared)
      break

def focusMobs(unit=unitBlank, aura=1, select=1, sidestep=1):
  combo = True
  fadeCount = 0

  if select == 1:
    doSelect(0.1)

  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      sys.exit()
      break

    if aura == 1:
      doAura()
    
    if sidestep == 1:
      if (fadeCount == 20):
        fadeCount = 0
        moveClick(700, 440, 0.2)
        doFade(0.1)
      else:
        fadeCount += 1

    try:
      if select == 1:
        doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackMobs + unit)

      doAttack(0.1)
      doAttack(0.1)

      if select == 1:
        doDeselectPack()
    except pyauto.ImageNotFoundException:
      logAction(msgMobsCleared)
      combo = False
      break

def attackMobs(unit=unitBlank, aura=1, interval=0.3, sidestep=1):
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
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9, region=getHpBar())
      doDeselect()
      logAction(msgBossFound)
      combo = False
      break
    except pyauto.ImageNotFoundException:
      logAction(msgAttackMobs + unit)

    if aura == 1:
      doAura()
    
    if sidestep == 1:
      if (fadeCount == 20):
        fadeCount = 0
        moveClick(700, 440, 0.2)
        doFade(0.1)
      else:
        fadeCount += 1

    try:
      doSelect(0.1)
      mobs = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackMobs + unit)

      if interval > 0.3:
        doAttack(interval)
        doAttackStrict(0.3)
        doAttack(interval)
        doAttackStrict(0.3)
      else:
        doAttack(interval)
        doAttack(interval)
  
    except pyauto.ImageNotFoundException:
      logAction(msgMobsCleared)
      combo = False
      break

def attackBoss(select=1, aura=1):
  combo = True

  if select == 1:
    doSelect(0.1)

  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      break

    if isBattleMode == False:
      if aura == 1:
        doAura()

    try:
      boss = pyauto.locateOnScreen(imgBoss, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackBoss)
      doAttack(0.1)
      doAttack(0.1)
    except pyauto.ImageNotFoundException:
      logAction(msgBossKilled)
      combo = False
      break

def attackSemiBoss(select=1):
  combo = True
  
  if select == 1:
    doSelect(0.1)

  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      break

    if isBattleMode == False:
      doAura()

    try:
      boss = pyauto.locateOnScreen(imgSemiBoss, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackBoss)
      doAttack()
      time.sleep(0.1)
      doAttack()
      time.sleep(0.1)
    except pyauto.ImageNotFoundException:
      logAction(msgBossKilled)
      combo = False
      break

def attackLavaGate(select=1):
  combo = True
  
  if select == 1:
    doSelect(0.1)

  while combo:
    if not macro:
      logAction(msgTerminate)
      combo = False
      break

    if isBattleMode == False:
      doAura()

    try:
      gate = pyauto.locateOnScreen(imgMobs, grayscale=False, confidence=.9, region=getHpBar())
      logAction(msgAttackBoss)
      doAttack()
      time.sleep(0.1)
      doAttack()
      time.sleep(0.1)
    except pyauto.ImageNotFoundException:
      logAction(msgBossKilled)
      combo = False
      break