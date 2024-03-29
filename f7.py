from datetime import date
totold = 0
totyoung = 0
for people in range(1, 7+1):
    birthdate = int(input(f'Digite o ano em que a {people} pessoa nasceu:'))
    age = date.today().year - birthdate
    if age >= 18:
        totold += 1
    if age < 18:
        totyoung += 1
print(f'Ao todo tivemos {totyoung} pessoas menores e {totold} pessoas maiores.')
