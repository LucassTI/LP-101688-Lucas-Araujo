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


quantidade = int(input("Quantidade de funcionários no sistema: "))
lista_funcionarios = []

for i in range(quantidade):
    
    print("\n==== Solicitando Dados ====\n")
    funcionarios = Funcionario(
        nome=input("Digite seu nome: "),
        email=input("Digite seu e-mail: "),
        telefone=input("Digite seu telefone:")
)
    
    lista_funcionarios.append(funcionarios)

print(f"\n ==== Dados do Funcionário ====\n")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()
print(f"==== Encerando Sistema ====")



