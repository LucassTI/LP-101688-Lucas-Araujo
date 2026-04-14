import os
from datetime import date

os.system("cls")

def ida (a):
    ano = date.today().year
    idade = ano - a
    return idade

n0 = int(input("Digite o Ano de Nascimento: "))

ida(n0)
idade = ida(a=n0)

print("\n= Resultado =")
print(f"Idade: {idade}")
print(f"Ano de Nascimento: {n0}")