# What's New with JTool

All notable changes to this project will be documented in this file.

# v5.75

## v5.75 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]
- [CI] Chaos Infinity [v5.50]
- [HVV] Hazardous Valley (Veradrix) [v5.50]
- [RH] Radiant Hall [v5.65] [Development]

## v5.75 Features

- [Application] Added access for Tester II
- [Application] Added reset_battle_mode() for faster wait time
- [Application] Reduced cancel_aura in set_battle_mode from 2 to 1.2
- [CI] Added checker for Gate of Chaos
- [CI] Added fast plunder mechanism
- [LHA] Added fade step after dash on second boss position
- [LHA] Added dash and fade positioning after second boss

## v5.75 Fixes

- [Application] Decrease wait time for box checking from 1 to 0.5
- [CI] Improved retargeting mobs for faster clear time
- [CI] Reduced wait time for member party
- [CI] Reduced wait time for cancel_aura()
- [CI] Replaced cancel_aura to reset_battle_mode in the end of dungeon
- [LHA] Reduced wait time on scene change
- [PCA] Improved response time on dialog queues
- [PCA] Removed unnecessary wait clauses

# v5.70

## v5.70 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]
- [CI] Chaos Infinity [v5.50]
- [HVV] Hazardous Valley (Veradrix) [v5.50]
- [RH] Radiant Hall [v5.65]

## v5.70 Features

- [Application] Refactored some coding structure
- [Application] Added trial user version
- [Application] Added Class Input
- [CI] Added Cancel Aura before reposition center
- [CI] Added mob selection on reposition center
- [CI] Added double checker for repositions
- [CI] Added horizontal reposition for Wave 10
- [Dungeon] Increased wait time from 1 to 2 before entering dungeon
- [Dungeon] Increased wait time for end dungeon message from 70 to 100
- [LHA] Added another source for second guard
- [PCA] Added fail check on the Showorai shadows

## v5.70 Fixes

- [Application] Reduced wait time of mail from 0.5 to 0.3
- [Application] Reduced default log time sec from 2 to 1.5 
- [Application] Removed archer and range input
- [Application] Optimized do_buffs(), do_short_buffs() and force_short_buffs()
- [CFA] Optimized run time
- [CFA] Simplified some logs
- [CI] Fixed centering positions
- [CI] Increased wait time for mobs from 20 to 30
- [CI] Changed reposition threshold from 15 to 20
- [HK] Reduced wait time on some key points
- [LHA] Improved movements in relation to the dungeon updates
- [LHA] Fixed box not being detected properly on the final boss
- [LHA] Fixed second boss position
- [LHA] Changed the positioning for last boss
- [LHA] Decreased path finding of lava gate from 12 to 10
- [LHA] Increased wait time for semi bosses from 15 to 20
- [PCA] Increased wait time for the last shadow from 3 to 20
- [PCA] Optimized wait time

# v5.65

## v5.65 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]
- [CI] Chaos Infinity [v5.50]
- [HVV] Hazardous Valley (Veradrix) [v5.50]
- [RH] Radiant Hall [v5.65]

## v5.65 Features

- [RH] Added Radiant Hall for Development Phase (Only available to Super License)
- [CI] Added Fail Run Count for near impossible recoveries

## v5.65 Fixes

- [CI] Fixed stuck up scenarios near the gate
- [LHA] Improved speed of automation on some mob checks
- [LHA] Fixed automation bugs caused by game updates
- [PCA] Fixed automation bugs caused by game updates

# v5.60

## v5.60 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]
- [CI] Chaos Infinity [v5.50]
- [HVV] Hazardous Valley (Veradrix) [v5.50]

## v5.60 Features

- [Application] Added custom click x and y for other store items.
- [Application] Added cont and strict mode in attack_semi_boss
- [Application] Added evasion on pet train
- [Application] Added back member status for party type automations (Beta Phase)
- [Applicaiton] Added Pet Train on beta phase, available now for testers
- [Application] Added Chaos Infinity on beta phase, available now for testers
- [Application] Added Panic Cave on beta phase, available now for testers
- [Dungeon] Changed wait time before starting dungeon from 3 to 1

