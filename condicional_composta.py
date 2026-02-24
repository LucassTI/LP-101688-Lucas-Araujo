import os

#Limpa o Terminal
os.system("cls || clear")

idade = int(input("Digite sua idade: "))

# Condicional simples.
if idade < 18:
    print("Acesso negado.")
else:
    print("Acesso liberado.")
    
print("Programa encerrado.")

