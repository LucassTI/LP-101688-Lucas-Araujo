import os
os.system('cls')

# criando um vetor
vetor_notas = []

QUANTIDADE_NOTAS = 4
soma = 0
print("Adicionando 4 notas.")

for i in range( QUANTIDADE_NOTAS ):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    # Adiciona nota  no vetor
    vetor_notas.append(nota)
    soma += 1    
    # sum(vetor) = soma todos os valores no vetor.
media = sum(vetor_notas) / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"    
print("\n- Exibindo Resultados -")

# ForEach = percorre o vetor sem informar a quantidade.
# enumerate = através da variável i, numera a quantidade de repetições

for uma_nota in vetor_notas:
    print(f"Nota: {uma_nota}")
print(f"Média: {media:.1f}")
print(f"Resultado: {resultado}")