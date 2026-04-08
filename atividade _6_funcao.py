import os

os.system("cls")

print("= Solicitando Dados =")
n0 = int(input("Valor para ser transformado: "))

def cent (a):
    centimetros = a * 100
    print(f"O valor em centímetros: {centimetros} ")


print("\n= Resultado =")
cent(n0)