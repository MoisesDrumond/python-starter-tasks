from time import sleep
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor'))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual e a sua opcao?'))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} e: {soma}!')
    if opcao == 2:
        produto = n1 * n2
        print(f'A multiplicacao entre {n1} e {n2} e: {produto}!')
    if opcao == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o {maior} e maior!')
    if opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro numero:'))
        n2 = int(input('Segundo numero'))
    if opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente!')
    print('=-='* 10)
    sleep(2)
print('Fim do programa! Volte sempre!')