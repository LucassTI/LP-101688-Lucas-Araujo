import os

import time
os.system("cls || clear")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / QUANTIDADE_NOTAS
print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")
