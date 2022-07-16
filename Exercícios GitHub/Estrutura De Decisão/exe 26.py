print('''
                      Até 5 Kg                Acima de 5 Kg
\a File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg --- [ 1 ]
\a Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg --- [ 2 ]
\a Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg --- [ 3 ]
''')
print('')
# linhas
linha = '=' * 61
linha_div = '-' *61

# informações do estabelecimento
nfc = 'NFC - e'
local = 'HIPERMERCADO TABAJARA'
endereco = 'RUA BECO DO CRIME, 219, New Jersey, GOTHAM CITY - EUA'

# título da nota fiscal
titulo = 'Documento Auxiliar da Nota Fiscal'
sub = 'de Consumidor Eletronica'



tipo = int(input("Escolha a Carne \nr: "))
print('')
peso_carne = int(input("Peso Da Carne (Kg) \nr: "))
print('')
unidade_carne = int(input("Quantidade De Carnes \nr: "))
print('')
resposta = int(input("A compra será realizada com cartao Tabajara? \n1p/ SIM - 2p/ NÃO: "))
print('')

if tipo == 1:
    nome_carne = "File Duplo"
    if peso_carne <= 5:
        preco_carne = peso_carne * 4.90
    else:
        preco_carne = peso_carne * 5.80
        
if tipo == 2:
    nome_carne = "Alcatra"
    if peso_carne <= 5:
        preco_carne = peso_carne * 5.90
    else:
        preco_carne = peso_carne * 6.80

if tipo == 3:
    nome_carne = "Picanha"
    if peso_carne <= 5:
        preco_carne = peso_carne * 6.90
    else:
        preco_carne = peso_carne * 7.80

if resposta == 1:
    r = "SIM"
    porcentagem = 5
    desconto_carne = preco_carne - (preco_carne * 5 /100)
    valor_sub = preco_carne - desconto_carne
    valor_liquido = desconto_carne * unidade_carne

else:
    r = "NAO"
    porcentagem = 0
    desconto_carne = 0
    valor_sub = 0
    valor_liquido = preco_carne * unidade_carne
print(linha_div)
print(nfc.center(61))
print(local.center(61))
print(endereco.center(61))
print(linha_div)
print('')
print(linha)
print(titulo.center(61))
print(sub.center(61))
print(linha)
print('')
print(linha)
print('{} {:>49}'.format('ITEM CODIGO', 'DESCRICAO'))
print('{:>8}   {:>6} {:>10} {:>22}'
.format('QTD', 'UN X VL.ITEM(R$)', 'TRIB', 'TOT.ITEM(R$)'))
print(linha)
print('{} {:>45} {}KG'.format('001  61050', nome_carne, peso_carne))
print('{:>6} UN X {:>40} R${:.2f}'.format(unidade_carne, '', preco_carne * unidade_carne))
print('      DESCONTO DE {}% {:>30} -R${:.2f}'.format(porcentagem, '', valor_sub))
print('{:>6} {:>38} R${:.2f}'.format('VALOR LIQUIDO', '', valor_liquido))
print(linha)
print('')
print(linha_div)
print('{} {:>40}'.format('Qtde. Total de Itens', unidade_carne))
print('{} {:>31} R${:.2f}'.format('Valor Total de Itens', '', preco_carne * unidade_carne))
print('{} {:>42} R${:.2f}'.format('Descontos', '', desconto_carne))
print('')
print('')
print('{} {:>38} R${:.2f}'.format('Valor a pagar', '', valor_liquido))
print(linha_div)
print('{} {:>42}'.format('FORMA DE PAGAMENTO', 'VALOR PAGO'))
print('{} {:>42} R${:.2f}'.format('C. DEBITO', '', valor_sub))
print(linha_div)
print('(Lei Federal 12. 741 /2012) Fonte: IBPT')
print('PROCON-RJ: tel. 151')
print('CODECON: tel. 0800 282 7060')
print('End. R da Alfandega, 8 - Centro/RJ')
print('{} {:>42} R${:.2f}'.format('C. DEBITO', '', valor_sub))
print('DOC: 40228922')
print('VIVA SAUDE: 123.456.789-10 ')
print('COD. TRANSIÇÃO: 123456789101112')
print(linha_div)
print('PDV: 214 NSU 37 OPER 1234567 - LAIZA AUT 1234567')
print('SVD01: 11.10.12/14.50.00 LOJA: 1340 COD: 654321')
print(linha_div)
