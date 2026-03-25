import os
os.system('cls')

numeros = []
NUMERO = 5



for i in range(NUMERO):
    numero = int(input("Digite um número: "))
    
    numeros.append(numero)
    
    maior_numero = max(numeros)
    menor_numero = min(numeros)
    
    
print(f"\nMaior número: {maior_numero}")
print(f"Menor número: {menor_numero}")