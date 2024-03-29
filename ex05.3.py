# Informa se um número é par
# Retorna True se é par e False se é ímpar
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
# Separa elementos da lista entre pares e ímpares
def separaPorParidade(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if eh_par(numero):
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
# Utilizando a função
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares =  separaPorParidade(nums)
print(pares)
print(impares)