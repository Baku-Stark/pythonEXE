>>>  - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/usando-modulos-do-python/modulos/exercicio-21-tocando-um-mp3/
--------------------------------------------------------

Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio 
de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('gnr.mp3')
pygame.mixer.music.play()
pygame.event.wait()
--------------------------------------------------------

Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e 
mostre:

– O nome com todas as letras maiúsculas e minúsculas.
print('Seu nome em MAIÚSCULO fica: {}.'.format(nome.upper()))
print('Seu nome em MINÚSCULO fica: {}.'.format(nome.lower()))
– Quantas letras ao todo (sem considerar espaços).
nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
– Quantas letras tem o primeiro nome.
print('Seu PRIMEIRO nome possui {} letras.'.format(nome.find(' ')))

# 'Wallace De Freitas Moura Dos Santos'
nome = str(input('Digite seu nome completo:')).strip()
print('')
print('Analisando o resultado...')
print('')

print('Seu nome em MAIÚSCULO fica: {}.'.format(nome.upper()))
print('')

print('Seu nome em MINÚSCULO fica: {}.'.format(nome.lower()))
print('')

print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('')

print('Seu PRIMEIRO nome possui {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu PRIMEIRO nome é {}.'.format(separa[0]))
--------------------------------------------------------

Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.

nint = int(input('Digite um valor: '))
n = str(nint)
print('')
print('O número escolhido foi: {}'.format(nint))
print('-' *20)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
print('-' *20)
--------------------------------------------------------

Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se 
ela começa ou não com o nome “SANTO”.

city = str(input('Qual a sua cidade: ')).capitalize().strip()
print(city[:5] == 'Santo')
--------------------------------------------------------