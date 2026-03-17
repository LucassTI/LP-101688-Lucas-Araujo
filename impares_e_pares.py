import os

import time
os.system("cls || clear")

pares = 0
impares = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")