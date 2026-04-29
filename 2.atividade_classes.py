import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

print("=== Solicitando dados do Cliente ===")
cliente = Cliente(
    nome= input('Digite seu nome:'),
    email= input('Digite seu e-mail: '),
    telefone= int(input("Digite seu telefone: "))
)
print(f"\n=== Exibindo Resultados ===")
print(f"Nome: {cliente.nome}")
print(f"E-mail: {cliente.email}")
print(f"Telefone: {cliente.telefone}")