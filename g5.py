from math import factorial
numero = int(input('Digite um numero:'))
f = factorial(numero)
for i in range(1, numero, 1):
        f = f
print(f'O fatorial de {numero} e: {f}.')
