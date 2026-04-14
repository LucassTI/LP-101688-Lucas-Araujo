import os

os.system("cls")
def imc(defpeso,defalturaquadrado):

    resultado_calculo = defpeso / (defalturaquadrado * defalturaquadrado)

    return resultado_calculo

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
calculo = altura * altura



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

print(f"Imc: {resultado_calculo:.2f}")
print(f"Situação: {resultado}")
print(f"Recomendação: {recomendacao}")