Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
mostre a temperatura em graus Celsius.  

print('--- Fahrenheit > Celsius ---')
### ([número] °F − 32) × 5/9 = °C
temp = float(input('Registre a temperatura em Fahrenheit (°F): '))
print('')
print('-=' *30)
print('({} °F − 32) × 5/9 = °C'.format(temp))
celsius = (temp - 32) * 5/9
print('')
print('Fahrenheit >>> Celsius: {:.1f}°C'.format(celsius))
print('-=' *30)

Faça um Programa que peça a temperatura em graus Celsius, transforme e 
mostre em graus Fahrenheit. 

print('--- Celsius > Fahrenheit ---')
### ([número] °C × 9/5) + 32 = 32 °F
temp = float(input('Registre a temperatura em Celsius (°C): '))
print('')
print('-=' *30)
print('({} °C × 9/5) + 32 = 32 °F'.format(temp))
fahrenheit = (temp * 9/5) + 32
print('')
print('Celsius >>> Fahrenheit: {}°F'.format(fahrenheit))
print('-=' *30)
