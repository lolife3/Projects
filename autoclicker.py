import keyboard
import pyautogui


def main():
    while True:
        while keyboard.is_pressed('space'):
            pyautogui.click()
            pyautogui.PAUSE = 0.03

if __name__ == "__main__":
    main()
