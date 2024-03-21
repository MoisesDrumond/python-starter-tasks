#só para lembrar que as variáveis podem ficar nos ifs e elses
Km = float(input('Quantos é a distancia de sua viagem em Km?'))
passagem = Km * 0.50
passagem2 = Km * 0.45
print(f'Voce esta prestes a começar uma viagem de: {Km}Km.')
if Km <= 200:
    passagem = Km * 0.50
    print(f'O preço da sua passagem é: R${passagem:.2f}.')
else:
    passagem2 = Km * 0.45
    print(f'O preço da sua passagem é: R${passagem2:.2f}.')
