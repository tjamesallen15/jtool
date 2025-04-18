from pynput.keyboard import Key

# CONSTANT KEYS
KEY_SELECT = 'z'
KEY_DASH = '1'
KEY_FADE = '2'
KEY_ATTACK = ['3', '4', '5']
KEY_VERADRIX  = '6'
KEY_LOOT_ACTION = '7'
KEY_FURY = '8'
KEY_HP = '9'
KEY_AURA = '0'
KEY_BM_ATK = '-'
KEY_BM = '='
KEY_DESELECT = Key.esc
KEY_LOOT_SPACE = Key.space
KEY_BUFF_LONG_1 = '1'
KEY_BUFF_LONG_2 = '2'
KEY_BUFF_SHORT_1 = '3'
KEY_BUFF_SHORT_2 = '4'
KEY_BUFF_NORMAL_1 = '5'
KEY_BUFF_NORMAL_2 = '6'
KEY_DEBUFF_LIGHT = '7'
KEY_DEBUFF_HARD = '8'

# CONSTANT INTERVALS
VAL_INTERVAL_RANGE = 0.3
VAL_INTERVAL_MELEE = 0.8
VAL_INTERVAL_DEFAULT = 0.3

# CONSTANT UI VARIABLES
APP_FONT = "Tahoma 10"
APP_FRAME_SIZE = "330x310"
APP_NAME = "Cabal JTool"
APP_VERSION = "5.90"
APP_FULL_NAME = APP_NAME + " " + APP_VERSION
HOTKEY_TERMINATE = "ctrl+r"
HOTKEY_PAUSE = "ctrl+g"
LIST_CLASS = ["BL", "FB", "WA", "GL", "FS", "FA", "FG", "DM"]

