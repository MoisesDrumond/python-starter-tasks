from random import choice
a1 = input('Diga o nome do primeiro aluno:')
a2 = input('Diga o nome do segundo aluno:')
a3 = input('Diga o nome do terceiro aluno:')
a4 = input('Diga o nome do quarto aluno:')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(f'O aluno sorteado é: {sorteio}.')
