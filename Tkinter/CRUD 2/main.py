# ===============================================
# IMPORTAÇÕES
from tkinter import *

# ===============================================
# CORES
bg_root = "#111111"
fg_root = "#111111"

frame_top_bottom = "#f0f8ff"
hl_bg = "#9C9FA6"

# ===============================================
# JANELA [config.]
root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        # =======================================
        # ROOT [mainloop]
        root.mainloop()
    
    def tela(self):
        self.root.title("Python - Cadastro de Cliente")
        self.root.geometry("700x500")
        self.root.configure(background=bg_root)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)
        self.root.resizable(width='true', height='true')
        
    # ===========================================
    # FRAMES [top - bottom]
    def frame_tela(self):
        self.frameTop = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )

        self.frameBottom = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )

        # =======================================
        # INSERÇÃO DE FRAME
        self.frameTop.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frameBottom.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

# ===============================================
# EXECUÇÃO DA JANELA
if __name__ == '__main__':
    App()
    