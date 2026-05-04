import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pet:
    nome: str
    idade:  str
    raca: int

    def mostrar_dados(self):
         print(f"Nome: {self.nome}")
         print(f"Idade: {self.idade}")
         print(f"Raça: {self.raca}")
         print("=======================")


lista_pets = []

print("==== Solicitando Dados ====")
for i in range(2):
    pets = Pet(
        nome= input("Digite o nome do pet: "),
        idade= input("Digite a idade do pet: "),
        raca= input("Digite a raça do pet: ")
        )
    lista_pets.append(pets)
    print("=======================")
    
continuar = input("Deseja cadastrar mais pets: (s/n): ").lower()
print("=======================")

if continuar == "s":
    while True:
            pets = Pet(
        nome= input("Digite o nome do pet: "),
        idade= input("Digite a idade do pet: "),
        raca= input("Digite a raça do pet: "),
            )
    
            lista_pets.append(pets)
            continuar = input("Deseja cadastrar mais pets: (s/n): ").lower()
            if continuar == "n":
                 break

with open('dados_pet.txt', 'a') as arquivo_pets:
     for pets in lista_pets:
          arquivo_pets.write(f'{pets.nome}, {pets.idade}, {pets.raca}\n')
        

print("Arquivo salvo com sucesso!")

print("\n==== Lista de Pets Cadastrados ====\n")
for pets in lista_pets:
     pets.mostrar_dados()
print("==== Encerrando Programa ====")

    
        
    

        
         
   

