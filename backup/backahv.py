import pyautogui
import pyscreeze
import keyboard as kb
import time
import sys

from pynput import keyboard 
from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller

pkeyboard = Controller()

select = 'z'
dash = '1'
fade = '2'
attack = ['3', '4', '5']
buffAttack = ['6']
lootSpace = Key.space
loot = '7'
fury = '8'
pots = '9'
bmaura = '0'
bm3atk = '-'
bm3 = '='

cabalwindow = []

combo = True
pathing = True
moving = True
macro = True

def terminate():
  print("exit looper")
  global macro
  macro = False

def lootBox():
  pkeyboard.press(select)
  pkeyboard.release(select)
  pkeyboard.press(bm3atk)
  pkeyboard.release(bm3atk)
  pkeyboard.press(attack[0])
  pkeyboard.release(attack[0])
  pkeyboard.press(attack[1])
  pkeyboard.release(attack[1])
  pkeyboard.press(attack[2])
  pkeyboard.release(attack[2])
  pkeyboard.press(bm3atk)
  pkeyboard.release(bm3atk)
  time.sleep(1)
  for x in range(4):
    pkeyboard.press(loot)
    pkeyboard.release(loot)
    time.sleep(0.5)
    pkeyboard.press(lootSpace)
    pkeyboard.release(lootSpace)
    time.sleep(0.5)

def autoEssentials():
  pkeyboard.press(lootSpace)
  pkeyboard.release(lootSpace)
  pkeyboard.press(fury)
  pkeyboard.release(fury)
  pkeyboard.press(pots)
  pkeyboard.release(pots)
  pkeyboard.press(loot)
  pkeyboard.release(loot)

  pkeyboard.release(Key.alt)
  pkeyboard.release(Key.ctrl)

def attackMobs(msg):
  combo = True
  while combo:
    if not macro:
      print("attackMobs Terminate")
      combo = False
      sys.exit()
      break

    pkeyboard.press(bm3)
    pkeyboard.release(bm3)
    autoEssentials()
    pkeyboard.press(bmaura)
    pkeyboard.release(bmaura)

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      time.sleep(0.1)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Attack Mobs: " + msg)
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      pkeyboard.press(attack[0])
      pkeyboard.release(attack[0])
      autoEssentials()
      pkeyboard.press(attack[1])
      pkeyboard.release(attack[1])
      autoEssentials()
      pkeyboard.press(attack[2])
      pkeyboard.release(attack[2])
      autoEssentials()
      time.sleep(1)
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      pkeyboard.press(attack[0])
      pkeyboard.release(attack[0])
      autoEssentials()
      pkeyboard.press(attack[1])
      pkeyboard.release(attack[1])
      autoEssentials()
      pkeyboard.press(attack[2])
      pkeyboard.release(attack[2])
      autoEssentials()
      time.sleep(1)
    except pyautogui.ImageNotFoundException:
      print("Mobs Killed: " + msg)
      combo = False
      break

def attackBoss():
  combo = True
  while combo:
    if not macro:
      print("attackMobs Terminate")
      combo = False
      break

    pkeyboard.press(bm3)
    pkeyboard.release(bm3)
    autoEssentials()
    pkeyboard.press(bmaura)
    pkeyboard.release(bmaura)

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Attack Boss.")
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      pkeyboard.press(attack[0])
      pkeyboard.release(attack[0])
      autoEssentials()
      pkeyboard.press(attack[1])
      pkeyboard.release(attack[1])
      autoEssentials()
      pkeyboard.press(attack[2])
      pkeyboard.release(attack[2])
      autoEssentials()
      time.sleep(1)
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      autoEssentials()
      pkeyboard.press(bm3atk)
      pkeyboard.release(bm3atk)
      pkeyboard.press(attack[0])
      pkeyboard.release(attack[0])
      autoEssentials()
      pkeyboard.press(attack[1])
      pkeyboard.release(attack[1])
      autoEssentials()
      pkeyboard.press(attack[2])
      pkeyboard.release(attack[2])
      autoEssentials()
      time.sleep(1)
    except pyautogui.ImageNotFoundException:
      print("Boss Killed.")
      combo = False
      break

