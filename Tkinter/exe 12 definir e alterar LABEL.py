from tkinter import *

janela = Tk()
janela.title("DEFINIR E ALTERAR PROPRIEDADES DE UM LABEL")
janela.geometry("500x500")

label_l = Label(
    janela,
    text="Frase Teste",
    font=('Arial 20'),
    bd=1,
    relief="solid",
)
label_l.pack()

label_k = Label(janela)
label_k['text'] = "teste da label k"
label_k['font'] = "Times, 30"
label_k['bd'] = 1
label_k['relief'] = "solid"
label_k.pack()

# === PRINTAR NO CONSOLE ===
print('\033[1;34mChaves da label L:\033[m')
for item in label_l.keys():
    print(f'{item}: {label_l[item]}')
print('')
print('\033[1;32mChaves da label K:\033[m')
for item in label_k.keys():
    print(f'{item}: {label_k[item]}')
print('')
print(f'Label L: {label_l["font"]}')
print(f'Label K: {label_l["font"]}')


janela.mainloop()