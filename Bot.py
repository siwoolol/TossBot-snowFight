from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pos1: (92, 769)
# pos2: (254, 769)
# pos3: (423, 769)
# RGB(1, 188, 102)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    # pos1 check
    if pyautogui.pixel(92, 769)[0] == 1 & pyautogui.pixel(92, 769)[1] == 188 & pyautogui.pixel(92, 769)[2] == 102:
        click(92, 769)

    # pos2 check
    if pyautogui.pixel(254, 769)[0] == 1 & pyautogui.pixel(254, 769)[1] == 188 & pyautogui.pixel(254, 769)[2] == 102:
        click(254, 769)

    # pos3 check
    if pyautogui.pixel(423, 769)[0] == 1 & pyautogui.pixel(423, 769)[1] == 188 & pyautogui.pixel(423, 769)[2] == 102:
        click(423, 769)