## v5.60 Fixes

- [CFA] Fixed battle mode transitions
- [CFA] Improved dialog sequence
- [CI] Fixed stuck up scenarios when mobs are not present in the middle
- [CI] Improved sequence per fight
- [LHA] Fixed occasional stuck up in final boss in certain scenarios when shorts are turned off
- [LHA] Fixed battle mode transitions
- [SCA] Disabled sidestep to avoid stuck up
- [SCA] Adjusted wait time for mob spawn
- [S1P] Fixed discrepancy in calling of methods
- [TM] Minor adjustments for stuck up scenarios when some mobs are not been lured to you
- [TM] Added backtrack checking on redonno sequence

# v5.50

## v5.50 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]
- [CI] Chaos Infinity [v5.50]
- [HVV] Hazardous Valley (Veradrix) [v5.50]

## v5.50 Features

- [Application] Increased application window size for other features
- [Application] Added timer for dungeon automation
- [Application] Added additional notes for features
- [Application] Added Status for pet training
- [Application] Extended list of choice in dungeon restarts
- [Application] Extended list of choice in click stores
- [Application] Added pet training feature available only for super license
- [Application] Added Chaos Infinity in Development and Beta Phase
- [Application] Added Hazardous Valley (Veradrix) in Development and Beta Phase
- [Application] Added interface for inheritance and preparation for object oriented approach
- [Application] Added new button in pricing for changelogs
- [Dungeon] Added fail counter for dungeons that has fail reset instance
- [Dungeon] Changed thread sleep on some areas during end dungeon cycle
- [Dungeon] Changed the order of method focus_mobs() similar to attack_mobs()
- [Dungeon] Added focus_mob_boss() to be used for mobs that behaves like a boss on certain dungeons
- [Dungeon] Updated all existing dungeon macro to class oriented
- [LHA] Updated gatekeeper sprite for better accuracy on image reading

## v5.50 Fixes

- [CFA] Added a fail check on second checkpoint to reduced failed dungeon instance
- [CFA] Changed approach on position to the second checkpoint location to avoid stuck up
- [CFA] Added fail run count
- [HK] Inverted the approach on the final mobs and boss
- [HK] Reduced the amount of tick counts from 50 to 30 on waiting time for bosses
- [HK] Increased wait time for portal dialogs
- [HK] Added fail run count
- [HK] Reduced time waiting on final group of mobs before the last boss
- [HVENH] Reworked first sequence of movements up to the bridge
- [LHA] Added fail run count
- [LHA] Improved pathfinding towards bosses to greatly reduced failed dungeon instance
- [PCA] Slightly increased combat ready on the final boss
- [PCA] Added a fail check on first checkpoint after nualle to reduced failed dungeon 
- [PCA] Added fail run countinstance
- [PCA] Fixed position on first shadow that results to failed dungeon instance
- [PCA] Fixed position of range characters on final boss
- [SCA] Fixed some scenarios where character will stuck up on second boss
- [TM] Slightly improved third espada and poerte sequence to reduced time spent on run

# v5.40

## v5.40 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]

## v5.40 Features

- [Application] Changed status to license
- [Application] Added account name beside the license

## v5.40 Fixes

- [Dungeon] Optimized action on attack and select
- [TM] Fixed first espada encounter stuck on power supply

# v5.35

## v5.35 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]

## v5.35 Features

- [Application] Updated instruction manual for better readability
- [Application] Added pricing tab
- [Application] Added Tester Access Level

## v5.35 Fixes

- [Dungeon] Fixed click portal for blockers with more than one

# v5.31

## v5.31 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]

## v5.31 Features

