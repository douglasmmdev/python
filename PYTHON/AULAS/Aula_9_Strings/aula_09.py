frase = 'Curso em Vídeo Python'
print(frase)

#FATIAMENTO
print(frase[3:13])
print(frase[3:13:2])
#CORTAR LETRAS
print(frase.count('o'))
#CONTAR QNTD DE LETRAS
print(len(frase))
#TROCAR PALAVRA
print(frase.replace('Python', 'em Android'))
#VERIFICAR SE PALAVRA ESTÁ NA FRASE
print('em' in frase)
#VERIFICAR POSIÇÃO DA PALAVRA NA FRASE
print(frase.find('Py'))
#DEIXAR TUDO EM CAIXA BAIXA(MINÚSCULO)
print(frase.lower())
#DEIXAR TUDO EM CAIXA ALTA(MAIÚSCULO)
print(frase.upper())
#DIVIDIR FRASE
print(frase.split())