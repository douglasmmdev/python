# 012: Calculando Descontos: Faça um algaritmo que leia o preço de um produto e mostre seu novo preço com 5$ de desconto.
print('-' * 12)
preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com de desconto de 5% vai custar R${:.2f}'.format(preço, novo))
print('-' * 12)