# CONSTANT MESSAGES
MSG_START_DG = "Starting Dungeon"
MSG_END_DG = "End Dungeon"
MSG_EXIT = "Macro Exit"
MSG_PAUSE = "Pause for 15 delayonds"
MSG_TERMINATE ="Macro Terminate"
MSG_PATH_FIND = "Pathfind, "
MSG_ATTACK = "Attack, "
MSG_ATTACK_BOSS = "Boss Attack"
MSG_MONSTERS_FOUND = "Monsters Found, "
MSG_BOSS_FOUND = "Boss Found"
MSG_BOSS_KILLED = "Boss Killed"
MSG_MONSTERS_NOT_FOUND = "Monsters Not Found"
MSG_BOSS_NOT_FOUND = "Boss Not Found"
MSG_BLOCKER_FOUND = "Blocker Found"
MSG_BLOCKER_NOT_FOUND = "Blocker Not Found"
MSG_MONSTERS_CLEARED = "Monsters Cleared"
MSG_GATE_CLEARED = "Gate Cleared"
MSG_MONSTER_CLEARED = "Monster Cleared"
MSG_CHECK_BOSS = "Checking Boss"
MSG_CHECK_BOX = "Checking Box"
MSG_BOX_FOUND = "Box Found"
MSG_BOX_NOT_FOUND = "Box Not Found"
MSG_LOOTING_DROP = "Looting Drops"
MSG_PATH_STOP = "Pathing stop, attacking"
MSG_MOVE_STOP = "Moving stop, proceeding"
MSG_CHECK_END_DG = "Check End Dungeon"
MSG_NOTIFICATION_FOUND = "Notification Found"
MSG_NOTIFICATION_NOT_FOUND = "Notification Not Found"
MSG_ACTION = ""
MSG_RUN_NUMBER =  "Run #: "
MSG_CLICK = "Click #: "
MSG_BACKTRACK = "Backtrack #: "
MSG_CHALLENGE_DG = "Challenge Dungeon"
MSG_ENTER_DG = "Enter Dungeon"
MSG_BUTTON_FOUND = "Button Found"
MSG_BUTTON_NOT_FOUND = "Button Not Found"
MSG_BUFFS = "Buffing"
MSG_SHORT_BUFFS = "Buffing Shorts"
MSG_DEBUFF = "Debuffing"
MSG_DEBUFF_HARD = "Hard Debuffing"
MSG_BATTLE_MODE = "Doing Mode II"
MSG_DICE_ROLL = "Check Dice Roll"
MSG_DICE_ROLL_OKAY = "Check Dice Roll Okay"
MSG_CHECK_DIALOG_FOUND =  "Check Dialog Found"
MSG_CHECK_DIALOG_NOT_FOUND = "Check Dialog Not Found"
MSG_GATE_FOUND = "Gate Found "
MSG_GATE_NOT_FOUND = "Gate Not Found"
MSG_WAIT = "Waiting"
MSG_MOVING_POSITION = "Moving to position"
MSG_ROLL_EQUIPMENT = "Rolling Equipment"
MSG_ROLL_EQUIPMENT_NOT_FOUND = "Roll Equipment Not Found"
MSG_CHECK_UMPRA_WEAK = "Checking Umpra The Weak"
MSG_UMPRA_WEAK_FOUND = "Umpra The Weak Found"
MSG_UMPRA_WEAK_NOT_FOUND = "Umpra The Weak Not Found"
MSG_CHECK_SIENA_BOX = "Checking Siena Box"
MSG_SIENA_BOX_FOUND = "Found Siena Box"
MSG_SIENA_BOX_NOT_FOUND = "Siena Box Not Found"
MSG_CHECKING_SUB_PASS = "Checking Sub Pass"
MSG_CABAL_WINDOW_FOUND = "Cabal Window Found"
MSG_CABAL_WINDOW_NOT_FOUND = "Cabal Window Not Found"
MSG_LAUNCHER_LOAD = "Launcher Loading"
MSG_LAUNCHER_LOAD_COMPLETE = "Launcher Complete"
MSG_LAUNCHER_LOAD_FAIL = "Launcher Fail"
MSG_PLAY_BTN_FOUND = "Play Button Found"
MSG_PLAY_BTN_NOT_FOUND = "Play Button Not Found"
MSG_CHECK_BEAD_WINDOW = "Checking Bead Window"
MSG_BEAD_WINDOW_FOUND = "Bead Window Found"
MSG_BEAD_WINDOW_NOT_FOUND = "Bead Window Not Found"
MSG_SUB_PASS_FOUND = "Sub Password Found"
MSG_SUB_PASS_NOT_FOUND = "Sub Password Not Found"
MSG_COUNTDOWN = "Countdown, "
MSG_OPEN_APPLICATION = "Opening application"
MSG_CLOSE_APPLICATION = "Closing application"
MSG_TYPE_PASSWORD = "Typing password"
MSG_TYPE_PIN = "Typing pin"
MSG_CHECK_RECONNECT = "Check reconnecting status"
MSG_CLEARING_WINDOWS = "Clearing windows"
MSG_ENTER_WORLD = "Entering world"
MSG_MOVE_BEAD = "Moving bead window"
MSG_MOVE_APPLICATION = "Moving application window"
MSG_SELECT_TASK_BAR = "Selecting taskbar"
MSG_DUNGEON_RESTART = "Restarting before automation"
MSG_PET_SKILL_FOUND = "Pet Skill Found"
MSG_PET_SKILL_FOUND = "Pet Skill Not Found"
MSG_CHECK_BATTLE_IMAGE = "Check Battle Image"

