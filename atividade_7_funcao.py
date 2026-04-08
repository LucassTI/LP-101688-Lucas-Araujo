import os
os.system("cls")

def inf (a):
    if a <= 100:
        resultado = a * 1.10
    else:
        resultado = a * 1.20
    
    return resultado


print("= Solicitando Dados =")
n0 = int(input("Digite um valor para ser inflacionado: "))
inf(n0)
resultado = inf(a=n0)

print("\n= Resultado =")
print(f"Resultado da inflação: {resultado:.1f}")