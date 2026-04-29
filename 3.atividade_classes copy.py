import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

print("=== Recebendo Informações ===")

paciente = Paciente(
    nome= input("Digite seu Nome: "),
    idade= int(input("Digite sua Idade: ")),
    peso= float(input("Digite seu Peso: ")),
    altura= float(input("Digite sua Altura: "))
)

print("\n=== Exibindo Informações ===")
print(f"Nome informado: {paciente.nome}")
print(f"Idade informada: {paciente.idade}")
print(f"Peso informado: {paciente.peso}")
print(f"Altura informada: {paciente.altura:.2f}\n")
print("=== Encerrando Programa ===")