# CONSTANT IMAGES
IMG_APP_ICON = "img/icon.png"
IMG_ZERO = "img/0.jpg"
IMG_ONE = "img/1.jpg"
IMG_TWO = "img/2.jpg"
IMG_THREE = "img/3.jpg"
IMG_FOUR = "img/4.jpg"
IMG_FIVE = "img/5.jpg"
IMG_SIX = "img/6.jpg"
IMG_SEVEN = "img/7.jpg"
IMG_EIGHT = "img/8.jpg"
IMG_NINE = "img/9.jpg"
IMG_START_WINDOWS = "img/startwindows.jpg"
IMG_CABAL_WINDOW = "img/cabalwindow.jpg"
IMG_LOGIN = "img/login.jpg"
IMG_CHALLENGE_DG = "img/challengedg.jpg"
IMG_DUNGEON = "img/dungeon.jpg"
IMG_ENTER_DG = "img/enterdg.jpg"
IMG_END_DG = "img/enddg.jpg"
IMG_EXIT_DG = "img/exitdg.jpg"
IMG_LAUCHER_LOAD = "img/launcher-loading.jpg"
IMG_LAUCHER_COMPLETE = "img/launcher-complete.jpg"
IMG_LAUNCHER_PLAY = "img/launcher-play.jpg"
IMG_CHANNEL_ONE = "img/channel-one.jpg"
IMG_CHANNEL_TWO = "img/channel-two.jpg"
IMG_CHANNEL_THREE = "img/channel-three.jpg"
IMG_CHANNEL_FOUR = "img/channel-four.jpg"
IMG_SELECT_CHARACTER = "img/select-character.jpg"
IMG_TIMEOUT = "img/timeout.jpg"
IMG_TIMEOUT_EXIT = "img/timeout-exit.jpg"
IMG_SUB_PASS = "img/subpass.jpg"
IMG_DUAL_BOSS = "img/dualboss.jpg"
IMG_BOSS = "img/boss.jpg"
IMG_SEMI_BOSS = "img/semiboss.jpg"
IMG_MOBS = "img/mobs.jpg"
IMG_DICE_ROLL = "img/rolladice.jpg"
IMG_DICE_OKAY = "img/diceokay.jpg"
IMG_DICE_EQUIP = "img/rollequip.jpg"
IMG_CHECK_NOTIF = "img/checknotif.jpg"
IMG_CLOSE_NOTIF = "img/closenotif.jpg"
IMG_CHECK_DIALOG = "img/checkdialog.jpg"
IMG_BOX = "img/box.jpg"
IMG_GATE = "img/gate.jpg"
IMG_HOLY_BOX = "img/holybox.jpg"
IMG_LAVA_GATE = "img/lava-gate.jpg"
IMG_FIRE_GUARD = "img/fire-guard.jpg"
IMG_GATEKEEPER = "img/gatekeeper.jpg"
IMG_SHOWORAI = "img/showorai.jpg"
IMG_OWLBEAR = "img/owlbear.jpg"
IMG_OWLBEAR_L = "img/owlbear-2.jpg"
IMG_VAOUR = "img/vaour.jpg"
IMG_VAOUR_L = "img/vaour-2.jpg"
IMG_HATCHLING = "img/hatchling.jpg"
IMG_HATCHLING_L = "img/hatchling-2.jpg"
IMG_AREIHORN = "img/areihorn.jpg"
IMG_PHIXIA = "img/phixia.jpg"
IMG_SIENA = "img/siena.jpg"
IMG_UMPRA_WEAK = "img/umpra-w.jpg"
IMG_MAX_CRIT_RATE = "img/max-crit-rate.jpg"
IMG_CRIT_RATE = "img/crit-rate.jpg"
IMG_CRIT_DAMAGE = "img/crit-dmg.jpg"
IMG_CRIT_RESIST = "img/resist-rate.jpg"
IMG_EVA = "img/evasion.jpg"
IMG_CHAOS_GATE = "img/chaosgate.jpg"

IMG_BLOODY_SWEEPER = "img/potf/bloody-sweeper.jpg"
IMG_BLOODY_FANG = "img/potf/bloody-fang.jpg"
IMG_BEELZEBUB = "img/potf/beelzebub.jpg"
IMG_ELECTULA = "img/potf/electula.jpg"
IMG_QUEEN_RIPLEY = "img/potf/queen-ripley.jpg"
IMG_ANT_HILL = "img/potf/ant-hill.jpg"
IMG_BURNING_ANT_HILL = "img/potf/burning-ant-hill.jpg"
IMG_FULL_ANT_HILL = "img/potf/full-ant-hill.jpg"
IMG_WEB_GATE = "img/potf/web-gate.jpg"

# IMG - CLASSES MODE
IMG_MODE_BATTLE_FA = "img/mode-classes/battle-fa.jpg"
IMG_MODE_FINAL_FA = "img/mode-classes/final-fa.jpg"
IMG_MODE_BATTLE_FG = "img/mode-classes/battle-fg.jpg"
IMG_MODE_FINAL_FG = "img/mode-classes/final-fg.jpg"
IMG_MODE_BATTLE_DM = "img/mode-classes/battle-dm.jpg"
IMG_MODE_FINAL_DM = "img/mode-classes/final-dm.jpg"
IMG_MODE_BATTLE_WA = "img/mode-classes/battle-wa.jpg"
IMG_MODE_FINAL_WA = "img/mode-classes/final-wa.jpg"
IMG_MODE_BATTLE_FB = "img/mode-classes/battle-fb.jpg"
IMG_MODE_FINAL_FB = "img/mode-classes/final-fb.jpg"
IMG_MODE_BATTLE_BL = "img/mode-classes/battle-bl.jpg"
IMG_MODE_FINAL_BL = "img/mode-classes/final-bl.jpg"
IMG_MODE_BATTLE_GL = "img/mode-classes/battle-gl.jpg"
IMG_MODE_FINAL_GL = "img/mode-classes/final-gl.jpg"
IMG_MODE_BATTLE_FS = "img/mode-classes/battle-fs.jpg"
IMG_MODE_FINAL_FS = "img/mode-classes/final-fs.jpg"

