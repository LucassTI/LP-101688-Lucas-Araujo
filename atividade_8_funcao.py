import os

os.system("cls")

def ida (a):
    idade = a - 2026
    return idade

n0 = int(input("Digite o Ano de Nascimento: "))

ida(n0)
idade = ida(a=n0)

print("n\= Resultado =")
print(f"Idade:{idade}")