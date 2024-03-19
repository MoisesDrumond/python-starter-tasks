nome = str(input('Digite seu nome completo:')).strip()
pri = nome.split()
ult = nome.rsplit()
print(f'Seu primeiro nome é: {pri[0]} e seu último nome é: {ult[-1]}.')

