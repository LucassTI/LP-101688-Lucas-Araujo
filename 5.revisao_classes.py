import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Funcionario:
    nome: str
    matricula: int
    turno: str
    setor: str

    def mostrar_dados(self):
        print(f"Nome do Funcionário: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Setor: {self.setor}")
        print(f"Turno: {self.turno}")
        print("==================")

quantidade = int(input("Digite o número de Funcionários que deseja cadastrar: "))
lista_funcionarios = []

for i in range(quantidade):
    funcionario = Funcionario(
        nome= input("Digite o nome do funcionário: "),
        matricula= int(input("Digite matrícula do funcionário: ")),
        setor= input("Digite setor do funcionário: "),
        turno= input("Digite o turno do funcionário: ")
    )
    print("=====================\n")
    lista_funcionarios.append(funcionario)

print("===== EXIBINDO DADOS DOS FUNCIONÁRIOS CADASTRADOS =====\n")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print("===== SALVANDO DADOS =====\n")
with open('lista_funcionarios.csv', 'a', encoding='utf-8') as arquivo:
    for funcionario in lista_funcionarios:
        arquivo.write(f"{funcionario.nome}, {funcionario.matricula}, {funcionario.setor}, {funcionario.turno}\n")
        print("===== SALVO COM SUCESSO =====")

print("\n===== FINALIZANDO SISTEMA =====")

