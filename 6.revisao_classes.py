import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Empresas:
    nome: str
    cnpj: str
    telefone: str

    def dados_finais(self):
        print(f"Nome da Empresa: {self.nome}")
        print(f"Cnpj da Empresa: {self.cnpj}")
        print(f"Telefone da Empresa: {self.telefone}")
        print("======================")

lista_empresas = []

while True:
    empresas = Empresas(
        nome= input('Digite o nome da Empresa: '),
        cnpj= input("Digite o cnpj da Empresa: "),
        telefone= input("Digite o telefone da Empresa:"),
    )
    lista_empresas.append(empresas)
    print("======================")

    continuar = input("Deseja adicionar mais uma empresa? (s/n): ").lower()
    print("======================")

    if continuar == "n":
        break


print("===== EXIBINDO DADOS DAS EMPRESAS CADASTRADAS =====\n")
for empresas in lista_empresas:
    empresas.dados_finais()

print("===== SALVANDO DADOS =====\n")
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresas in lista_empresas:
        arquivo.write(f"{empresas.nome}, {empresas.cnpj},{empresas.telefone}\n")

        print("===== SALVO COM SUCESSO =====")




