import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f"Nome do Livro: {self.nome}")
        print(f"Nome do Autor: {self.autor}")
        print(f"Nome do Categoria: {self.categoria}")
        print(f"Valor do Livro (R$): {self.preco}\n")

    

lista_livros = []


# quantidade = int(input("Digite a Quantidade de Livros a ser registrados no Arquivo: "))


        
while True:
    print("= SISTEMA DE CADASTRO =")
    print("1 - Adicionar livro")
    print("2 - Listar Livros")
    print("3 - Sair")
    escolha = int(input('Escolha a opção Desejada: '))
    match escolha:
        case 1:
            livro = Livro(
            nome= input(f'Digite o nome do  livro: '),
            autor= input(f"Digite o nome do  autor:"),
            categoria= input(f"Digite a categoria do livro: "),
            preco= float(input("Digite o valor do livro: "))
            )
            lista_livros.append(livro)
            print("\n= Salvando Dados =\n")
            with open('informacoes_livros.csv', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n')
            print("= Salvo com Sucesso =\n\n")

            # print("= SISTEMA DE CADASTRO =")
            # print("1 - Adicionar livro")
            # print("2 - Listar Livros")
            # print("3 - Sair\n")

            # reiniciar = int(input('Escolha a opção Desejada: '))

            



            


        case 2:
            lista_algo = []

            with open(f'informacoes_livros.csv', 'r') as arquivo:
                for linha in arquivo:
                    nome, autor, categoria, preco = linha.strip().split(',')
                    livro_dados = Livro(nome, autor, categoria, float(preco))
                    lista_algo.append(livro_dados)
                    
            print("= Mostrando dados =")
            for livro in lista_algo:
                    livro.mostrar_dados()
                    
        case 3:
                print('\n= Encerrando Sistema =')
                break
        case _:
            print("\n= Opção Inválida =\n")

            



