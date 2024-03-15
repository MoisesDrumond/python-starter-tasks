import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print(f'A raiz quadrada do número {num} é: {raiz:.3f}.')
print(f'A raiz quadrada do número {num} arredondada para cima é: {math.ceil(raiz)}.')
print(f'A raiz quadrada do número {num} arredondada para baixo é: {math.floor(raiz)}')
