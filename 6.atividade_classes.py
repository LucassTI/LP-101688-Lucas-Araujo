import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco 
    # Relacionamento com a classe Endereço

    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}\n")
        print(f"Idade: {self.idade}")
        
print("=-=- Informando Dados =-=-")

cliente = Cliente(
    nome= input ('Digite seu nome:'),
    idade= int(input("Digite sua idade: ")),
    endereco= Endereco
)
endereco = Endereco(
    logradouro= input("Digite o nome do Logradouro: "),
    numero= int(input("Digite o número do Logradouro: "))
)



print("\n=-=- Exibindo Informações =-=-")
cliente.mostrar()
print("\n=-=- Fim de Programa =-=-")