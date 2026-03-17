import os

import time
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 5
for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / QUANTIDADE_NOTAS
print(f"Média: {media}")
