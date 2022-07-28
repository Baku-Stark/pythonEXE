'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação 
    sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 
    2 questões ela deve ser classificada como "Suspeita", 
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
    Caso contrário, ele será classificado como "Inocente". 
'''

# ----- CONTAGEM -----
count = 0

# ----- DICIONÁRIO -----
dic = {
	"Pergunta1": "Telefonou para a vítima?",
	"Pergunta2": "Esteve no local do crime?",
	"Pergunta3": "Mora perto da vítima?",
	"Pergunta4": "Devia para a vítima?",
	"Pergunta5": "Já trabalhou com a vítima?"
}

# ---------------------
for p in xrange(1, 6):
	print(dic["Pergunta"+ str(p)])
	res = str(input('r: ')).upper().strip()
	if res == "SIM":
		count += 1
	print('')

print('-=' *30)
print('Resultado Do(a) Suspeito(a)')
situation = ""
print('')

if count <= 1:
	situation = "INOCENTE"

elif count == 2:
	situation = "SUSPEITA"

elif count == 3 or count == 4:
	situation = "CÚMPLICE"

elif count == 5:
	situation = "ASSASSINO"

print('\a A pessoa suspeita é: {}'.format(situation))
print('-=' *30)
