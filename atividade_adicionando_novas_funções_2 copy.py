import os

os.system("cls")

# Listas para guardar os números
numeros = []
pares = []
impares = []
soma_geral = 0

# 1. Coleta de dados
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    soma_geral += num
    
    # Separando os bonitos por categoria
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# 2. Cálculos finais
media = soma_geral / len(numeros) if numeros else 0

# 3. Exibição (A parte que você sentiu falta!)
print("\n" + "="*35)
print(f"{' ESTATÍSTICAS COMPLETAS ':-^35}")
print(f"Números Pares:   {pares}")
print(f"Números Ímpares: {impares}")
print("-" * 35)
print(f"Total de Pares:   {len(pares)}")
print(f"Total de Ímpares: {len(impares)}")
print(f"Média Geral:      {media:.2f}")
print("="*35)