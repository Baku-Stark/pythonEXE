from num2words import num2words

num = int(input('Escolha um número \nr: '))
num_convert = num2words(num)
print('')
print(f'--> {str(num_convert).capitalize()}')