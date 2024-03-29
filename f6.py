phrase = str(input('Diga uma frase ou palavra:')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = ''
for i in range(len(together) - 1, -1, -1):
    reverse = reverse + together[i]
print(f'O inverso de \033[1;34m{together}\033[m e \033[1;35m{reverse}\033[m')
if reverse == together:
    print('\033[4;32mTemos um PALINDROMO!\033[m')
else:
    print('\033[1;31mNAO e um PALINDROMO!\033[m')
