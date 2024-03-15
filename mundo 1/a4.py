dias = int(input('Quantos dias o carro foi alugado:'))
km = float(input('Quantos km o carro percorreu durante o aluguel do carro:'))
preço = (dias * 60) + (km * 0.15)
print(f'O valor do aluguel do carro é:{preço}.')
