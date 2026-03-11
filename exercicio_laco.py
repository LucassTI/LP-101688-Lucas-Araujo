import os
import time

# os.system("cls || clear")

# #  De  1 até 20 números impares
# for i in range(1,21,2 ):
#     print(i)
#     # Espera 2 segundos
#     time.sleep(0.6)


numero = int(input("Escreva um número para fazer contagem regressiva: "))

for i in range (numero , 0, -1):
    print(i)
    time.sleep(1)