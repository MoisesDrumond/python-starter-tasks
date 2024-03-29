def soma(* valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'Somando valores {valores} temos {s}')


soma(5, 3)
soma(2, 9, 4)
