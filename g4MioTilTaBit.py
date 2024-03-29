from random import randint
from time import sleep
n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
soma = """\033[1;31m[1]\033[m somar"""
multiplicar = 0
maior = """\033[1;31m[3] \033[mmaior"""
novos = """\033[1;31m[4] \033[mnovos numeros"""
sair = """\033[1;31m[5] \033[msair do programa"""
acao = int(input(f'{soma}\n'
'\033[1;31m[2] \033[mmultiplicar\n'
'\033[1;31m[3] \033[mmaior\n'
'\033[1;31m[4] \033[mnovos numeros\n'
'\033[1;31m[5] \033[msair do programa\n'
'Escolha uma das alternativas acima:'))
acabar = False
while not acabar:
    if acao == 1:
        acabar = True
        print(n1 + n2)
    if acao == 2:
        acabar = True
        print(n1 * n2)
    if acao == 3:
        if n1 > n2:
            acabar = True
            print(f'O numero {n1} e maior!')
        if n2 > n1:
            print(f'O numero {n2} e maior!')
        else:
            print(f'Os numeros {n1} e {n2} se equivalem!')
    if acao == 4:
        print(randint(0,10))
        print(randint(0, 10))
        break
    if acao == 5:
        print('Finalizando...')
        sleep(1)
        print('Fim do programa! Volte sempre!')
        break
    else:
        print('\033[1;31mOpcao invalida!\033[m')
        break
