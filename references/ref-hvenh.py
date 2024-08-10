# def run_dungeon(runs=1):
#   run_counter = 0
#   while run_counter < runs:
#     util.set_reset_status(False)
#     util.check_run_restart(run_counter)
#     run_counter += 1
#     util.log_action(util.MSG_START_DG)
#     util.log_run(run_counter)

#     # Click Cabal Window
#     util.go_cabal_window()
#     util.release_keys()
#     util.go_skill_slot(0.5)
#     util.do_buffs()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Click Dungeon
#     util.move(677, 361)
#     util.move(735, 361, 0.5)
#     util.click_portal(735, 361)

#     if difficulty == dungeonList[0]:
#       util.move_click(440, 300, 1)
#     elif difficulty == dungeonList[1]:
#       util.move_click(440, 280, 1)
#     elif difficulty == dungeonList[2]:
#       util.move_click(440, 260, 1)

#     # Enter Dungeon
#     util.enter_dungeon()
#     util.challenge_dungeon()

#     util.move(250, 150)
#     pyauto.mouseDown(button="right")
#     util.move(700, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(440, 260, 0.3)
#     util.do_dash(0.5)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Cutter and Toad Sequence
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#           util.log_action(util.MSG_TERMINATE)
#           moving = False

#       if moving == False:
#         break

#       path_find(util.UNIT_CUTTER_TOAD)
#       try:
#         boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(util.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(util.MSG_NO_BOSS_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.do_deselect_pack()
#     util.move(630, 520)
#     util.do_fade(0.5)
#     util.move(550, 250)
#     util.do_dash(0.5)

#     checking = True
#     while checking:
#       if not util.get_macro_state():
#         util.log_action(util.MSG_TERMINATE)
#         checking = False

#       if checking == False:
#          break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         checking = False
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(util.MSG_NO_BOSS_FOUND)

#     # First Boss
#     util.attack_boss()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.do_deselect_pack()
#     util.move_click(570, 260)
#     util.do_fade(1.5)
#     util.do_fade(0.5)

#     util.plunder_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Boars and Snakes Sequence (Orphidia I)
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#           util.log_action(util.MSG_TERMINATE)
#           moving = False

#       if moving == False:
#         break

#       path_find(util.UNIT_BOAR_SNAKE)
#       try:
#         boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(util.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(util.MSG_NO_BOSS_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Position for Orphidia I
#     util.do_deselect_pack()
#     position_orphidia()

#     # Attack Orphidia I
#     try:
#       util.do_select(0.1)
#       boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#       util.log_action(util.MSG_BOSS_FOUND)
#       util.attack_boss()
#     except pyauto.ImageNotFoundException:
#       util.log_action(util.MSG_NO_BOSS_FOUND)
#       util.force_exit_dungeon()
#       util.set_reset_status(True)

#     if util.get_reset_status():
#       continue

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(640, 560)
#     util.do_fade(0.5)
#     util.plunder_box()

#     # Orphidia Sequence II
#     path_find_white_snake()
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#           util.log_action(util.MSG_TERMINATE)
#           moving = False

#       if moving == False:
#         break

#       path_find(util.UNIT_WHITE_SNAKE)
#       try:
#         boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(util.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(util.MSG_NO_BOSS_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Position for Orphidia II
#     position_orphidia()

#     util.wait(1)
#     # Attack Orphidia II
#     try:
#       util.do_select(0.1)
#       boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#       util.log_action(util.MSG_BOSS_FOUND)
#       util.attack_boss()
#     except pyauto.ImageNotFoundException:
#       util.log_action(util.MSG_NO_BOSS_FOUND)
#       util.force_exit_dungeon()
#       util.set_reset_status(True)

#     if util.get_reset_status():
#       continue

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(640, 560)
#     util.do_fade(0.5)
#     util.plunder_box()

#     # Orphidia Sequence III
#     path_find_white_snake()
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#           util.log_action(util.MSG_TERMINATE)
#           moving = False

#       if moving == False:
#         break

#       path_find(util.UNIT_WHITE_SNAKE)
#       try:
#         boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(util.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(util.MSG_NO_BOSS_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Position for Orphidia III
#     position_orphidia()

#     # Attack Orphidia III
#     try:
#       util.do_select(0.1)
#       boss = pyauto.locateOnScreen(util.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#       util.log_action(util.MSG_BOSS_FOUND)
#       util.attack_boss()
#     except pyauto.ImageNotFoundException:
#       util.log_action(util.MSG_NO_BOSS_FOUND)
#       util.force_exit_dungeon()
#       util.set_reset_status(True)

#     if util.get_reset_status():
#       continue

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(640, 560)
#     util.do_fade(0.5)
#     util.plunder_final_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.set_battle_mode(False)

#     # Start to End Dungeon
#     util.check_notifications()
#     util.end_dungeon()
#     util.dice_dungeon()
#     util.log_action(util.MSG_END_DG)
#     util.wait(3)