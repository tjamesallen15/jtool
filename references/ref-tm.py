# def path_find_deprecated(unit=consts.UNIT_EMPTY):
#   pathing = True
#   boss_found = 0
#   boss_check = 0
#   box_found = 0
#   backtrack_counter = 0
#   while pathing:
#     if not util.get_macro_state():
#       util.log_action(consts.MSG_TERMINATE)
#       pathing = False

#     if pathing == False:
#       break

#     util.log_action(consts.MSG_PATH_FIND + unit)

#     if unit == consts.UNIT_POERTE:
#       backtrack_counter += 1
#       util.log_action(consts.MSG_BACKTRACK + str(backtrack_counter))
#       if (backtrack_counter >= 10):
#         backtrack_counter = 0
#         path_backtrack(unit)

#     if unit == consts.UNIT_MECH_LIHONAR or unit == consts.UNIT_ESPADA_1 or unit == consts.UNIT_ESPADA_2 or unit == consts.UNIT_ESPADA_3:

#       if unit != consts.UNIT_ESPADA_2:
#         try:
#           util.move_click(300, 260)
#           util.do_select(0.1)
#           mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#           util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#           pathing = False
#           util.log_action(consts.MSG_PATH_STOP)
#           break
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()
#           util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#         if pathing == False:
#           break

#         # Power Supply
#         if unit == consts.UNIT_ESPADA_3:
#           try:
#             util.do_select(0.1)
#             supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#             util.move(500, 440)
#             util.do_dash(1)
#             util.do_fade(0.5)
#             pathing = False
#           except pyauto.ImageNotFoundException:
#             util.do_deselect_pack()

#         if pathing == False:
#           break

#         try:
#           util.move_click(500, 260)
#           util.do_select(0.1)
#           mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#           util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#           pathing = False
#           util.log_action(consts.MSG_PATH_STOP)
#           break
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()
#           util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#         if pathing == False:
#           break

#         # Power Supply
#         if unit == consts.UNIT_ESPADA_3:
#           try:
#             util.do_select(0.1)
#             supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#             util.move(500, 440)
#             util.do_dash(1)
#             util.do_fade(0.5)
#             pathing = False
#           except pyauto.ImageNotFoundException:
#             util.do_deselect_pack()

#         if pathing == False:
#           break

#       try:
#         util.move_click(600, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.do_deselect_pack()
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       # Power Supply
#       if unit == consts.UNIT_ESPADA_3:
#         try:
#           util.do_select(0.1)
#           supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#           util.move(500, 440)
#           util.do_dash(1)
#           util.do_fade(0.5)
#           pathing = False
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()

#       if pathing == False:
#           break

#       try:
#         util.move_click(580, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.do_deselect_pack()
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       # Power Supply
#       if unit == consts.UNIT_ESPADA_3:
#         try:
#           util.do_select(0.1)
#           supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#           util.move(500, 440)
#           util.do_dash(1)
#           util.do_fade(0.5)
#           pathing = False
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()

#       if pathing == False:
#           break

#       try:
#         util.move_click(620, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.do_deselect_pack()
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       # Power Supply
#       if unit == consts.UNIT_ESPADA_3:
#         try:
#           util.do_select(0.1)
#           supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#           util.move(500, 440)
#           util.do_dash(1)
#           util.do_fade(0.5)
#           pathing = False
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()

#       if pathing == False:
#           break

#       try:
#         util.move_click(560, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.do_deselect_pack()
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       # Power Supply
#       if unit == consts.UNIT_ESPADA_3:
#         try:
#           util.do_select(0.1)
#           supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#           util.move(500, 440)
#           util.do_dash(1)
#           util.do_fade(0.5)
#           pathing = False
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()

#       if pathing == False:
#           break

#       try:
#         util.move_click(640, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.do_deselect_pack()
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       # Power Supply
#       if unit == consts.UNIT_ESPADA_3:
#         try:
#           util.do_select(0.1)
#           supply = pyauto.locateOnScreen(consts.IMG_BOX, grayscale=False, confidence=.9, region=util.get_region())
#           util.move(500, 440)
#           util.do_dash(1)
#           util.do_fade(0.5)
#           pathing = False
#         except pyauto.ImageNotFoundException:
#           util.do_deselect_pack()

#       pathing = False
#       break

#     else:
#       try:
#         util.move_click(600, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_BOSS_FOUND)
#         pathing = False
#         boss_found = 1
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.move_click(580, 260, 0.5)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_BOSS_FOUND)
#         pathing = False
#         boss_found = 1
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.move_click(620, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_BOSS_FOUND)
#         pathing = False
#         boss_found = 1
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.move_click(560, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_BOSS_FOUND)
#         pathing = False
#         boss_found = 1
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.move_click(640, 260)
#         util.do_select(0.1)
#         mobs = pyauto.locateOnScreen(consts.IMG_MOBS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#         pathing = False
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#       try:
#         util.do_select(0.1)
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         util.log_action(consts.MSG_BOSS_FOUND)
#         pathing = False
#         boss_found = 1
#         util.log_action(consts.MSG_PATH_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#       if pathing == False:
#         break

