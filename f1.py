sum = 0
counter = 0
for i in range(3, 500, 3):
    if i % 3 == 0:
        sum += i
        counter = counter + 1
print(f'A soma de todos os {counter} valores solicitados e {sum}.')
