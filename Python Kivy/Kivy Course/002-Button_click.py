import os

# KIVY
try:
    from kivy.app import App
    from kivy.properties import StringProperty
    from kivy.uix.gridlayout import GridLayout

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class WidgetsExample(GridLayout):
    number = StringProperty("0")
    number_sum = 0

    def Onclick(self):
        self.number_sum += 1
        self.number = str(self.number_sum)

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()