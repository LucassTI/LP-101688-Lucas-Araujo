import os

os.system("cls || clear")


# Solicitando dados
print("- Solicitando dados -")
nome = input("\nDigite seu nome: ")
idade = int(input("Digite sua idade: "))

# Condicionamento
if idade == 16:
    resultado =("Opcional votar.")
if idade == 17:
    resultado=("Opcional votar.")
if idade < 16:
    resultado=("Não possue idade para votar.")
if idade >= 18:
        resultado =("Voto Obrigátorio.")
if idade >= 65:
    resultado=("Opcional votar por idade avançada.")
    
# Saida de dados

print(f"\nResultado: {nome}, {idade} anos, {resultado}")


# O comando elif em Python (abreviação de else if) é usado em estruturas condicionais para verificar múltiplas expressões consecutivamente. Ele permite avaliar uma nova condição caso a anterior (if ou elif anterior) seja falsa, evitando indentação excessiva