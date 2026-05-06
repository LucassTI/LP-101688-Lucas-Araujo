import os
from dataclasses import dataclass

os.system('cls')

@dataclass
class Jogo:
    nome: str
    estilo: str
    plataforma: str

    def resultado(self):
        print(f"Jogo que deseja jogar: {self.nome}")
        print(f"Estilo do jogo: {self.estilo}")
        print(f"Plataforma que deseja jogar: {self.plataforma}")

NOME_ARQUIVO = 'jogos_futuros.csv'

def salvar_arquivo(jogo: Jogo):
    with open (NOME_ARQUIVO, "a", encoding='utf-8') as arquivo:
        arquivo.write(f'{jogo.nome}, {jogo.estilo}, {jogo.plataforma}\n')

def ler_jogos():
    try:
        print("\n= Lista der jogos que deseja jogar =\n")
        lista_jogos = []
        with open (NOME_ARQUIVO, 'r') as arquivo:
            for linha in arquivo:
                nome, estilo, plataforma = linha.strip().split(',')
                lista_jogos.append(Jogo(nome, estilo, plataforma))

                for jogo in lista_jogos:
                    jogo.resultado()
                    print('=' * 10)
    except FileNotFoundError:
        print("=( Arquivo não encontrado =(")
        


while True: 
            print((("""
                = JOGOS QUE FUTURAMENTE DESEJO JOGAR =\n
                    1- CADASTRAR JOGO
                    2- VER LISTA DE JOGOS QUE DESEJO JOGAR
                    3- ENCERRAR
                """)))
            
            opcao = int(input('Digite a opção desejada: '))

            match opcao:
                case 1:
                    os.system('cls')
                    print("         = CADASTRANDO JOGO =")
                    jogo = Jogo(
                        nome= input("\nDigite o nome do Jogo: "),
                        estilo= input('Digite o estilo do Jogo: '),
                        plataforma= input('Digite a plataforma que gostaria de jogar o jogo: ')
                        )
                    print("= Salvando dados")

                    salvar_arquivo(jogo)



                case 2:
                    os.system('cls')
                    ler_jogos()
                    input('= Precione enter para retornar ao menu =')
                    
                case 3:
                    print("\n= Encerrando Sistema =")
                    break
                    
                case _:
                    print("= Opção Inválida =\n")
                    
