#Escreva um programa que faça o ocmputador "pensar" em um número inteiro entre 0 e 5. E peça para o usuário tentar adivinha qual o computador escolheu
from random import randint
from time import sleep 
computador =  randint(0,5) #Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você venceu!')
else:
    print('Ganhei! Errou vacilão... pensei no nº{}!'.format(computador))