- [Application] Added get mail feature
- [Application] Added restart feature in Developmental Phase
- [Application] Added dungeon restart in Developmental Phase
- [Application] Added move bead window
- [Application] Added veradrix second checkbox to only use if necessary
- [Application] Added config and database for user access level and data retention
- [Application] Updated constant values throughout the UI
- [Application] Added Setup Files and Manual Instructions
- [Dungeon] Added necessary log actions when moving to positions
- [Dungeon] Added reconnect check in Developmental Phase

## v5.31 Fixes

- [Application] Disabled party and leader feature
 temporarily
- [Application] Improved functionality of reconnect
- [Application] Added catch exception in moving bead window
- [Dungeon] Overhauled attack functions for faster action response
- [Dungeon] Fixed not using health potion while doing battle mode
- [CFA] Fixed stuck up in ice block because of sidestep
- [CFA] Added node click for second ice dialog
- [HK] Optimized run through of the final boss
- [HK] Increased count threshold from 20 to 50 when waiting for the third boss
- [HK] Changed slightly dashing position when coming back for final after doing battle mode
- [HK] Fixed second boss sequence
- [HK] Increased count threshold from 20 to 50 when waiting for the second boss
- [HK] Changed image reading for second and third group
- [HK] Changed positioning when entering portal
- [HW] Changed positioning when entering portal
- [PCA] Fixed melee adjustments on position for final boss
- [S1P] Fixed a bug where characters would not get into portal after dashing
- [S1P] Adjustments on siena box plunder from 4 to 10
- [S1P] Fixed misclicks after force exit dungeon when having a dash error to checkpoints
- [TM] Overhauled dungeon automation for faster run clearance

# v5.21

## v5.21 Dungeons Available

- [HVA] Hazardous Valley (Awakened) [v1.00]
- [HVENH] Hazardous Valley (Easy | Medium | Hard) [v3.40]
- [SCA] Steamer Crazy (Awakened) [v4.51]
- [CFA] Catacomb Frost (Awakened) [v4.61]
- [LHA] Lava Hellfire (Awakened) [v4.95]
- [HW] Holy Windmill [v4.95]
- [TM] Terminus Machina [v4.95]
- [PCA] Panic Cave (Awakened) [v5.01]
- [HK] Holy Keldrasil [v5.11]
- [S1P] Altar of Siena B1F (Prideus) [v5.11]

## v5.21 Features

- [Application] Updated the changelog to a more specific readable way
- [Application] Added dungeons available in changelog
- [Application] Added tab controls, dungeon and misc tabs
- [Dungeon] Added new method plunder_box() to deprecate the old method loot_box()
- [Dungeon] Added new method plunder_final_box() to deprecate the old method loot_final_box()
- [Dungeon] Added new method plunder_ref_box() to deprecate the old method loot_ref_box()
- [Dungeon] Removed method loot_essentials() and do_loot()
- [Dungeon] Refactored do_aura() and removed do_aura_strict()
- [Dungeon] Refactored do_attack() and removed do_attack_strict()
- [Dungeon] Changed image of box similar to holy box
- [Dungeon] Added check validation for click dungeon portal when there is a monster blocking it
- [Dungeon] Implement click_portal() method to all dungeons
- [LHA] Added fail safe reset dungeon
- [SCA] Improved overall dungeon automation

## v5.21 Fixes

- [CFA] Updated loot_box() to plunder_box()
- [CFA] Fixed stuck up on second gate after being destroyed
- [CFA] Fixed box not being plundered after boss fight
- [HVA] Added check notifications before loot boxes
- [HVA] Fixed positioning on first boss
- [HVA] Fixed some stuck ups on final orphidia boss
- [HVA] Fixed first loot box not properly opened on certain situations
- [HVA] Updated loot_box() to plunder_box()
- [HVENH] Updated loot_box() to plunder_box()
- [HVENH] Tweaked backtrack mechanics
- [HK] Updated loot_box() to plunder_box()
- [HW] Updated loot_box() to plunder_box()
- [LHA] Overhauled pathing for semi bosses
- [LHA] Updated loot_box() to plunder_box()
- [LHA] Fixed stuck up situations on going to lava gate
- [LHA] Fixed optimizations on pathing
- [LHA] Fixed pathing for semi bosses and bosses
- [PCA] Updated loot_box() to plunder_box()
- [SCA] Updated loot_box() to plunder_box()
- [SCA] Fixed minor glitches on path_find()
- [SCA] Fixed pathing to make it smooth on dialog transition
- [S1P] Updated loot_ref_box() to plunder_ref_box()
- [TM] Updated loot_box() to plunder_box()