def pathFind(msg):
  pathing = True
  boss = 0
  while pathing:
    if not macro:
      print("attackMobs Terminate")
      pathing = False
      sys.exit()
      break

    print("Pathfinding: " + msg)

    if msg == "Mossites && Toad":
      try:
        vineblock = pyautogui.locateOnScreen('vineblock.jpg', grayscale=False, confidence=.9)
      except pyautogui.ImageNotFoundException:
        print("No vine found.")
      else:
        pathBackTrack("backtrack toad")
    
    try:
      pyautogui.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 260)
      pyautogui.click(cabalwindow[0] + 550, cabalwindow[1] + 260)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Boss Mobs found: " + msg)
      pathing = False
      boss = 1
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 260)
      pyautogui.click(cabalwindow[0] + 450, cabalwindow[1] + 260)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")
    
    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Boss Mobs found: " + msg)
      pathing = False
      boss = 1
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 350, cabalwindow[1] + 260)
      pyautogui.click(cabalwindow[0] + 350, cabalwindow[1] + 260)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Boss Mobs found: " + msg)
      pathing = False
      boss = 1
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 260)
      pyautogui.click(cabalwindow[0] + 250, cabalwindow[1] + 260)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Boss Mobs found: " + msg)
      pathing = False
      boss = 1
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 150, cabalwindow[1] + 260)
      pyautogui.click(cabalwindow[0] + 150, cabalwindow[1] + 260)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
      print("Boss Mobs found: " + msg)
      pathing = False
      boss = 1
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    if msg == "Lumber and Moth":
      try:
        pyautogui.moveTo(cabalwindow[0] + 150, cabalwindow[1] + 460)
        pyautogui.click(cabalwindow[0] + 150, cabalwindow[1] + 460)
        pkeyboard.press(select)
        pkeyboard.release(select)
        mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
        pkeyboard.press(dash)
        pkeyboard.release(dash)
        print("Mobs found: " + msg)
        pathing = False
        print("pathing set to false")
        break
      except pyautogui.ImageNotFoundException:
        print("No mobs found.")

      try:
        pkeyboard.press(select)
        pkeyboard.release(select)
        mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.9)
        print("Boss Mobs found: " + msg)
        pathing = False
        boss = 1
        print("pathing set to false")
        break
      except pyautogui.ImageNotFoundException:
        print("No mobs found.")

  if boss == 0:
    attackMobs(msg)

def pathBackTrack(msg):
  pathing = True
  boss = 0
  while pathing:
    if not macro:
      print("attackMobs Terminate")
      combo = False
      sys.exit()
      break

    print("Path Backtrack: " + msg)
    try:
      pyautogui.moveTo(cabalwindow[0] + 700, cabalwindow[1] + 560)
      pyautogui.click(cabalwindow[0] + 700, cabalwindow[1] + 560)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 560)
      pyautogui.click(cabalwindow[0] + 750, cabalwindow[1] + 560)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 560)
      pyautogui.click(cabalwindow[0] + 800, cabalwindow[1] + 560)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 560)
      pyautogui.click(cabalwindow[0] + 850, cabalwindow[1] + 560)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

    try:
      pyautogui.moveTo(cabalwindow[0] + 900, cabalwindow[1] + 560)
      pyautogui.click(cabalwindow[0] + 900, cabalwindow[1] + 560)
      pkeyboard.press(dash)
      pkeyboard.release(dash)
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('mobs.jpg', grayscale=False, confidence=.9)
      print("Mobs found: " + msg)
      pathing = False
      print("pathing set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No mobs found.")

  attackMobs(msg)

