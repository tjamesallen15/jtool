# cabal_window = pyauto.locateOnScreen("img/cabalwindow.jpg", grayscale=False, confidence=.9)
# util.set_cabal_window(cabal_window)
# util.go_cabal_window()

# test_var = True if val_mode.get() == util.STATE_ONE else False
# print(test_var)

# lbl_party = Label(tab_dungeon, text="Party: ", state="disabled")
# lbl_party.place(x=140, y=75)

# global val_party
# val_party = IntVar(value=0)
# chkbtn_party = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_party, state="disabled")
# chkbtn_party.place(x=185, y=76)

# lbl_leader = Label(tab_dungeon, text="Leader: ", state="disabled")
# lbl_leader.place(x=235, y=75)

# global val_leader
# val_leader = IntVar(value=0)
# chkbtn_leader = ttk.Checkbutton(tab_dungeon, text="", onvalue=1, offvalue=0, variable=val_leader, state="disabled")
# chkbtn_leader.place(x=293, y=76)

# sys.exit()

# 1 pyautogui.moveTo(cabalwindow[0] + 400, cabalwindow[1] + 670)
# 2 pyautogui.moveTo(cabalwindow[0] + 430, cabalwindow[1] + 670)
# 3 pyautogui.moveTo(cabalwindow[0] + 470, cabalwindow[1] + 670)
# 4 pyautogui.moveTo(cabalwindow[0] + 500, cabalwindow[1] + 670)
# 5 pyautogui.moveTo(cabalwindow[0] + 540, cabalwindow[1] + 670)
# 6 pyautogui.moveTo(cabalwindow[0] + 570, cabalwindow[1] + 670)
# 7 pyautogui.moveTo(cabalwindow[0] + 610, cabalwindow[1] + 670)
# 8 pyautogui.moveTo(cabalwindow[0] + 650, cabalwindow[1] + 670)
# 9 pyautogui.moveTo(cabalwindow[0] + 680, cabalwindow[1] + 670)
# 10 pyautogui.moveTo(cabalwindow[0] + 715, cabalwindow[1] + 670)
# - pyautogui.moveTo(cabalwindow[0] + 750, cabalwindow[1] + 670)
# = pyautogui.moveTo(cabalwindow[0] + 790, cabalwindow[1] + 670)


# util.move(375, 150)
# pyauto.mouseDown(button="right")
# util.move(700, 150)
# pyauto.mouseUp(button="right")
# pyauto.scroll(-10000)

# hp_bar = (int(cabalwindow[0] + 475), int(cabalwindow[1] + 25), 45, 30)
# im1 = pyauto.screenshot(region=hp_bar)
# im1.save("c:\screenshot.png")

#### MELEE
# util.move(620, 550)
# util.doFade(0.5)
#### MELEE

# shorts = ttk.Combobox(values=shortList, state="readonly")
# shorts.current(0)
# shorts.config(width=5)
# shorts.place(x=75, y=135)

# util.move_click(15, 535, 0.8)

# {
#     "dungeon": 0,
#     "mode": 0,
#     "buffs": 1,
#     "shorts": 0,
#     "range": 0,
#     "veradrix": 0,
#     "pword": "",
#     "pin": "",
#     "resolution": 0,
#     "load": 2
# }

# if get_party_status() == util.STATE_ONE:
#       try:
#         roll = pyauto.locateOnScreen(IMG_DICE_EQUIP, grayscale=False, confidence=.9, region=get_screen_region())
#         log_action(MSG_ROLL_EQUIPMENT)
#         move_rel(10, 10, roll)
#         move_click_rel(10, 10, roll)
#       except pyauto.ImageNotFoundException:
#         log_action(MSG_NO_ROLL_EQUIPMENT_FOUND)

# LAVA HELLFIRE AWAKENED
# util.move(550, 100)
# util.move(550, 100)
# util.move(650, 200)

# CHAOS INFINITY
# util.move(620, 150)
# util.do_dash(1.5)

# util.move(620, 250)
# util.do_dash(1.5)
# util.move(620, 100)
# util.do_dash()
# util.do_fade()

# util.move(620, 600)
# util.do_dash()
# util.do_fade(1.5)
# util.do_fade()



# util.move_click(700, 250, 4)
# util.move_click(510, 225, 5)
# util.move_click(1000, 300, 5)