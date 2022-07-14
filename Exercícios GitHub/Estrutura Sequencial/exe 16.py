Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos). 

print('-=' *30)
print('   SIMULADOR DE DOWNLOAD   ')
print('-=' *30)
print('')
arq = float(input('>>> Tamanho do arquivo (MB) \nr: '))
print('')
speed = float(input('>>> Velocidade de Internet (MBps) \nr: '))
print('')
download = (arq / speed) * 60
print('O tempo estimado para download é de: {:.0f} min'.format(download))
hora = download / 60
print('>>> Resultando em {:.0f} Horas'.format(hora))
