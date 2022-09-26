from tkinter import *
from tkinter import messagebox

# ----------------------------------------
# IMPORTAÇÃO DE IMPORTÂNCIA
from random import choice

# ----------------------------------------
# CORES
frame1_bg = "#04090D"
frame2_bg = "#191a19"

button = "#3F403F"

letter = "#D7D9D9"
l_emphasis = "#7D9CAA"

# ----------------------------------------
# ROOT PRINCIPAL
root = Tk()

class Application(Frame):
    def __init__(self, master):
        super().__init__()
        # ----------------------------------------
        # WIDGET
        root.geometry("350x400")
        root.title("JOKENPO GAME")
        root.configure(bg="#f0f8ff")
        root.iconbitmap("_img/icon.ico")
        root.resizable(width=FALSE, height=FALSE)

        # ----------------------------------------
        # LABEL CIMA
        self.frame_cima = Frame(
            root, bg=frame1_bg, width=350, height=150)

        self.title_game = Label(
            root, text="JOKENPÔ GAME!!!", font=("Ivy 20 bold"),
            fg=l_emphasis, bg=frame1_bg)

        self.instructions = Button(
            root, text="Instruções", font=('Arial 15'),
            overrelief="ridge", relief="raised", bg=button, fg=letter)
        self.instructions['command'] = self.Instructions

        # ----------------------------------------
        # LABEL BAIXO
        self.frame_baixo = Frame(
            root, bg=frame2_bg, width=350, height=250)

        self.name = Label(
            root, text="Jogador:", font=('Arial 13 bold'), bg=frame2_bg, fg=letter)

        self.set_escolha = Spinbox(
            root, width=13,
            values=("PEDRA", "PAPEL", "TESOURA"))

        self.name_maquina = Label(
            root, text="Máquina:", font=('Arial 13 bold'), bg=frame2_bg, fg=letter)

        self.set_escolha2 = Label(
            root, font=('Arial 13 bold'),
            bg=frame2_bg, fg=letter
        )

        self.situation = Label(
            root, text="- - -", font=('Ivy 13 bold'),
            bg=frame2_bg, fg=letter
        )

        self.play_btn = Button(
            root, text="JOGAR!", font=('Arial 15'),
            overrelief="ridge", relief="raised", bg=button, fg=letter)
        self.play_btn['command'] = self.Play

        # ----------------------------------------
        # PAINEL
        self.frame_cima.pack()
        self.title_game.place(x=50, y=10)
        self.instructions.place(x=125, y=70)

        self.frame_baixo.pack()
        # ---
        self.name.place(x=25, y=210)
        self.set_escolha.place(x=25, y=240)
        # ---
        self.name_maquina.place(x=225, y=210)
        self.set_escolha2.place(x=225, y=240)
        # ---
        self.situation.place(x=35, y=300)
        # ---
        self.play_btn.place(x=130, y=350)
    
    # ----------------------------------------
    # FUNÇÕES
    def Instructions(self):
        janela = Toplevel()
        janela.title("Instruções")
        janela.geometry("650x120")
        janela.resizable(width=FALSE, height=FALSE)

        text = Label(
            janela, font=('Arial 10 bold'), fg="#111111",anchor="nw", justify="left")
        
        text['text'] = "Instruções Do Jogo: \n \n \n 1° - Escolha uma das opções (Pedra, Papel ou Tesoura); \n 2° - Clique no botão 'JOGAR' depois de escolher; \n 3° - A condição de vitória ocorre quando PEDRA > TESOURA | TESOURA > PAPEL | PAPEL > PEDRA"

        text.pack()

    def Play(self):
        messagebox.showinfo(
            title="Jogada feita!", message="Humano Vs. Máquina")
        
        lista = ["PEDRA", "PAPEL", "TESOURA"]
        escolha_computer = choice(lista)
        jogador = self.set_escolha.get()

        self.set_escolha2['text'] = escolha_computer

        if escolha_computer == jogador:
            self.situation['text'] = "Resultado: EMPATE!"

        # --- VITÓRIA DO COMPUTADOR
        elif escolha_computer == "PEDRA" and jogador == "TESOURA":
            self.situation['text'] = "Resultado: COMPUTADOR VENCEU!"
        
        elif escolha_computer == "PAPEL" and jogador == "PEDRA":
            self.situation['text'] = "Resultado: COMPUTADOR VENCEU!"
        
        elif escolha_computer == "TESOURA" and jogador == "PAPEL":
            self.situation['text'] = "Resultado: COMPUTADOR VENCEU!"

        # --- VITÓRIA DO JOGADOR
        elif jogador == "PEDRA" and escolha_computer == "TESOURA":
            self.situation['text'] = "Resultado: JOGADOR VENCEU!"

        elif jogador == "PAPEL" and escolha_computer == "PEDRA":
            self.situation['text'] = "Resultado: JOGADOR VENCEU!"

        elif jogador == "TESOURA" and escolha_computer == "PAPEL":
            self.situation['text'] = "Resultado: JOGADOR VENCEU!"



# ----------------------------------------
# ATIVAÇÃO DA APLICAÇÃO
if __name__ == '__main__':
    root = Application(root)
    root.mainloop()