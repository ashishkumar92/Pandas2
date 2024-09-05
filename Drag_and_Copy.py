import pyautogui
import time
import pyperclip
import pywinauto
# from pywinauto.application import Application
time.sleep(5)
# app = pywinauto.application.Application()
#
# while True:
#     pp = pyautogui.position()
#     time.sleep(1)
#     print(pp)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("C")
pyautogui.moveTo(464,670,3)
pyautogui.dragTo(500,670,3,button="left")
# time.sleep(8)

# # # app.start("Notepad.exe")
# pyautogui.press("V")
# pyautogui.keyUp("ctrl")
list = []
var = pyperclip.paste()
list.append(var)
print(list)


# import pyautogui as pya
# import pyperclip  # handy cross-platform clipboard text handler
# import time
# i=0
# while i<5:
#     def copy_clipboard():
#         pya.hotkey('ctrl', 'c')
#         time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
#         return pyperclip.paste()
#
#     # double clicks on a position of the cursor
#     pya.doubleClick(pya.position())
#
#     list = []
#     var = copy_clipboard()
#     list.append(var)
#     print(list)
#     i+=1