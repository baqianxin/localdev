import os
import time
import math
import pyautogui
from pymouse import PyMouse
from win32api import GetSystemMetrics


class MouseClick:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def autoclick1(self):
        pyautogui.click(self.x, self.y, clicks=1, interval=0.0, button='left')

    def autoclick2(self):
        PyMouse().click(self.x, self.y, button=1)


while True:
    width = math.ceil(GetSystemMetrics(0) / 2)
    height = math.ceil(GetSystemMetrics(1) / 2)
    MouseClick(width, height).autoclick1()
    #MouseClick(width, height).autoclick2()
    time.sleep(60)
