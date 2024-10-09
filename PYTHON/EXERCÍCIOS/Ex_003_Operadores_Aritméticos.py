# Ordem de Precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

# Adição (+)
a = 8
b = 12
resultado = a + b
print(resultado)  # Saída: 20

# Subtração (-)
a = 25
b = 7
resultado = a - b
print(resultado)  # Saída: 18

# Multiplicação (*)
a = 6
b = 9
resultado = a * b
print(resultado)  # Saída: 54

# Divisão (/)
a = 22
b = 7
resultado = a / b
print(resultado)  # Saída: 3.142857142857143

# Divisão Inteira (//)
a = 22
b = 7
resultado = a // b
print(resultado)  # Saída: 3

# Módulo (%)
a = 22
b = 7
resultado = a % b
print(resultado)  # Saída: 1

# Exponenciação (**)
a = 4
b = 3
resultado = a ** b
print(resultado)  # Saída: 64
print('-' * 12)
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, o produto é {}, a divisão é {}, a divisão inteira é {}, e a potência é {}".format(s, m, d, di, e))
print('-' * 12)