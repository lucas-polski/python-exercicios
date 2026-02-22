from random import randint as chute
from time import sleep
pc = chute(0,5) #Faz o computador 'pensar'
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
usu = int(input("Em que número eu pensei? ")) #Jogador tenta advinhar
print('PROCESSANDO....')
sleep(2)
print('PROCESSANDO....')
sleep(1)
if pc == usu:
    print("PARABENS VOCE CONSEGUIU ME VENCER!")
else:
    print(f"GANHEI! Eu pensei no numero {pc} e nao no {usu}!")
print('-=-' * 20)
sair = input('digite algo para fechar')