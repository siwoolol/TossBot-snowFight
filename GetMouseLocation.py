import time
import pyautogui

while(True):
    pos = pyautogui.position()
    print(f"mousePos: {pos}")
    time.sleep(1)