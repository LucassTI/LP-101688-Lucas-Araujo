# MODELO NORMAL, SEM USAR CLASSE 
# import os

# os.system("cls")

# nome = 'Alice'
# idade = 19

# print(f"Nome: {nome} \n Idade: {idade}")

import os
from dataclasses import dataclass
os.system('cls')

# Criando uma Classe
@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class Pet:
    nome: str
    idade: int

# Usando uma Classe.
pessoa1 = Pessoa('Alice', 18)
pessoa2 = Pessoa('João do chupão', 17)
pet1 = Pet('Anitta', 13)
pet2= Pet("Nemo", 7)


print(f"Nome:{pessoa1.nome}")
print(f"Idade:{pessoa1.idade}")
print(f"\nNome do Pet: {pet1.nome}")
print(f"Idade do pet: {pet1.idade}")
print(f"\nNome:{pessoa2.nome}")
print(f"Idade:{pessoa2.idade}")
print(f"\nNome do Pet: {pet2.nome}")
print(f"Idade do pet: {pet2.idade}")
