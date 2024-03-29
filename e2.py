height = float(input('Qual e a sua altura?'))
weight = float(input('Qual e o seu peso?'))
imc = weight / (height ** 2)
print(f'Seu imc e de {imc:.1f}.')
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Voce esta com o peso ideal!')
elif imc > 25 and imc <= 30:
    print('Voce esta com sobrepeso!')
elif imc > 30 and imc < 40:
    print('Voce esta com obesidade!')
else:
    print('Voce esta com obesidade morbida!')
#elif 18.5 <= imc <= 25:
