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



print("===== SALVANDO DADOS =====\n")
with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivo:
    for empresas in lista_empresas:
        arquivo.write(f"{empresas.nome}, {empresas.cnpj},{empresas.telefone}\n")

        print("===== SALVO COM SUCESSO =====\n\n")

print("= Consultando Arquivos =\n")
lista_contatos = []
with open('contato_empresas.csv', 'r') as arquivo:
    for linha in arquivo:
        nome, cnpj, telefone = linha.strip().split(',')
        lista_contatos.append(Empresas(
            nome=nome,
            cnpj=cnpj,
            telefone=telefone
            ))


print("===== EXIBINDO DADOS DAS EMPRESAS CADASTRADAS =====\n")
for empresas in lista_contatos:
    empresas.dados_finais()