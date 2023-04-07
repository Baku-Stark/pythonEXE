import os

# KIVY
try:
    from kivy.app import App
    from kivy.metrics import dp
    from kivy.uix.widget import Widget
    from kivy.graphics.vertex_instructions import Ellipse
    from kivy.properties import Clock

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ball_size = dp(50)

        self.vx = dp(3)
        self.vy = dp(3)

        with self.canvas:
            self.ball = Ellipse(
                pos=self.center,
                size=(self.ball_size, self.ball_size)
            )

        # atualizar conteúdo    (função, tempo)
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        print(f"on size : {str(self.width)}, {str(self.height)}")
        # min size [on size : 800, 600]
        # max size [on size : 1360, 705]


        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx

        if y < 0:
            y = 0
            self.vy = -self.vy

        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()