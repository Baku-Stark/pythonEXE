import os

# KIVY
try:
    from kivy.app import App
    from kivy.uix.widget import Widget

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()