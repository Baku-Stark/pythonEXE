import os

# KIVY
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.uix.button import Button
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.pagelayout import PageLayout

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class ScrollViewExample(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.min_height = 2000

class PageLayoutExample(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "Wallace"

        for i in range(1, 11):
            
            button = Button(
                text=f"{i}", size_hint=(None, None),
                size=('200dp', '200dp')
            )

            self.add_widget(button)

class MainWidget(Widget):
    pass

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()