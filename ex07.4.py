def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2,5,7)
contador(7, 4, 3)
contador(5, 9, 2)
