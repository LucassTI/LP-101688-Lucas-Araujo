import os
os.system('cls')

numeros = []
NUMERO = 6
pares  = 0
impares = 0


for i in range(NUMERO):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    
print(f"\nNúmeros Pares: {pares}")
print(f"Números Impares: {impares}")