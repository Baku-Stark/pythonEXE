from time import sleep
import pyautogui

pyautogui.press("win")
sleep(1.3)
pyautogui.write("cmd", interval=0.25)
sleep(1.3)
pyautogui.press("return") # ---- TECLA ENTER