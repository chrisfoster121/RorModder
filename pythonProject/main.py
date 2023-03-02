# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# importing libraries
from PyQt5.QtWidgets import *
from Window import Window
import sys



# create pyqt5 app
App = QApplication(sys.argv)

# setting cursor flashtime
App.setCursorFlashTime(100)

# setting application object name
App.setObjectName("GfG")

# setting application display name
App.setApplicationDisplayName("RoR2 Modder")

# beep sound will occur when application
# is opened
App.beep()

# message displayed about the Qt
App.aboutQt()

# create the instance of our Window
window = Window(500, 400)

# start the app
sys.exit(App.exec())


