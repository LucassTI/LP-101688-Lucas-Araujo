import os

os.system("cls || clear")

# ENTRADA DE DADOS

nota = int(input("Digite um nota: "))

# PROCESSAMENTO DE DADOS
if nota>= 0 and nota <=10:
    resultado = nota
else:
  resultado = "A nota tem que estar entre 0 e 10"

# SAÍDA DE DADOS
print("\n- Exibindo Resultados -")
print(f"{resultado}")