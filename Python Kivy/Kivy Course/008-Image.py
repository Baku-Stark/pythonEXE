import os

# KIVY
try:
    from kivy.app import App
    # from kivy.uix.gridlayout import GridLayout

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class ImageExample():
    pass

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()