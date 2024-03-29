from math import factorial
numero = int(input('Digite um numero para calcular seu fatorial:'))
f = factorial(numero)
parador = False
while not parador:
    print(f'O fatorial de {numero} e {f}.')
    parador = True
#ou so o break tbm funciona
#from math import factorial
#numero = int(input('Digite um numero para calcular seu fatorial:'))
#f = factorial(numero)
#while not f == numero:
#    print(f'O fatorial de {numero} e {f}.')
#    break