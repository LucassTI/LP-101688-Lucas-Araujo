import os
os.system("cls")

# função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Bem vindo(a) ao nosso site")

# Exemplo de uso da função
nome_visitante = input("Digite seu nome: ")
saudacao(nome=nome_visitante)