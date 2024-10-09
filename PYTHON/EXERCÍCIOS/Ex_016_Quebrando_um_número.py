# Quebrando um número: Crie um programa que leia um número Real qualquer pelo tecldo e mostre na tela a sua porção inteira.
import math
print('-' * 15)
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))