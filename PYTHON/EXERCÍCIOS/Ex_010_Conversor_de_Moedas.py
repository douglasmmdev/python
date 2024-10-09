# 010 Quanto dinheiro você tem na carteira. Conversor de real para dolar.
print('-' * 12)
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.47
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('-' * 12)