num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao:)
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
option = int(input('Sua opcao: '))
if option == 1:
    print(f'{num} convertido para BINARIO e igual a {bin(num)[2:]}.')
elif option == 2:
    print(f'{num} convertido para OCTAL e igual a {oct(num)[2:]}.')
elif option == 3:
    print(f'{num} convertido para HEXADECIMAL e igual a {hex(num)[2:]}')
else:
    print('Opcao invalida. Tente novamente.')
