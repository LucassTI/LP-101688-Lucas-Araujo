import os

os.system("cls")
soma = 0
QUANTIDADE_NOTAS = 2

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota: "))
    
        if nota > 0 and nota <= 10:
            soma+= nota
            break
        else:
         print("Nota inválida.")
         print("Tente novamente!")
    
media = soma / QUANTIDADE_NOTAS
print(f"Media: {media}")
    