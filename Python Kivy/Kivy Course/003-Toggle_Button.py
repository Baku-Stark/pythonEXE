import os

# KIVY
try:
    from kivy.app import App
    from kivy.properties import StringProperty, BooleanProperty
    from kivy.uix.gridlayout import GridLayout

except ModuleNotFoundError:
    os.system('python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/')
# ====================== END OF KIVY

class WidgetsExample(GridLayout):
    number_text = StringProperty('0')
    number_count = 0
    count_status = BooleanProperty(False)

    def Onclick(self):
        if self.count_status:
            self.number_count += 1
            self.number_text = str(self.number_count)

    def onToggle(self, widget):
        print('TOGGLE: ' + widget.state)

        # widget.state = down [botão ativado]
        # widget.state = normal [botão desativado]

        if widget.state == 'normal':
            widget.text = 'Desligado'
            self.count_status = False

        else:
            widget.text = 'Ligado'
            self.count_status = True

class TheLab(App):
    pass

if __name__ == '__main__':
    TheLab().run()