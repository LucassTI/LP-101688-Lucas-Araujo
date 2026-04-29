import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: int
    endereco: str

    def mostrar(self):
        print(f"\nNome: {fornecedor.nome}")
        print(f"E-mail: {fornecedor.email}")
        print(f"Telefone: {fornecedor.telefone}")
        print(f"Endereço: {fornecedor.endereco}")
        print("\n=== Encerrando Programa ===")

fornecedor = Fornecedor(
    nome = input("Digite seu nome: "),
    email= input("Digite seu e-mail: "),
    telefone= int(input("Digite seu telefone: ")),
    endereco = input("Digite seu endereço: ")
)

print("\n=== Exibindo Dados Informados ===")
fornecedor.mostrar()