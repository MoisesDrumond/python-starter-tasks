sumage = 0
mediaage = 0
older = 0
oldname = ''
totwoman20 = 0
for i in range(1, 5):
    print(f'===== {i} Pessoa =====')
    name = str(input('Nome:')).strip()
    age = int(input('Idade:'))
    sex = str(input('Sexo [M/F]:')).strip()
    sumage += age
    if i == 1 and sex in 'Mm':
        older = age
        oldname = name
    if sex in 'Mm' and age > older:
        older = age
        oldname = name
    if sex in 'Ff' and age < 20:
        totwoman20 = totwoman20 + 1
mediaage = sumage / 4
print(f'A media de idade do grupo e de {mediaage} anos.')
print(f'O homem mais velho tem {older} anos e se chama {oldname}.')
print(f'Ao todo sao {totwoman20} mulheres com mais de 20 anos.')
