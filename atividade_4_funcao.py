import os
os.system("cls")

# Essa função está defeinido a media
def notas(n1, n2):
    media = (n1 + n2) / 2
    return media

# Essa função está calculando de o aluno está aprovado ou reprovado
def ap_rep(media):
    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return resultado

print("=== Solicitando Dados === ")
n1 = int(input("\nDigite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))


media = notas(n1, n2)
resultado = ap_rep(media)


# Exibindo Resultados
print(f"media: {media}")
print(f"Resultado: {resultado}")