import os

os.system("cls || clear")

# Entrada de dados
print("- Solicitando Dados")
print("- Valores das maçãs: R$1,30 unidade, a partir de 12 unidades saem a R$1,00 a Unidade -")
quantidade = int(input("Quantidade de maçãs desejadas: "))

if quantidade < 11:
    calculo = 1.30 * quantidade
else:
    calculo = 1 * quantidade
    
# SAÍDA DE DADOS

print(f"\n-  Valor: R${calculo:.2f}, de {quantidade} maçãs")