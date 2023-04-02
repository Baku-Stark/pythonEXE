import os

# KIVY
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        b1 = Button(
            text="B-1"
        )

        b2 = Button(
            text="B-2"
        )

        self.orientation = "vertical"

        self.add_widget(b1)
        self.add_widget(b2)

class MainWidget(Widget):
    pass

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()