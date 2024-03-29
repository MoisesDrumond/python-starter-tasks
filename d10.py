from datetime import date
byear = int(input('Em que ano voce nasceu?'))
actual = date.today().year
age = actual - byear
print(f'Voce, atleta nasceu no ano de {byear} e tem {age} anos.')
if age <= 9 and age >= 0:
    print('Sua categoria e: MIRIM.')
elif age <= 14 and age > 9:
    print('Sua categoria e: INFANTIL.')
elif age <= 19 and age > 14:
    print('Sua categoria e: JUNIOR.')
elif age <= 25 and age > 19:
    print('Sua categoria e: SENIOR.')
elif age > 25:
    print('Sua categoria e MASTER.')
else:
    print('Esta idade nao existe e portanto nao condiz com categoria alguma.')
