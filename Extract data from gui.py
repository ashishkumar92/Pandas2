import time

import pywinauto
from pywinauto.application import Application

app = Application().connect(title="Calculator")
time.sleep(5)
w = pywinauto.findwindows.find_window(title="Calculator")
window=app.window(handle=w)

window.print_control_identifiers()