# FILE
FILE_CHANGELOG = "CHANGELOG.md"
FILE_READ = "r"

# CONSTANT UNITS
UNIT_EMPTY = "--"
UNIT_BLOCKER = "Blocker"
UNIT_MUSH_FLOWER = "Mushed and Ectoflower"
UNIT_MOSS_TOAD = "Mossite and Toad"
UNIT_LUMBER_DORIGO = "Lumber and Dorigo"
UNIT_CUTTER_TOAD = "Moscutter and Toad"
UNIT_BOAR_SNAKE = "Boars and Snake"
UNIT_WHITE_SNAKE = "White Snake"
UNIT_ORPHIDIA = "Orphidia"
UNIT_MECHAPE = "Mechape"
UNIT_ARMUN = "Armun"
UNIT_TRICUS = "Tricus"
UNIT_GATE = "Gate"
UNIT_GATE_ONE = "Gate One"
UNIT_GATE_TWO = "Gate Two"
UNIT_GATE_THREE = "Gate Three"
UNIT_GATE_FOUR = "Gate Four"
UNIT_LEGRIN = "Legrin of Wind"
UNIT_LEO = "Leo of Wind"
UNIT_ESPI = "Espi of Wind"
UNIT_DRACO = "Draco of Wind"
UNIT_AKENAPH = "Akenaph"
UNIT_SPECTOR = "Spector"
UNIT_ICE_BLOCK = "Ice Block"
UNIT_FIRE_GUARD = "Fire Guard"
UNIT_GATEKEEPER_JASON = "Gatekeeper Jason"
UNIT_LAVA_GATE = "Lava Gate"
UNIT_MECH_LION = "Mech Lion"
UNIT_MECH_LIHONAR = "Mech Lihonar"
UNIT_ESPADA_1 = "Espada"
UNIT_ESPADA_2 = "Espada II"
UNIT_ESPADA_3 = "Espada III"
UNIT_POERTE = "Poerte"
UNIT_REDONNO = "Redonno"
UNIT_POWER_SUPPLY = "Power Supply"
UNIT_SHOWORAI_F = "Showorai [F]"
UNIT_SHOWORAI_R = "Showorai [R]"
UNIT_SHOWORAI_M = "Showorai [M]"
UNIT_GHOST = "Ghost"
UNIT_AREIHORN_GROUP = "Arehorn's Group"
UNIT_HUMMING_BIRD = "Hummingbird"
UNIT_HATCHLING = "Hatchling"
UNIT_PHIXIA = "Phixia"
UNIT_AREIHORN = "Areihorn"
UNIT_OWL_BEAR = "Owl Bear"
UNIT_VAOUR = "Vaour"
UNIT_KNIGHT = "Knight of Wind"
UNIT_SHIRDRAHN = "Shirdrahn"
UNIT_UMPRA_WEAK = "Umpra The Weak"
UNIT_SIENA_BOX = "Siena Box"
UNIT_BOX = "Box"
UNIT_ARENA_MOBS = "Arena Monsters"

UNIT_WEB_GATE = "Web Gate"
UNIT_BLOODY_SWEEPER = "Bloody Sweeper"
UNIT_BLOODY_FANG = "Bloody Fang"
UNIT_BEELZEBUB = "Beelzebub"
UNIT_ELECTULA = "Electula"
UNIT_QUEEN_RIPLEY = "Queen Ripley"
UNIT_OMERAI = "Omerai"

UNIT_BLOODY_HORN = "Bloody Horn"
UNIT_KORAIDER = "Koraider"
UNIT_MUTANT_KORAIDER = "Mutang Koraider"
UNIT_ELECTRISHIA = "Electrishia"
UNIT_ANT_HILL = "Ant Hill"

UNIT_BORDER_CRAB = "Border Crab"
UNIT_CRAG_CRAB = "Crag Crab"
UNIT_TOLERANT = "Tolerant"
UNIT_CRASIO = "Crasio"
UNIT_GROGO = "Grogo"
UNIT_GROGO_II = "Grogo II"
UNIT_GARLIARDO = "Garliardo"
UNIT_GUARDIAN_GOLEM = "Guardian Golem"
UNIT_DARTHPENCIO = "Darthpencio"
UNIT_GNELL = "Gnell"
UNIT_RULER_BARIALD = "Ruler Bariald"

