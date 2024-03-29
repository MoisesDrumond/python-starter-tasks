sum = 0
count = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} numero inteiro:'))
    if num % 2 == 0:
        sum += num
        count += 1
        pair = 'PARES'
        numbers = 'numeros'
    if count == 1:
        pair = 'PAR'
        numbers = 'numero'
    if count == 0:
        pair = 'PARES'
        numbers = 'numeros'
print(f'Voce informou {count} {numbers} {pair} e a SOMA foi {sum}.')
