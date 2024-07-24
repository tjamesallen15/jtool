# What's New with JTool

All notable changes to this project will be documented in this file.

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
- [Application] Added reconnect feature in Developmental Phase
- [Application] Added move bead window
- [Dungeons] Added necessary log actions when moving to positions
- [Dungeon] Added reconnect check in Developmental Phase

## v5.31 Fixes

- [Application] Disabled party and leader feature
 temporarily
- [Application] Improved functionality of reconnect
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