def runAhv():
  # MAIN
  kb.add_hotkey("esc", terminate)
  global cabalwindow
  cabalwindow = pyautogui.locateOnScreen('cabalwindow.jpg', grayscale=False, confidence=.5)
  pyautogui.moveTo(cabalwindow[0] + 50, cabalwindow[1] + 15)
  pyautogui.click(cabalwindow[0] + 50, cabalwindow[1] + 15)
  print(cabalwindow)

  # AHV
  # AHV ENTER FREE VIEW
  pyautogui.moveTo(cabalwindow[0] + 677, cabalwindow[1] + 361)
  pyautogui.moveTo(cabalwindow[0] + 680, cabalwindow[1] + 361)

  time.sleep(1)
  pyautogui.click(cabalwindow[0] + 680, cabalwindow[1] + 361)

  time.sleep(1)

  enterdg = pyautogui.locateOnScreen('enterdg.jpg', grayscale=False, confidence=.9)
  pyautogui.moveTo(enterdg[0] + 15, enterdg[1] + 15)
  pyautogui.click(enterdg[0] + 15, enterdg[1] + 15)

  time.sleep(2)

  challengedg = pyautogui.locateOnScreen('challengedg.jpg', grayscale=False, confidence=.9)
  pyautogui.moveTo(challengedg[0] + 15, challengedg[1] + 15)
  pyautogui.click(challengedg[0] + 15, challengedg[1] + 15)

  time.sleep(1)

  pyautogui.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 150)
  pyautogui.mouseDown(button="right")
  pyautogui.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 150)
  pyautogui.mouseUp(button="right")
  pyautogui.scroll(-10000)

  time.sleep(3)

  pyautogui.moveTo(cabalwindow[0] + 850, cabalwindow[1] + 600)
  pkeyboard.press(dash)
  pkeyboard.release(dash)

  time.sleep(2)

  # LEAFING
  moving = True
  while moving:
    if not macro:
        print("attackMobs Terminate")
        moving = False
        sys.exit()
        break

    pathFind("Mushed and Ectoflower")
    try:
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.8)
      moving = False
      print("moving set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No boss found.")

  pyautogui.moveTo(cabalwindow[0] +  850, cabalwindow[1] + 600)
  pkeyboard.press(dash)
  pkeyboard.release(dash)
  # pyautogui.click(cabalwindow[0] + 850, cabalwindow[1] + 600)

  attackBoss()
  lootBox()

  # MOSSITES & TOAD
  moving = True
  while moving:
    pathFind("Mossites && Toad")
    try:
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.8)
      moving = False
      print("moving set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No boss found.")

  attackBoss()
  lootBox()

  # LUMBER AND MOTH
  moving = True
  while moving:
    if not macro:
        print("attackMobs Terminate")
        moving = False
        sys.exit()
        break

    pathFind("Lumber and Moth")
    try:
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.8)
      moving = False
      print("moving set to false")
      break
    except pyautogui.ImageNotFoundException:
      print("No boss found.")


  pyautogui.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 260)
  pyautogui.click(cabalwindow[0] + 550, cabalwindow[1] + 260)

  time.sleep(0.2)

  pyautogui.moveTo(cabalwindow[0] + 450, cabalwindow[1] + 260)
  pyautogui.click(cabalwindow[0] + 450, cabalwindow[1] + 260)

  time.sleep(0.2)

  pyautogui.moveTo(cabalwindow[0] + 350, cabalwindow[1] + 260)
  pyautogui.click(cabalwindow[0] + 350, cabalwindow[1] + 260)

  time.sleep(0.2)

  pyautogui.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 260)
  pyautogui.click(cabalwindow[0] + 250, cabalwindow[1] + 260)

  time.sleep(0.2)

  pyautogui.moveTo(cabalwindow[0] + 250, cabalwindow[1] + 660)
  pyautogui.click(cabalwindow[0] + 250, cabalwindow[1] + 660)

  time.sleep(1)

  try:
    pkeyboard.press(select)
    pkeyboard.release(select)
    mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.8)
    attackBoss()
  except pyautogui.ImageNotFoundException:
    print("No boss found.")

  time.sleep(1)

  pyautogui.moveTo(cabalwindow[0] + 800, cabalwindow[1] + 600)
  pyautogui.click(cabalwindow[0] + 800, cabalwindow[1] + 600)

  time.sleep(0.2)

  pkeyboard.press(dash)
  pkeyboard.release(dash)

  bossCount = 0
  while bossCount < 2:
    try:
      pkeyboard.press(select)
      pkeyboard.release(select)
      mobs = pyautogui.locateOnScreen('boss.jpg', grayscale=False, confidence=.8)
      bossCount += 1
      attackBoss()
    except pyautogui.ImageNotFoundException:
      print("No boss found.")

  pyautogui.moveTo(cabalwindow[0] + 550, cabalwindow[1] + 260)
  pyautogui.click(cabalwindow[0] + 550, cabalwindow[1] + 260)

  time.sleep(3)

  pyautogui.moveTo(cabalwindow[0] + 1050, cabalwindow[1] + 420)
  pyautogui.click(cabalwindow[0] + 1050, cabalwindow[1] + 420)

  time.sleep(3)

  lootBox()
  time.sleep(0.5)
  lootBox()
  time.sleep(0.5)
  lootBox()
  time.sleep(0.5)

  enddungeon = pyautogui.locateOnScreen('enddungeon.jpg', grayscale=False, confidence=.9)
  pyautogui.moveTo(enddungeon[0] + 50, enddungeon[1] + 15)
  pyautogui.click(enddungeon[0] + 50, enddungeon[1] + 15)

  rolladice = pyautogui.locateOnScreen('rolladice.jpg', grayscale=False, confidence=.9)
  pyautogui.moveTo(rolladice[0] + 50, rolladice[1] + 15)
  pyautogui.click(rolladice[0] + 50, rolladice[1] + 15)

  time.sleep(1)
  pyautogui.click(rolladice[0] + 50, rolladice[1] + 15)
