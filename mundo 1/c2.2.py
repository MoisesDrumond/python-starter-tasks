n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
indiceultimonome = len(nome)-1
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nome[0]} e seu último nome é: {nome[indiceultimonome]}.')
