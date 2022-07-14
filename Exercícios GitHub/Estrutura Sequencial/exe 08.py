Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('>>> Salário por hora: R$'))
horas_trab = int(input('>>> Horas trabalhadas: '))
print('')
print('-=' *30)
salario = salario_hora * horas_trab
print('O salário no final do mês é de: R${:.2f}'.format(salario))
print('-=' *30)
