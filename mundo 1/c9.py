a = int(input('Digite o primeiro número:'))
b = int(input('Digite o primeiro número:'))
c = int(input('Digite o primeiro número:'))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor número é: {menor}.')
print(f'O maior número é: {maior}.')
