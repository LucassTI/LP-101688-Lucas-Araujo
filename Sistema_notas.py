import os

os.system("cls || clear")

# REGRAS DAS NOTAS

print("- SISTEMA DE AVALIAÇÃO")
print("- NOTA 9 OU MAIOR: A -")
print("= NOTA 7.5 OU MAIOR E MENOR QUE 9: B -")
print("- NOTA 6 OU MAIOR E MENOR QUE 7.5: C -")
print("- NOTA 4 OU MAIOR E MENOR QUE 6: D -")
print("- NOTA MENOR QUE 4: E -")


print("\n- APROVADOS ALUNOS COM NOTAS: A, B OU C -")
print("- REPROVADOS ALUNOS COM NOTAS: D OU E -")

# ENTRADA DE DADOS

print("\n- Informações do Aluno -")

nome = (input("Digite seu nome: "))
nota1 = float(input("Digite sua Nota da primeira unidade escolar: "))
nota2 =  float(input("Digite sua Nota da segunda unidade escolar: "))
media = (nota1 + nota2) / 2

# CONDIÇÕES

if media >= 9:
    resultado = "Nota A"
elif media >= 7.5:
    resultado = "Nota B"
elif media >= 6:
    resultado = "Nota C"
elif media >=4:
    resultado = "Nota D"
else:
    resultado = "Nota E"
    
if media >= 6:
    resultado2 = "Aprovado"
else:
    resultado2 = "Reprovado"
    
    
    
# SAÍDA DE DADOS 
print(f"\nAluno: {nome} ")
print(f"Média: {media}")
print(f"Nota: {resultado}")
print(f"Situação: {resultado2}")
print(f"Resultado Final: Aluno {nome} ficou com Média {media} sendo sua {resultado} e situação {resultado2}.") 
print("\nFim de programa")