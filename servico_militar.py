
import os

os.system("cls || clear")

# Entrada de Dados

print("\n- Requerimento de Informações -")
sexo = input("Digite o seu sexo: ").lower()
ano= int(input("Digite seu ano de Nascimento: "))
ano_atual= 2026


# Processamento de Dados
sexo_correto = sexo == "masculino" 
ano_correto = ano_atual - ano >= 18

if ano_correto and sexo_correto:
    resultado = "Necessário Alistamento!"
else:
    resultado= "Não necessário alistamento!"

# Saída de dados
print("\n- Saída de Dados -")
print(f"Necessário Alistamento: {resultado}")
