n = int(input('Digite um numero e direi se ele e primo ou nao:'))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end='')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes.')
if tot == 2:
    print('E por isso ele e PRIMO!')
else:
    print('E por isso ele nao e PRIMO!')
