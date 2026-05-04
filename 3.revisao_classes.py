import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: str
    

    def mostrar_dados(self):
        
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}\n")

lista_funcionarios = []


while True:
    
    print("\n==== Solicitando Dados ====\n")
    funcionarios = Funcionario(
        nome=input("Digite seu nome: "),
        email=input("Digite seu e-mail: "),
        telefone=input("Digite seu telefone:"),
)
    lista_funcionarios.append(funcionarios)

    continuar=input("Deseja continuar(s/n):").strip().lower()
    if continuar == "n":
        break

    

print(f"\n ==== Dados do Funcionário ====\n")
for funcionarios in lista_funcionarios:
    funcionarios.mostrar_dados()
print(f"==== Encerando Sistema ====")



