name = str(input('Qual é o seu nome?')).strip()
name = name.title()
if name == 'Gustavo':
    print('Que nome lindo voce tem.')
elif name == 'Danilo' or name == 'Caua':
    print('Voce e xara do meu melhor amigo!')
elif name in 'Ana Johnny Gabriel':
    #elif nome in 'Ana' or nome in 'Johnny':
    print('Esses nomes sao bem representativos.')
else:
    print(f'Seu nome é bem normal, {name}.')
print(f'Tenha um bom dia, {name}!')
