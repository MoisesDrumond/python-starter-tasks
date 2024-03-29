start = int(input('Inicio:'))
end = int(input('Fim:'))
skip = int(input('Passo:'))
for i in range(start, end+1, skip):
    print(i)
