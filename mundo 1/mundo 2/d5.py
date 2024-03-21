house = float(input('Qual e o valor da sua casa?'))
salary = float(input('Qual e o valor do seu salario?'))
age = int(input('Em quantos anos voce pretende pagar a casa?'))
installment = house / (age * 12)
minimum = (salary * 30) / 100
print(f'Para pagar uma casa de R${house:.2f} em {age} anos', end='')
print(f' a prestacao será de: {installment:.2f}.')
if installment <= minimum:
    print('Seu emprestimo foi aceito.')
else:
    print('Seu emprestimo nao foi aceito.')
