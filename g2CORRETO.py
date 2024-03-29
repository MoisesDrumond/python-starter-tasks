sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Diga seu sexo novamente:'))
print(f'Sexo {sexo} registrado com sucesso.')
