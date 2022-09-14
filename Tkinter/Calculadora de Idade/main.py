import os
from tkinter import *
from time import sleep

# Data atual
from datetime import datetime

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
tempo = datetime.now()
dia = tempo.day
mes = tempo.month
ano = tempo.year

def dataAtual():
    if mes < 10:
        current_date['text'] = f"{dia}/0{mes}/{ano}"
    else:
        current_date['text'] = f"{dia}/{mes}/{ano}"

def calcularIdade():
    print('\033[34mIdade sendo calculada\033[m')
    sleep(0.3)
    print('Limpando terminal')
    sleep(0.3)
    os.system('cls')
    
    dia_user = int(dia_enter.get())
    if dia > dia_user:
        dias = dia - dia_user
    else:
        dias = dia_user - dia

    mes_user = int(mes_enter.get())
    if mes > mes_user:
        meses = mes - mes_user
    else:
        meses = mes_user - mes

    ano_user = int(ano_enter.get())
    if ano > ano_user:
        idade = ano - ano_user
    else:
        idade = ano_user - ano

    # ===== RESULTADO =====
    register['text'] = f"{str(idade)}"
    register2['text'] = f"{str(meses)}"
    register3['text'] = f"{str(dias)}"

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


dia_label = Label(frame2, text="Dia:", font=('Helvetica 10 bold'), bg=frame2_bg, fg=comun_fg)
dia_enter = Entry(frame2)

mes_label = Label(frame2, text="Mês:", font=('Helvetica 10 bold'), bg=frame2_bg, fg=comun_fg)
mes_enter = Entry(frame2)

ano_label = Label(frame2, text="Ano:", font=('Helvetica 10 bold'), bg=frame2_bg, fg=comun_fg)
ano_enter = Entry(frame2)

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

dia_label.place(x=105, y=47)
dia_enter.place(x=155, y=50)

mes_label.place(x=105, y=87)
mes_enter.place(x=155, y=90)

ano_label.place(x=105, y=127)
ano_enter.place(x=155, y=130)

btn.place(x=105, y=235)

dataAtual()
root.mainloop()