UNIT_APE = "Ape"
UNIT_FLOATER = "Floater"
UNIT_COPTER = "Copter"
UNIT_STEAKY = "Steaky"
UNIT_PENNA = "Penna"
UNIT_STEAMER = "Steamer"
UNIT_OBSTACLE = "Obstacle"

UNIT_FLA_3571 = 'FLA 3571'
UNIT_MONAD_FRAGMENT = 'Monad Fragment'
UNIT_MONAD = 'Monad'
UNIT_SEEKER = 'Seeker'
UNIT_AION = 'Aion'
UNIT_SERVANT = 'Servant'
UNIT_VITO = 'Vito'
UNIT_PLUMA = 'Pluma'
UNIT_PERIUS = 'Perius'

# JSON DATA
DATA_JSON = "data/config.json"
DATA_FRAME = "frame"
DATA_BUTTON = "btn"
DATA_DUNGEON = "dungeon"
DATA_RUNS = "runs"
DATA_MODE = "mode"
DATA_ACCESS_LEVEL = "access_level"
DATA_CHAR_CLASS = "char_class"
DATA_CHANNEL = "channel"
DATA_LEADER = "leader"
DATA_MEMBER = "member"
DATA_BUFFS = "buffs"
DATA_CANCEL_BUFFS = "cancel_buffs"
DATA_DEBUFFS = "debuffs"
DATA_HARD_DEBUFFS = "hard_debuffs"
DATA_SHORTS = "shorts"
DATA_HARD_SHORTS = "hard_shorts"
DATA_CLASS = "class"
DATA_VERADRIX = "veradrix"
DATA_RUN_RESTART = "run_restart"
DATA_CLOSE_APP = "close_app"
DATA_RUNS = "runs"
DATA_PWORD = "pword"
DATA_PIN = "pin"
DATA_RESOLUTION = "resolution"
DATA_LOAD = "load"
DATA_CONNECTION = "connection"
DATA_PET = "pet"
DATA_OTHERS = "others"
DATA_JOIN_WAR = "war"

# DUNGEON NAMES
DG_HVA = "Hazardous Valley (Awakened)"
DG_HVH = "Hazardous Valley (Hard)"
DG_HVM ="Hazardous Valley (Medium)"
DG_HVE =  "Hazardous Valley (Easy)"
DG_SCA = "Steamer Crazy (Awakened)"
DG_CFA = "Catacomb Frost (Awakened)"
DG_LHA = "Lava Hellfire (Awakened)"
DG_HW = "Holy Windmill"
DG_TM = "Terminus Machina"
DG_PCA = "Panic Cave (Awakened)"
DG_HK = "Holy Keldrasil"
DG_S1P = "Altar of Siena B1F (Prideus)"
DG_CI = "Chaos Infinity"
DG_HVV = "Hazardous Valley (Veradrix)"
DG_POTF = "Purifier of the Forest"
DG_MI = "Mirage Island"
DG_SCP = "Steamer Crazy (Premium)"
DG_CLS = "Celestia"

# ACCESS LEVEL
ACCESS_FREE = "Free"
ACCESS_PRO = "Pro"
ACCESS_PREMIUM = "Premium"
ACCESS_TESTER = "Tester"
ACCESS_TESTER_II = "Tester II"
ACCESS_SUPER = "Super"

# STATES
STATE_SPACE = " "
STATE_EMPTY = ""
STATE_NA = "N/A"
STRING_HOUR = "h "
STRING_MIN = "m "
STRING_SEC = "s"
STATE_ONE = 1
STATE_ZERO = 0
STATE_TWO = 2
STATE_THREE = 3
STATE_FOUR = 4
STATE_FIVE = 5
STATE_DISABLED = "disabled"
STATE_NORMAL = "normal"
STATE_READONLY = "readonly"
STATE_CENTER = "center"
IS_TRUE = True
IS_FALSE = False
CLICK_LEFT = "left"
CLICK_RIGHT = "right"

# STATE LABEL
LBL_LICENSE = "License: "
LBL_EXPIRATION_NA = "Expiration: N/A"
LBL_EXPIRATION = "Expiration: "
LBL_OPEN_SECTION = " ("
LBL_CLOSE_SECTION = ")"
LBL_HYPHEN = " | "

