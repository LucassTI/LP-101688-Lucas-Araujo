import os

os.system('cls')

vetor_notas = []

QUANTIDADE_NOTAS = 3

print("Adicionando 3 notas.")

for i in range( QUANTIDADE_NOTAS ):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    
    
print("\n- Exibindo Resultados -")
# ForEach
for uma_nota in vetor_notas:
    print(f"Nota: {uma_nota}")