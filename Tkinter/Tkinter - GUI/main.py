from tkinter import *

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
        root.title("Python GUI")
        root.geometry("800x500")
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

        # =============================================
        # FRAME CENTRO
        self.frame_center = Frame(
            root, bg=light_bg, width=340, height=500
        )

        # =============================================
        # FRAME DIREITO
        self.frame_right = Frame(
            root, bg=light_right, width=230, height=500
        )

        # =============================================
        # PAINEL
        self.frame_left.grid(row=0, column=1)
        self.theme_btn.place(x=0, y=10)

        self.frame_center.grid(row=0, column=2)

        self.frame_right.grid(row=0, column=3)

    # =============================================
    # FUNÇÕES
    def DarkMode(self):
        check = mode_check.get()

        if check == 1:
            self.theme_btn['bg'] = dark_left
            self.theme_btn['fg'] = dark_fg

            self.frame_left['bg'] = dark_left
            self.frame_center['bg'] = dark_bg
            self.frame_right['bg'] = dark_right
        
        else:
            self.theme_btn['bg'] = light_left
            self.theme_btn['fg'] = light_fg

            self.frame_left['bg'] = light_left
            self.frame_center['bg'] = light_bg
            self.frame_right['bg'] = light_right

# =============================================
# ATIVAÇÃO DO ROOT
if __name__ == '__main__':
    app = App(root)
    app.mainloop()