#   if unit == consts.UNIT_ESPADA_1 or unit == consts.UNIT_ESPADA_2 or unit == consts.UNIT_ESPADA_3:
#     action.focus_monsters(unit, 0, 1, val_sidestep)

#   if boss_found == consts.STATE_ZERO and util.get_attack_type() == consts.STATE_ZERO and unit == consts.UNIT_REDONNO:
#     action.focus_monsters(unit, 0, 1, val_sidestep)
#   elif boss_found == consts.STATE_ZERO and util.get_attack_type() == consts.STATE_ZERO and unit == consts.UNIT_POERTE:
#     action.focus_monsters(unit, 0, 1, val_sidestep)
#   elif boss_found == consts.STATE_ZERO:
#     action.attack_monsters(unit, 1, 0.3, val_sidestep)

# def path_backtrack(unit):
#   util.log_action(consts.MSG_BACKTRACK + unit)
#   util.move(800, 400)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   util.move(615, 600)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   util.move(615, 600)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   util.move(615, 600)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   util.move(615, 600)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   util.move(450, 400)
#   util.do_dash(1)
#   util.do_fade(0.5)

#   backtracking = True
#   backtrack_counter = 0
#   while backtracking:
#     backtrack_counter += 1
#     util.log_action(consts.MSG_BACKTRACK + str(backtrack_counter))
#     if (backtrack_counter >= 10):
#       backtrack_counter = 0
#       backtracking = False

#     if backtracking == False:
#       break

#     try:
#       util.move_click(620, 250)
#       util.do_select(0.1)
#       box = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
#       util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#       util.log_action(consts.MSG_PATH_STOP)
#       atk.focus_gate(unit, 0)
#       backtrack_counter += 5
#     except pyauto.ImageNotFoundException:
#       util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#     try:
#       util.move_click(620, 250)
#       util.do_select(0.1)
#       box = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
#       util.log_action(consts.MSG_MONSTERS_FOUND + unit)
#       util.log_action(consts.MSG_PATH_STOP)
#       atk.focus_gate(unit, 0)
#       atk.plunder_box()
#       backtrack_counter += 5
#     except pyauto.ImageNotFoundException:
#       util.log_action(consts.MSG_MONSTERS_NOT_FOUND)

#     if backtracking == False:
#       break

#   util.move(770, 260)
#   util.do_dash(1)
#   util.do_fade(0.5)

# def run_dungeon_deprecated(runs=1):
#   run_counter = 0
#   while run_counter < runs:
#     util.check_run_restart(run_counter)
#     run_counter += 1
#     util.log_action(consts.MSG_START_DG)
#     util.log_run(run_counter)

#     # Click Cabal Window
#     util.go_cabal_window()
#     util.release_keys()
#     util.go_skill_slot(0.2)
#     util.do_buffs()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(375, 150)
#     pyauto.mouseDown(button="right")
#     util.move(700, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     # Click Dungeon
#     self.click_dungeon_portal(600, 240)

#     self.enter_dungeon()
#     self.challenge_dungeon()

#     if util.is_party == consts.STATE_ONE:
#       util.wait(3)

#     util.move(700, 150)
#     pyauto.mouseDown(button="right")
#     util.move(375, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Mech Lion Sequence
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       path_find(consts.UNIT_MECH_LION)
#       try:
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # First Boss
#     util.do_deselect_pack()
#     util.move(700, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.do_short_buffs()
#     util.do_battle_mode()
#     action.attack_boss()
#     atk.plunder_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.set_battle_mode(False)

#     util.move(710, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(710, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(375, 150)
#     pyauto.mouseDown(button="right")
#     util.move(700, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(680, 200)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     atk.focus_gate(consts.UNIT_GATE_ONE)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Mech Lihonar Sequence
#     moving = True
#     counter = 0
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       if counter > 6:
#         moving = False
#         break

#       path_find(consts.UNIT_MECH_LIHONAR)
#       counter += 1
#       print(str(counter))

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(500, 440)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(700, 150)
#     pyauto.mouseDown(button="right")
#     util.move(375, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(350, 200)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(350, 200)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(350, 200)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(700, 150)
#     pyauto.mouseDown(button="right")
#     util.move(375, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     # Gate II
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       gate_counter = path_find_gate_strict(consts.UNIT_GATE_TWO)
#       if gate_counter > 3 and util.get_party_status() == consts.STATE_ONE:
#         moving = False

#       try:
#         gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_full_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     atk.focus_gate(consts.UNIT_GATE_TWO, 1)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(610, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(590, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     # Espada Sequence
#     moving = True
#     counter = 0
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       if counter > 6:
#         moving = False
#         break

#       path_find(consts.UNIT_ESPADA_1)
#       counter += 1
#       print(str(counter))

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(1000, 400)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(320, 500)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(320, 500)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(320, 500)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     atk.focus_gate(consts.UNIT_POWER_SUPPLY)
#     util.do_plunder(1)

