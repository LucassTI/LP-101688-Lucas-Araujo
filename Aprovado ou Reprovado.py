import os

os.system (" cls || clear")

nome = input("Digite seu nome: ")
nota_1 = float(input(" Digite sua primeira nota:"))
nota_2 = float(input(" Digite sua segunda nota:"))
nota_3 = float(input(" Digite sua terceira nota:"))

media = (nota_1 +nota_2 + nota_3) / 3

if media >=7:
    resultado = (f"{nome} está aprovado com a média de valor: {media}")
    
else:
   resultado = (f"{nome} está reprovado pois a {media} foi menor que 7")
   
   # Mostre o nome e a Média
print("\n- Exibindo dados -")
print("Nome: ", nome)
print(f"Resultado: {resultado}")

print("Programa encerrado")
    