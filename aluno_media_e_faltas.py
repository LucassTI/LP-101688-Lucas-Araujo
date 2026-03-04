import os

os.system("cls || clear")

# ENTRADA DE DADOS

nome = input("Digite o nome do Aluno: ")
media= float(input("Digite sua média: "))
faltas= int(input("Digite seu número de faltas: "))


# PROCESSAMENTO DE DADOS
if media >=7 and faltas <=40 :
    resultadofinal = "Aprovado!"
else:
    resultadofinal = "Reprovado!"

# SAÍDA DE DADOS
print("\n- Exibindo Resultados -")
print(f"Nome do Aluno: {nome}")
print(f"Situação do Aluno: {resultadofinal} ") 