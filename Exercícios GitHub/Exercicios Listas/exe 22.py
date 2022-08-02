'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira 
tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando 
o estado de cada um deles, para verificar o que se pode aproveitar deles. 
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito: 

	* necessita da esfera; 
	* necessita de limpeza;
	* necessita troca do cabo ou conector;
	* quebrado ou inutilizado

Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório: 

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

# === DADOS ===
defeitos_ = ['Necessita de Esfera', 'Necessita de limpeza', 'Troca de Cabo ou Conector',
'Quberado ou Inutilizado']

# === FUNÇÃO DEF-CLEAN ===
def clean():
	print('\n' *10)


# ---
num_mouses = int(input('Quanto mouses com defeitos? \nr: '))
defeitos = 4 * [0]
print('-' *30)
print('')

for idx in range(num_mouses):
	validacao = True
	while validacao:
		defeito = int(input('\a Código do problema do mouse \nr: '))
		print('')

		if defeito == 1 or defeito == 2 or defeito == 3 or defeito == 4:
			validacao = False
		else:
			print('Número Inválido! Tente novamente (escolhendo entre: 1, 2, 3 ou 4)!')

	defeitos[defeito-1] = defeitos[defeito-1] + 1
print('-' *30)
clean()
print('-=' *30)
print('Quantidade de mouses: {}'.format(num_mouses))
print('')
print('Situação   Quantidade   Percentual')
for idx in range(len(defeitos_)):
	print('\a {:<2} - {} defeitos - {}%'
		.rjust(30).format(defeitos[idx], defeitos[idx], (defeitos[idx]*100/num_mouses)))
print('-=' *30)