# LABELS
BTN_START = "Start"
BTN_SOLO = "Solo"
BTN_MEMBER = "Member"
BTN_LEADER = "Leader"
BTN_TRAIN = "Train"
BTN_CLICK = "Click"
BTN_DIVIDE_ONE = "Divide (1)"
BTN_TRANSFER = "Transfer"
BTN_JOIN_WAR = "Join War"
BTN_MOVE_WINDOW = "Move Window"
BTN_TEST = "Test"
LBL_EMPTY = ""
LBL_DUNGEON = "Dungeon: "
LBL_RUNS = "Runs: "
LBL_CLASS = "Class: "
LBL_MODE = "Mode II: "
LBL_BUFFS = "Buffs: "
LBL_DEBUFFS = "Debuffs: "
LBL_SHORTS = "Shorts: "
LBL_LEADER = "Leader: "
LBL_MEMBER = "Member: "
LBL_VERADRIX = "Veradrix: "
LBL_CLOSE_APP = "Exit Cabal: "
LBL_CLICK = "Click #: N/A"
LBL_MACRO = "Idle"
LBL_CURRENT_RUN = "Run #: --"
LBL_RUN_TIME = "Run Time: "
LBL_RUN_TIME_EMPTY = "Run Time: --"
LBL_STATUS_TRAINING = "Status: Training"
LBL_STATUS_IDLE = "Status: Idle"
LBL_RESTART_NOTE_PREFIX = "Every "
LBL_RESTART_NOTE_SUFFIX = " runs"

LBL_RUN_RESTART = "Run Restart: "
LBL_RUN_RESTART_EMPTY = "Run Restart: --"
LBL_RUN_RESTART_NOTE = "Restart every run specified."
LBL_DG_RESTART = "DG Restart: "
LBL_DG_RESTART_NOTE = "Restart first before macro."
LBL_CLOSE_APP_NOTE = "Close Cabal after macro."
LBL_PWORD = "Password: "
LBL_PIN = "PIN: "
LBL_RESOLUTION = "Resolution: "
LBL_CHANNEL = "CH: "
LBL_RESOLUTION_NOTE = "Only listed resolution above are supported."
LBL_LOAD_TIME = "Load Time: "
LBL_LOAD_TIME_NOTE = "Adjust based on application load for login screen."
LBL_CABAL_NOTE = "Make sure Cabal World is available in start menu."

LBL_PET_NOTE_1 = "Inventory Tab must only have pet, kit and cores."
LBL_PET_NOTE_2 = "Pet in Slot 1, Kit in Slot 2 and rest cores."
LBL_PET_NOTE_3 = "Pet should have remove one skill before start."
LBL_PET_NOTE_4 = "NPC should be beside of player, camera zoomed in."
LBL_PET_NOTE_5 = "Auto train will check the skills marked above."

LBL_NPC_X = "NPC X: "
LBL_NPC_Y = "NPC Y: "
LBL_MCR = "MCR: "
LBL_CRT = "CRT: "
LBL_CDI = "CDI: "
LBL_CRR = "CRR: "
LBL_EVA = "EVA: "

LBL_STORE_NOTE = "Open NPC store first before clicking the buttons."
LBL_MAIL_NOTE = "Open first mail before clicking the button."
BTN_FURY = "Fury"
BTN_UPGRADE = "Upgrade"
BTN_FORCE = "Force"
BTN_MAILS = "Mails"
LBL_CUSTON_CLICK_NOTE = "Use custom x and y for other items in store."

LBL_CLICKS = "Clicks: "

BTN_FREE = "Free"
BTN_PRO = "Pro"
BTN_PREMIUM = "Premium"
BTN_CHANGELOG = "Changelog"

TAB_DUNGEON = "Dungeon"
TAB_CONNECTION = "Connection"
TAB_PET = "Pet"
TAB_OTHERS = "Others"
TAB_PRICING = "Pricing"

IS_MELEE = 0
IS_RANGE = 1
VAL_CLASS_FB = 'FB'
VAL_CLASS_FA = 'FA'
VAL_CLASS_FS = 'FS'
VAL_CLASS_FG = 'FG'
VAL_CLASS_DM = 'DM'
VAL_CLASS_BL = 'BL'
VAL_CLASS_GL = 'GL'
VAL_CLASS_WA = 'WA'

TYPE_BOSS = 'Boss'
TYPE_SEMI = 'Semi'
TYPE_MONSTER = 'Monster'
TYPE_SHADE = 'Shade'