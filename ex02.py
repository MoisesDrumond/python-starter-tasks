from random import randint
def retornar_numero_aleatorio(x, y):
    return randint(x, y)
retorno_da_funcao = retornar_numero_aleatorio(0, 10)
print(retorno_da_funcao)