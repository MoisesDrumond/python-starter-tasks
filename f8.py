maior = 0
menor = 0
for i in range(1, 6):
    weight = float(input(f'Digite o peso da {i} pessoa:'))
    if i == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print(f'O maior peso lido foi {maior}Kg.')
print(f'O menor peso lido foi {menor}Kg.')


