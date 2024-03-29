from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)
print("""Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
player = int(input('Qual e a sua jogada?'))
sleep(.8)
print("""JO""")
sleep(.8)
print("""KEN""")
sleep(.8)
print("""PO!!!""")
print('\033[1;31m-=\033[m'*13)
print(f'Computador jogou {itens[computer]}.')
print(f'Jogador jogou {itens[player]}')
print('\033[1;31m-=\033[m'*13)
if computer == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')
if computer == 1:
    if player == 1:
        print('EMPATE')
    elif player == 0:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')
if computer == 2:
    if player == 2:
        print('EMPATE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 0:
        print('JOGADOR VENCE')
    else:
        print('\033[4;31mJOGADA INVALIDA!\033[m')
#else nao funciona e fds
