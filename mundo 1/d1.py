print('-=-'*20)
print('Ansalisador de Triangulos')
print('-=-'*20)
line1 = float(input('Digite sua primeira reta:'))
line2 = float(input('Digite sua segunda reta:'))
line3 = float(input('Digite sua terceira reta:'))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('A soma de suas retas podem SIM formar um triangulo!')
else:
    print('A soma de suas retas NÃO podem formar um triangulo!')
