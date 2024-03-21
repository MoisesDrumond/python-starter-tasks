Km = float(input('Quantos é a distancia de sua viagem em Km?'))
print(f'Voce esta prestes a começar uma viagem de: {Km}Km.')
if Km <= 200:
    passagem = Km * 0.50
    print(f'O preço da sua passagem é: R${passagem:.2f}.')
else:
    passagem = Km * 0.45
    print(f'O preço da sua passagem é: 200R${passagem:.2f}.')
