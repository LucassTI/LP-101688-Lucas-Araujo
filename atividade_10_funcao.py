import os

os.system("cls")

def med (n1,n2):
    media = (n1 + n2) / QUANTIDADE
    return media

while True:
    notas = []

    QUANTIDADE = 2

    for i in range(QUANTIDADE):
        notas2 = float(input(f"Adicione a {i+1}ª nota: "))
        notas.append(notas2)



    media = med(notas[0], notas [1])


    if 0 <= media <= 10:
        if media >= 7:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"
        break
    else:
        print(f"\nMédia {media:.2f} é inválida! Notas devem resultar entre 0 e 10.")
        
        


print("\n= Exibindo Resultados =")
print(f"Resultado: {resultado}")
print (f"Média: {media:.2f}")
