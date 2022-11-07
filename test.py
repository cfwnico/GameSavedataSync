from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import Common

a = Common.get_now_time()
print(a)

a = "aaaaaaaaaa"
# b = True
# c = False

if a is True:
    print("a is true")
else:
    print("a is false")
app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("TestWindow")
win.resize(800, 600)
win.show()
app.exec()
