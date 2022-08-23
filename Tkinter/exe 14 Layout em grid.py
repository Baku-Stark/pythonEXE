from tkinter import *


janela = Tk()
janela.title("INTRODUÇÃO AO LAYOUT EM GRID")
janela.geometry("500x500")

label_l = Label(
    janela, text="Label 1", font=('Arial 20'),
    bg="red")
label_l.grid(row=0, column=0)

label_k = Label(
    janela, text="Label 1", font=('Arial 20'),
    bg="green")
label_k.grid(row=0, column=1)

label_j = Label(
    janela, text="Label 3", font=('Arial 20'),
    bg="blue")
label_j.grid(row=0, column=2)

btn_l = Button(janela, text="Click 1")
btn_l.grid(row=1, column=0)

btn_k = Button(janela, text="Click 2")
btn_k.grid(row=1, column=1)

btn_j = Button(janela, text="Click 3")
btn_j.grid(row=1, column=2)

# =====================================
res = str(input('Deseja ver as informações das Labels? \nr: ')).upper().strip()
print('')
if res == "SIM":
    print('\033[1;31mChaves da label L:\033[m')
    for info in label_l.keys():
        print(f'{info} : {label_l[info]}')
    print('-=' *30)
    print('\033[1;32mChaves da label K:\033[m')
    for info in label_k.keys():
        print(f'{info} : {label_k[info]}')
    print('-=' *30)
    print('\033[1;34mCahves da label J:\033[m')
    for info in label_j.keys():
        print(f'{info} : {label_j[info]}')

else:
    print('As informções não serão mostradas.')
# =====================================

janela.mainloop()