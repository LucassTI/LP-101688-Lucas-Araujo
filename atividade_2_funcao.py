import os
os.system("cls")


def sistema(numero):
    pares = 0
    impares = 0
    if n1 % 2 == 0:
        pares += 1
        print(f"O número {n1} é par")
    else:
        print(f"O número {n1} é ímpar")


n1 = int(input("Digite um número: "))

sistema(numero= n1)