import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

print("=== Solicitando dados do Cliente ===")
cliente = Cliente(
    nome= input('Digite seu nome:'),
    email= input('Digite seu e-mail: '),
    telefone= int(input("Digite seu telefone: "))
)
print(f"\n=== Exibindo Resultados ===")
cliente.mostrar_dados()