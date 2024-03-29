m = 'M'
f = 'F'
sexo = 0
while m != sexo and f != sexo:
    sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
    if m == sexo:
        print('Sexo masculino registrado com sucesso!')
    if f == sexo:
        print('Sexo feminino registrado com sucesso!')
    if sexo != m and f:
        str(input('Dados invalidos. Por favor informe seu sexo:'))
