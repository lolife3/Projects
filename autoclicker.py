import keyboard
import pyautogui


while True:
    while keyboard.is_pressed('space'):
        pyautogui.click()
        pyautogui.PAUSE = 0.01
