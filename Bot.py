from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pos1: (92, 769)
# pos2: (254, 769)
# pos3: (423, 769)
# RGB(0, 165, 101)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(rr/100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    rr = random.randint(3, 6)

    if pyautogui.pixel(92, 769)[0] == 0:
        click(92, 769)
        print("r(0) detected in (92, 769)")
        print(f"object clicked: took {rr*10}ms")

    elif pyautogui.pixel(254, 769)[0] == 0:
        click(254, 769)
        print("r(0) detected in (254, 769)")
        print(f"object clicked: took {rr*10}ms")

    elif pyautogui.pixel(423, 769)[0] == 0:
        click(423, 769)
        print("r(0) detected in (423, 769)")
        print(f"object clicked: took {rr*10}ms")