#     util.move(375, 150)
#     pyauto.mouseDown(button="right")
#     util.move(900, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(400, 360)
#     util.do_fade(0.5)

#     util.move(550, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(540, 260)
#     util.do_dash(1)
#     util.do_fade(1)

#     # Espada II Sequence
#     moving = True
#     counter = 0
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       if counter > 3:
#         moving = False
#         break

#       path_find(consts.UNIT_ESPADA_2)
#       counter += 1
#       print(str(counter))

#     atk.focus_gate(consts.UNIT_POWER_SUPPLY)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(680, 400)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(600, 150)
#     pyauto.mouseDown(button="right")
#     util.move(375, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(520, 400)
#     util.do_dash(1.5)

#     util.move(650, 150)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(500, 300)
#     if util.get_attack_type() == consts.STATE_ONE:
#       util.do_dash(4)
#     else:
#       util.do_dash(1)
#       util.do_fade(4)

#     # Espada III Sequence
#     moving = True
#     counter = 0
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       if counter > 4:
#         moving = False
#         break

#       path_find(consts.UNIT_ESPADA_3)
#       counter += 1
#       print(str(counter))

#     util.do_deselect_pack()
#     util.wait(1.5)
#     util.move(600, 600)
#     util.do_dash(1)
#     util.do_select(0.1)
#     atk.focus_gate(consts.UNIT_POWER_SUPPLY, 0)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(620, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(900, 300)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     atk.plunder_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.move(770, 260)
#     util.do_dash(1)
#     util.do_fade(2)

#     # Poerte Sequence
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       path_find(consts.UNIT_POERTE)
#       try:
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Second Boss
#     util.do_deselect_pack()
#     util.move(720, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.do_short_buffs()
#     util.do_battle_mode()
#     action.attack_boss()
#     atk.plunder_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue
#     util.set_battle_mode(False)

#     util.move(640, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(640, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(1040, 410)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(570, 550)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(580, 550)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(700, 150)
#     pyauto.mouseDown(button="right")
#     util.move(375, 150)
#     pyauto.mouseUp(button="right")
#     pyauto.scroll(-10000)

#     util.move(640, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     # Gate III
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       gate_counter = path_find_gate_strict(consts.UNIT_GATE_THREE)
#       if gate_counter > 3 and util.get_party_status() == consts.STATE_ONE:
#         moving = False

#       try:
#         gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     if util.get_attack_type == consts.STATE_ONE:
#       util.move_click(650, 450, 1.5)

#     atk.focus_gate(consts.UNIT_GATE_THREE)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Redonno Sequence
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       path_find(consts.UNIT_REDONNO)
#       try:
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Third Boss
#     util.do_deselect_pack()
#     if util.get_attack_type() == consts.STATE_ONE:
#       util.move(580, 260)
#       util.do_dash(1)
#     else:
#       util.move(720, 260)
#       util.do_dash(1)

#     util.do_battle_mode()
#     action.attack_boss()
#     util.set_battle_mode(False)
#     atk.plunder_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     if util.get_battle_mode() == consts.STATE_ONE:
#       util.wait(20)

#     util.move(720, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     util.move(720, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     # Gate IV
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       gate_counter = path_find_gate_strict(consts.UNIT_GATE_FOUR)
#       if gate_counter > 3 and util.get_party_status() == consts.STATE_ONE:
#         moving = False

#       try:
#         gate = pyauto.locateOnScreen(consts.IMG_GATE, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     util.move(800, 400)
#     util.do_fade(0.5)
#     atk.focus_gate(consts.UNIT_GATE_FOUR)
#     util.do_plunder(1)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     # Final Boss
#     util.do_battle_mode()
#     util.do_aura(0, 1)
#     util.do_short_buffs()

#     # Final Boss Sequence
#     moving = True
#     while moving:
#       if not util.get_macro_state():
#         util.log_action(consts.MSG_TERMINATE)
#         moving = False

#       if moving == False:
#         break

#       path_find_boss()
#       try:
#         boss = pyauto.locateOnScreen(consts.IMG_BOSS, grayscale=False, confidence=.9, region=util.get_region())
#         moving = False
#         util.log_action(consts.MSG_MOVE_STOP)
#         break
#       except pyauto.ImageNotFoundException:
#         util.log_action(consts.MSG_BOSS_NOT_FOUND)

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.do_deselect_pack()
#     util.move(560, 260)
#     util.do_dash(1)
#     util.do_fade(0.5)

#     # Final Boss
#     action.attack_boss()
#     atk.plunder_final_box()

#     # Check Macro State
#     if not util.get_macro_state():
#       run_counter += 1000
#       continue

#     util.set_battle_mode(False)

#     # Start to End Dungeon
#     util.check_notifications()
#     self.end_dungeon()
#     self.dice_dungeon()
#     util.log_action(consts.MSG_END_DG)
#     util.wait(3)