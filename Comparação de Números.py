import os

os.system ("cls || clear")

print ("\n- Solicitando Dados - ")
numero_1 = float(input(" Digite o primeiro número: "))
numero_2 = float(input(" Digite o primeiro número: "))
soma = numero_1 + numero_2
produto = numero_1 * numero_2

# CONDICIONAL 1
if numero_1 > numero_2:
    resultado1 = (f"{numero_1} é maior que {numero_2}")
else:
    resultado1 = (f"{numero_2} é maior que {numero_1}")
    
    # CONDICIONAL 2
if numero_1 < numero_2:
    resultado2 = (f"{numero_1} é menor que {numero_2}")
else:
    resultado2 = (f"{numero_2} é menor que {numero_1}")
    
#  Outra forma de fazer: 
# menor = min(numero_1, numero_2)
# maior = max(numero_1, numero_2)

    # Mostre os resultados
print(f"- Exibindo dados -")
print(f"Soma:   {soma}")
print(f"Produto  {produto}")
print(f"Maior número: {resultado1}")
print(f"Menor número:  {resultado2}")

print("Programa encerrado")
    