grade1 = float(input('Digite sua primeira nota:'))
grade2 = float(input('Digite sua segunda nota:'))
average = (grade1 + grade2)/2
print(f'Tirando {grade1:.1f} e {grade2:.1f}, a media do aluno e: {average:.1f}')
if average < 5.0 and average >= 0:
    print('REPROVADO!')
elif average >= 5.0 and average <= 6.9:
    print('RECUPERACAO!')
elif average >= 7.0 and average <= 10:
    print('APROVADO!')
else:
    print('Essa media e INVALIDA!')
#if 7 > average >= 5: outra forma
