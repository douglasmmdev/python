# 013: Reajuste salarial: Faça um algaritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
print('-' * 12)
salário = float(input('Qual é o salário atual? R$'))
novo = salário + (salário * 15 / 100)
print('Com o salário atual no valor de R${:.2f}, com o aumento de 15% o salário aumentará para R${:.2f}.'.format(salário, novo))
print('-' * 12)