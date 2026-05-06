import os
from dataclasses import dataclass
os.system("cls")


@dataclass

class Funcionario:
    nome: str
    matricula: str
    turno: str
    setor: str

    def mostrar_dados(self):
        print(f"Nome do Funcionário: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Setor: {self.setor}")
        print(f"Turno: {self.turno}")

lista_funcionarios = []

with open ('lista.funcionarios.csv', 'r') as arquivo:
        for linha in arquivo:
            nome, matricula, turno, setor = linha.strip().split(',')
            funcionarios = (Funcionario(
                nome=nome,
                matricula=matricula,
                setor=setor,
                turno=turno,
        ))
        lista_funcionarios.append(funcionarios)

        for funcionarios in lista_funcionarios:
            funcionarios.mostrar_dados()
