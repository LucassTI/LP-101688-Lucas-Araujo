import os
os.system("cls")

notas = []
QUANTIDADE = 3

for i in range (QUANTIDADE):
    notas3 = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(notas3)

def med (a,b,c):
    media = (a + b + c) / 3
    return media

med (notas[0], notas[1], notas[2])
media = med(notas[0], notas[1], notas[2])


print("\n- Exibindo Resultados: ")
print(f"Média: {media:.2f}")