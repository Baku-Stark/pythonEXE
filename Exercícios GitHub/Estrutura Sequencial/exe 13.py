Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo

nome = str(input('Nome Do Usuário: '))
print('')
salario_hora = float(input('Ganho Por Hora R$'))
print('')
trab_hora = int(input('Horas Trabalhadas (mês) \nr:'))
salario = salario_hora * trab_hora
print('')
print('-=' *30)
print('DADOS')
print('')
print('> {}'.format(nome))
print('> Salário: R${:.2f}'.format(salario))
print('---')
ir = salario - (salario * 11/100)
print('> IMPOSTO (11%): R${:.2f}'.format(ir))
print('---')
inss = ir - (ir * 8/100)
print('> INSS (8%): R${:.2f}'.format(inss))
print('---')
sind = inss - (inss * 5/100)
print('> Sindicato (5%): R${:.2f}'.format(sind))
print('---')
salario_liq = sind
print('>>> Salário Liquido: R${:.2f}'.format(salario_liq))
print('-=' *30)
