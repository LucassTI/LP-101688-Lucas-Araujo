import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    idade: int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} metros")
        print(f"Altura: {self.altura} kg\n")

lista_cliente = []


print("=== Solicitando Dados ===\n")
for i in range(2):
    novo_cliente = Cliente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        peso= float(input("Digite seu peso: ")),
        altura= float(input("Digite sua altura: ")),
        
)
    print("=================")
    lista_cliente.append(novo_cliente)


print("\n === Exibindo Dados ===\n")
for cliente in lista_cliente:
    cliente.mostrar_dados()
print("=== Encerrando Sistema ===")
