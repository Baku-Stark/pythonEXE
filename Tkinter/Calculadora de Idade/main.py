import os
from tkinter import *
from time import sleep

# ----------------------------------------
# Cores
comun_fg = "#f0f8ff"

frame1_bg = "#1A1A1A"
frame1_fg = "#90FA2E"

frame2_bg = "#111111"

# ----------------------------------------
# Janela
root = Tk()
root.geometry("300x450")
root.title("Calculadora de Idade")
root.resizable(width=FALSE, height=FALSE)

# ----------------------------------------
# Frame Personalizado
class meuFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = frame1_bg
        self['width'] = 300
        self['height'] = 180

class meuFrame2(Frame):
    def __init__(self, root):
        super().__init__()
        self['bg'] = frame2_bg
        self['width'] = 300
        self['height'] = 270

# ----------------------------------------
# Função
def calcularIdade():
    print('\033[34mIdade sendo calculada\033[m')
    sleep(0.3)
    print('Limpando terminal')
    sleep(2)
    os.system('cls')


# --------------------------------------------------------------------------------
# Widgets
frame = meuFrame(root)
frame2 = meuFrame2(root)

# ----------------FRAME CIMA ----------------
title = Label(
    frame, text="Registre sua idade", font=('Arial 20 bold'),
    bg=frame1_bg, fg=comun_fg
)
sub_title1 = Label(
    frame, text="Anos", font=('Arial 12 bold'), bg=frame1_bg, fg=comun_fg
)
sub_title2 = Label(
    frame, text="Meses", font=('Arial 12 bold'), bg=frame1_bg, fg=comun_fg
)
sub_title3 = Label(
    frame, text="Dias", font=('Arial 12 bold'), bg=frame1_bg, fg=comun_fg
)

register = Label(
    frame, text="00", font=('Arial 15 bold'),
    bg=frame1_bg, fg=frame1_fg
)
register2 = Label(
    frame, text="00", font=('Arial 15 bold'),
    bg=frame1_bg, fg=frame1_fg
)
register3 = Label(
    frame, text="00", font=('Arial 15 bold'),
    bg=frame1_bg, fg=frame1_fg
)

# ----------------FRAME BAIXO ----------------
register4 = Label(
    frame2, text="Data atual:", font=('Arial 15 bold'), bg=frame2_bg, fg=comun_fg
)

current_date = Label(
    frame2, text="--/--/----", font=('Arial 15 bold'), bg=frame2_bg, fg=comun_fg
)

btn = Button(
    frame2, text="Calcular Idade", font=('Arial 9 bold'), command=calcularIdade, 
    bg=frame1_bg, fg=comun_fg, border=None, relief=RAISED, overrelief=RIDGE
)

# --------------------------------------------------------------------------------
# Painel
frame.grid(row=0, column=0)
frame2.grid(row=1, column=0)

title.place(x=25, y=35)
register.place(x=35, y=100)
register2.place(x=135, y=100)
register3.place(x=235, y=100)
sub_title1.place(x=25, y=130)
sub_title2.place(x=125, y=130)
sub_title3.place(x=225, y=130)

register4.place(x=35, y=10)
current_date.place(x=155, y=10)

btn.place(x=105, y=235)

root.mainloop()