# v5.11

## v5.11 Features

- [Application] Made the Terminate Function more function faster than before
- [Application] Added Check Notifications
- [Application] Changed variable and method cases
- [Application] Added Party and Leader Option for Experiment Purposes
- [Dungeons] Added feature that makes character exit dungeon to restart again
- [HK] Added Holia Keldrasil for dungeon automation (Development Phase)
- [TM] Added Backtrack for Terminus Machina
- [TM] Added Terminus Machina for Party and Leader Option for Experiment Purposes
- [S1P] Added Altar of Siena B1F - Prideus for Development Phase

## v5.11 Fixes

- [Applicaiton] Fixed changelog order
- [Application] Fixed Terminate Function that exits the whole software
- [CFA] Fixed Catacomb Frost (Awakened) wrong pathing of dashes
- [HVA] Fixed Hazardous Valley (Awakened) not holding up with the Orphidia timers
- [HVENH] Fixed Hazardous Valley (ENH) minor glitches
- [HK] Fixed Holia Keldrasil Third Boss not detecting properly
- [PCA] Fixed Panic Cave (Awakened) abrupt exits when range classes are in battle mode
- [TM] Fixed Terminus Machina glitches in some sequences
- [TM] Fixed Terminus Machina Glitches
- [TM] Fixed optimization for Terminus Machina

# v5.01

## v5.01 Features

- [Application] Added Pylint
- [PCA] Added Panic Cave (Awakened) for Development Phase for Range Classes

## v5.01 Fixes

- [Dungeon] Fixes a lot of discrepancy movements in dungeons

# v4.95

## v4.95 Features

- [Application] Added Range Check
- [Application] Added Veradrix Check
- [Application] Change Combobox UI to Checkbox
- [HW] Added Holy Windmill for Development Phase
- [LHA] Added Lava Hellfire (Awakened) for Development Phase
- [TM] Added Terminus Machina for Development Phase

## v4.95 Fixes

- [Application] Loop improvements for better response for image reading
- [Application] Change variables, refactor structures
- [Application] Image reading improvements by region sector

# v4.61

## v4.61 Features

- [CFA] Started Catacomb Frost (Awakened) for Development

# v4.51

## v4.51 Fixes

- [Application] Improved reading image during loops
- [HVENH] Fixed glitches in HVENH Automation
- [SCA] Fixed glitches in Steamer Crazy (Awakened)

# v4.50

## v4.50 Features

- [Application] Added Utility class for refactoring purposes
- [SCA] Added Steamer Crazy (Awakened) for Development Phase

## v4.50 Fixes

- [HVENH] Fixed glitches in HVENH Automation
- [SCA] Fixed glitches in Steamer Crazy (Awakened)

# v3.40

## v3.40 Features

- [HVENH] Added Hazardous Valley Easy, Normal and Hard for Development Phase

## v3.40 Fixes

- [HVA] Fixed glitches in HVA Automation

# v2.10

## v2.10 Features

- [Application] Added GUI for Buffs, Shorts and Mode Two

## v2.10 Fixes

- [HVA] Fixed glitches in HVA Automation

# v1.10

## v1.10 Features

- [Application] Added GUI.
- [Application] Added Trial Program.

# v1.00

## v1.00 Features

- [Application] Added initial files for development.
- [HVA] Added dungeon, Hazardous Valley (Awakened) available for automation.
