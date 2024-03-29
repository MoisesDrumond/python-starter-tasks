def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} e de {a}m2.')

print('Controle de Terrenos\n', ('-'*20))
l = float(input(('Altura [m]:')))
c = float(input('Largura [m] :'))
area(l, c)
