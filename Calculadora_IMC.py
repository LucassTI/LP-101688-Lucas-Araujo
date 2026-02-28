import os

os.system("cls|| clear")

# Pedido de Informações

print("O IMC - Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. ")

print("\nInsira abaixo seu Peso e Altura para descobrir seu IMC")
peso = (float(input("Insira seu Peso: ")))
altura = (float (input("Insira sua Altura: ")))

# Processamento de dados
calculo1 =altura * altura
calculo = peso / calculo1

if calculo <= 40:
    resultado2 = "Obesidade Grau 3 (Mórbida)"
elif calculo <= 35:
   resultado2= "Obesidade Grau 2"
elif calculo <=30:
    resultado2= "Obesidade Grau 1"
elif calculo <= 25:
    resultado2= "Levente acima do peso"
elif calculo <= 18.6:
    resultado2= "Peso Ideal (Parabéns)"
else:
    resultado2= "Abaixo do peso"

# Saída de dados:
print("n\- Resultado -")
print(f"Resultado do Cálculo: {calculo:.2f}")
print(f"Condição do Imc: {resultado2}")