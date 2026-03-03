import os

os.system("cls || clear")

# Recebendo dados

nome = input("Nome do Colaborador: ")
matricula = int(input("Digite a Matrícula do Colaborador (6 números): "))
idade = int(input("Idade: "))
ano = int(input("Ano de nascimento: "))
tempo = float(input("Tempo Trabalhado (anos): "))

# Processamento de Dados
if idade >= 65 or tempo >=30:
    resultadofinal = "Requerer aposentadoria"
else:
    resultadofinal= "Não requerer aposentadoria"
    

# Exibindo dados

print("n\- Dados do Colaborador -")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Ano de Nascimento: {ano}")
print(f"n\Matrícula: {matricula}")
print(f"Tempo trabalhado (Em anos): {tempo}")
print(f"Requerimento: {resultadofinal}")