import os

# KIVY
try:
    from kivy.app import App
    from kivy.uix.widget import Widget
    from kivy.graphics.context_instructions import Color
    from kivy.graphics.vertex_instructions import Line
    from kivy.graphics.vertex_instructions import Rectangle

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Line(
                points=(100, 100, 400, 500),
                width=2
            )

            Color(0, 1, 0)
            Line(
                circle=(400, 200, 80),
                width=2
            )

            Color(0, 0, 1)
            Line(
                rectangle=(800, 100, 300, 200),
                width=2
            )

            Color(1, 0, 0)
            Rectangle(
                pos=(700, 200), size=(150, 100)
            )

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()