import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def imc(defpeso,defalturaquadrado):

    resultado_calculo = defpeso / (defalturaquadrado * defalturaquadrado)

    return resultado_calculo



# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    
resultado_calculo = imc(defpeso=peso, defalturaquadrado=altura)


if resultado_calculo < 18.5:
    resultado = "Abaixo do peso"
    recomendacao = "Consulte um nutricionista para orientação"
elif resultado_calculo <= 24.9:
    resultado = "Peso normal"
    recomendacao = 'Mantenha hábitos saudáveis!'
elif resultado_calculo <= 29.9:
    resultado = "Sobrepeso"
    recomendacao = "Considere uma dieta balanceada e atividade física"

elif resultado_calculo <= 34.9:
    resultado = "Obesidade grau I"
    recomendacao = 'Procure orientação de um profissional de saúde'

elif resultado_calculo <= 39.9:
    resultado = "Obesidade grau II"
    recomendacao = "Consulte um médico para avaliação e orientação"

elif resultado_calculo >= 40:
    resultado = "Obesidade grau III"
    recomendacao = "Busque assistência médica imediatamente"

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"Imc: {resultado_calculo:.2f}")
    print(f"Recomendação: {recomendacao}")