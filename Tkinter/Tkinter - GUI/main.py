from tkinter import *
from tkinter.ttk import Treeview

# ----------------------------------------
# IMPORTAÇÃO DA "view.py"
from view import *

# =============================================
# CORES

# --- DARK MODE
dark_left = "#252525"
dark_bg = "#2F3136"
dark_right = "#252525"
dark_fg = "#f0f8ff"

# --- LIGHT MODE
light_left = "#ADAFB2"
light_bg = "#f0f8ff"
light_right = "#ADAFB2"
light_fg = "#111111"

# =============================================
# APLICAÇÃO
root = Tk()
mode_check = IntVar()

class App(Frame):
    def __init__(self, master):
        super().__init__()
        # =============================================
        # WIDGET
        root.title("Python - Lista Telefônica")
        root.geometry("570x500")
        root.iconbitmap("_img/pc.ico")
        root.resizable(width='false', height='false')

        # =============================================
        # FRAME ESQUERDO
        self.frame_left = Frame(
            root, bg=light_left, width=230, height=500
        )

        self.theme_btn = Checkbutton(
            root, text="Dark Mode", font=('Helvetica 12 bold'),
            bg=light_left, fg=light_fg, variable=mode_check,
            command=self.DarkMode
        )

        self.label_nome = Label(
            root, text="Nome*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_nome = Entry(root)

        self.label_ddd = Label(
            root, text="DDD*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_ddd = Entry(root)

        self.label_telefone = Label(
            root, text="Telefone*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_telefone = Entry(root)

        # =============================================
        # FRAME CENTRO
        self.frame_center = Frame(
            root, bg=light_bg, width=340, height=500
        )

        self.btn_insert = Button(
            root, text="Inserir", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge'
        )

        self.btn_update = Button(
            root, text="Atualizar", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge'
        )

        self.btn_delete = Button(
            root, text="Deletar", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge'
        )

        # =============================================
        # PAINEL
        self.frame_left.grid(row=0, column=1)
        self.theme_btn.place(x=0, y=10)
        self.label_nome.place(x=20, y=50)
        self.insert_nome.place(x=20, y=70)
        # -----------------
        self.label_ddd.place(x=20, y=100)
        self.insert_ddd.place(x=20, y=120)
        # -----------------
        self.label_telefone.place(x=20, y=150)
        self.insert_telefone.place(x=20, y=170)

        self.frame_center.grid(row=0, column=2)
        self.btn_insert.place(x=235, y=250)
        self.btn_update.place(x=350, y=250)
        self.btn_delete.place(x=480, y=250)

        self.show()

    # =============================================
    # FUNÇÕES
    def DarkMode(self):
        check = mode_check.get()

        if check == 1:
            self.theme_btn['bg'] = dark_left
            self.theme_btn['fg'] = dark_fg

            self.frame_left['bg'] = dark_left
            self.label_nome['bg'] = dark_left
            self.label_nome['fg'] = dark_fg
            self.label_ddd['bg'] = dark_left
            self.label_ddd['fg'] = dark_fg
            self.label_telefone['bg'] = dark_left
            self.label_telefone['fg'] = dark_fg

            self.frame_center['bg'] = dark_bg
            self.btn_insert['bg'] = dark_left
            self.btn_insert['fg'] = dark_fg
            self.btn_update['bg'] = dark_left
            self.btn_update['fg'] = dark_fg
            self.btn_delete['bg'] = dark_left
            self.btn_delete['fg'] = dark_fg
        
        else:
            self.theme_btn['bg'] = light_left
            self.theme_btn['fg'] = light_fg

            self.frame_left['bg'] = light_left
            self.label_nome['bg'] = light_left
            self.label_nome['fg'] = light_fg
            self.label_ddd['bg'] = light_left
            self.label_ddd['fg'] = light_fg
            self.label_telefone['bg'] = light_left
            self.label_telefone['fg'] = light_fg

            self.frame_center['bg'] = light_bg
            self.btn_insert['bg'] = light_left
            self.btn_insert['fg'] = light_fg
            self.btn_update['bg'] = light_left
            self.btn_update['fg'] = light_fg
            self.btn_delete['bg'] = light_left
            self.btn_delete['fg'] = light_fg

    global list_tel

    def show(self):
        global list_tel
        lista = acess()
        
        tabela_head = ['ID', 'Nome', 'DDD', 'Telefone']
        
        hd = ["nw", "nw", "nw", "nw"]
        h = [30, 100, 40, 170]
        n = 0

        list_tel = Treeview(
            root, selectmode="extended", columns=tabela_head, show="headings"
        )

        list_tel.place(x=230, y=0)

        for col in tabela_head:
            list_tel.heading(col, text=col.title(), anchor=CENTER)
            list_tel.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            list_tel.insert('', 'end', values=item)

# =============================================
# ATIVAÇÃO DO ROOT
if __name__ == '__main__':
    app = App(root)
    app.master.mainloop()