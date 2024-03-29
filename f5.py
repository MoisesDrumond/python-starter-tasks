first = int(input('Primeiro termo:'))
reason = int(input('Razao:'))
tenth = first + (10 -1) * reason
for i in range(first, tenth + reason, reason):
    print(i, end=' > ')
print('ACABOU')
