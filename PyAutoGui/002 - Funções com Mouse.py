from time import sleep
import pyautogui

# Descobrir o tamanho da tela
width, height = pyautogui.size()
print(f"===MONITOR===\nLargura: {width} \nAltura: {height}")
print('-=' *30)

# Descobrir posição do ponteiro MOUSE
x, y = pyautogui.position()
print(f"Posição X: {x}\nPosição Y:{y}")

# Mover mouse e click
pyautogui.mouseUp(557, 748)
sleep(3)
pyautogui.doubleClick()