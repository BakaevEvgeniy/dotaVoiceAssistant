from pynput.keyboard import Key, Controller

from pynput.keyboard import Listener
import time

def tryCastSF(text, keyboard):
    if text.lower() == "boom" or text.lower() == "бум" or text.lower() == "let me die":
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(0.82)
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(0.01)
        keyboard.press("r")
        keyboard.release("r")
        time.sleep(0.15)