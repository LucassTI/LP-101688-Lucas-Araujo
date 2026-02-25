import os

os.system("cls || clear")

# Coleta de Dados

print("- Solicitando dados -")
numero_1 = int(input("\nDigite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))

# VARIAVEIS

soma = (numero_1 + numero_2)
produto = (numero_1 * numero_2)
minimo = (min(numero_1, numero_2))
maximo = (max(numero_1, numero_2))
media = (numero_1 + numero_2 / 2)

# CONDICIONAL

if numero_1 == numero_2:
    resultado = f"Sim, ambos os valores são iguais sendo eles: {numero_1}" 
else:
    resultado = "Não, os valores são diferentes"

# SAÍDA DE DADOS
print("\n- Resultados -")
print(f"\nSoma dos valores = {soma}")
print(f"Produto dos valores = {produto}")
print(f"Média dos valores = {media}")
print(f"Maior valor = {maximo}")
print(f"Menor valor = {minimo}")
print(f"Valores são iguais = {resultado}")

print("\nPrograma encerrado")