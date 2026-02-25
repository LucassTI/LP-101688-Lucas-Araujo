import os

os.system("cls || clear")

# SOLICITANDO DADOS
print("\n- Solicitando dados- ")
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

# PROCESSAMENTO
maximo =max(numero_1,numero_2,numero_3)
minimo =min(numero_1,numero_2,numero_3)

# SAÍDA DE DADOS
print("\n- Resultado -")
print(f"Maior entre os números: {maximo}")
print(f"Menor entre os números: {minimo}")
print("\nFim do programa")