"""n = 1
while n != 0:
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} nao e par!')
print('Fim!')"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Voce digitou {par} numeros pares e {impar} numeros impares!')
