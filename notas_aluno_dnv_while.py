import os
os.system("cls")
soma = 0
NOTAS = 3
aluno = input("Digite seu nome: ")
for i in range (NOTAS):
    while True:
        nota = float(input("Digite suas notas: "))
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print("Tente novamente!")     

media = soma / NOTAS

if media >= 7:
    resultado = f"Aluno {aluno} está aprovado com média de valor{media:.2f}"
elif media >=5:
    resultado = f"Aluno {aluno} ficou com média nota {media:.2f} e está de recuperação"
else:
    resultado = f"AÇuno {aluno} ficou com média nota {media:.2f} e está reprovado"
    
print("\n- Exibindo Informações -")  
print(resultado)
