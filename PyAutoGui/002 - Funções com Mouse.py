from time import sleep
import pyautogui

# Descobrir o tamanho da tela
print('-=' *30)
width, height = pyautogui.size()
print(f"===MONITOR===\nLargura: {width} \nAltura: {height}")
print('-=' *30)
print('')
# Descobrir posição do ponteiro MOUSE
print('-=' *30)
x, y = pyautogui.position()
print(f"Posição X: {x}\nPosição Y:{y}")
print('-=' *30)
print('')
# Mover mouse e click
pyautogui.mouseUp(557, 748)
sleep(3)
pyautogui.doubleClick()