from datetime import date
actual = date.today().year
byear = int(input('Em que ano voce nasceu?'))
age = actual - byear
if age > 18:
    passed = age - 18
    print(f'Voce ja tem mais de 18 anos. O prazo para voce se alistar expirou há {passed} anos.')
    year = actual - passed
    print(f'O seu alistamento militar foi no ano de: {year}.')
elif age == 18:
    print('Voce deve se alistar no exercito ainda nesse ano.')
elif age < 18:
    coming = 18 - age
    print(f'Voce ainda nao tem 18 anos. Ainda faltam {coming} anos para o seu alistamento militar.')
    year = actual + coming
    print(f'O seu alistamento militar vai acontecer no ano de: {year}')
