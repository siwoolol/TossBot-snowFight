from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pos1: (x, y)
# pos2: (x, y)
# pos3: (x, y)
# RGB(1, 188, 102)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    # TODO replace x, y with new data
    if pyautogui.pixel(581, 400)[0, 1, 2] == 1, 188, 102:
        click(581, 400)
    if pyautogui.pixel(682, 400)[0, 1, 2] == 1, 188, 102:
        click(682, 400)
    if pyautogui.pixel(770, 400)[0, 1, 2] == 1, 188, 102:
        click(770, 400)
