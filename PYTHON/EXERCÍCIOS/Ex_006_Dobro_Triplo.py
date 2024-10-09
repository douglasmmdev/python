# 006 Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
n = int(input("Digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("Analisando o valor {}, o dobro vale {}, o triplo vale {} e a raiz quadrada vale {}".format(n, (n*2), (n*3), (n**(1/2))))