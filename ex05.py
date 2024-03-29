# Informa a paridade de um número passado como argumento
def paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
# Utilizando a função
num = 5
print("O numero {} é {}".format(num, paridade(num)))