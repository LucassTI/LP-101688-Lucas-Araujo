import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

@dataclass
class Funcionario:
    nome: str
    matricula: int
    setor: str
    email: str


cliente1 = Cliente('Jussara', 'jujudopix@gmail.com', 71987655678)
funcionario1 = Funcionario('Lucas', 20223041, 'Oficina Ortópedica', "lc@gmail.com")

print(f"Nome: {cliente1.nome}")
print(f"E-mail: {cliente1.email}")
print(f"Telefone: {cliente1.telefone}\n")

print(f"Nome do Funcionário: {funcionario1.nome}")
print(f"Matrícula: {funcionario1.matricula}")
print(f"E-mail: {funcionario1.email}")
print(f"Setor: {funcionario1.setor}\n")