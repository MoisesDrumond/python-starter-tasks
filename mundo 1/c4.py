import random
número = int(input('Tente adivinhar o número de 1 a 5 que estou pensando:'))
resposta = random.randint(1,5)
print(resposta)
if número == resposta:
    print('Parabéns, voce acertou.')

else:
    print('boo, voce errou.')
