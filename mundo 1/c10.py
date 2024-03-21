salario = float(input('Diga o seu salário:'))

if salario > 1250:
    salario = (salario * 10)/100
else:
    salario = (salario * 15)/100
print(f'O valor do seu aumento é: {salario}.')

