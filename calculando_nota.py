import os

# Limpa o terminal
os.system("cls")

print("- Solicitando dados")
nome = input ("Digite seu nome: ")


primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float (input("Digite a segunda nota: "))

#Calcule
media = primeira_nota + segunda_nota / 2 
 
 # Mostre o nome e a Média
print("\n- Exibindo dados -")
print("Nome: ", nome)
print(f"Média: {media} do aluno.")