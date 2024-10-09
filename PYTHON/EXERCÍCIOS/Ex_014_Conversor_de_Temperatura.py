# 014: Conversor de temperatura: Escreva um programa que converta uma temperatura de ºC para ºF.
print('-' * 12)
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF.'.format(c, f))
print('-' * 12)