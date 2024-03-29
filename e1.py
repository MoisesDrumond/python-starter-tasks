print('-=-'*20)
print('Ansalisador de Triangulos')
print('-=-'*20)
line1 = float(input('Digite sua primeira reta:'))
line2 = float(input('Digite sua segunda reta:'))
line3 = float(input('Digite sua terceira reta:'))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('A soma de suas retas podem SIM formar um triangulo!')
    if line1 == line2 == line3:
        print('O triangulo e equilatero.')
    elif line1 == line2 or line2 == line3 or line3 == line1:
        print('O triangulo e isosceles.')
    elif line1 != line2 != line3 != line1:#or else tbm funciona
        print('O triangulo e escaleno.')
else:
    print('A soma das retas nao podem formar um triangulo!')
#if line1 == line2 and line2 == line3:#another way
#elif line1 != line2 and line2 != line3 and line1 != line3:#another way
