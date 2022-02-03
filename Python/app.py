import pyautogui as pg
import time

pg.hotkey("win","r")
pg.typewrite("https://www.youtube.com/watch?v=nqc4t4029as\n")
time.sleep(2)
pg.typewrite("k")
pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("mis primeros pasos\n")
time.sleep(3)
pg.typewrite("en python con\n")
time.sleep(2)
pg.typewrite("pyautogui\n")