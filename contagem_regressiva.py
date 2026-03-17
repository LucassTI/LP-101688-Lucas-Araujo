import os
import time
os.system("cls || clear")

numero = int(input("Digite um número para a contagem regressiva: "))

for i in range (numero, 0, -1):
    print(i)
    time.sleep(1)