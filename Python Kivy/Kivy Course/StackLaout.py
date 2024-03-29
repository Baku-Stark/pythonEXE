import os

# KIVY
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.uix.button import Button
    from kivy.uix.stacklayout import StackLayout

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        b = Button(
            text="Z", size_hint=(.2, .2)
        )

        self.add_widget(b)

class MainWidget(Widget):
    pass

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()