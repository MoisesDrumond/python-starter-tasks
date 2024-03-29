num = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
if num > num2:
    print(f'O {num} e maior do que o {num2}.')
elif num2 > num:
    print(f'O {num2} e maior do que o {num}.')
else:
    print('Nao existe numero maior, os dois sao iguais.')
