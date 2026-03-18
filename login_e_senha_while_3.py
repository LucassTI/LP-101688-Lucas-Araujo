import os

os.system("cls")

quantidade = 3

while quantidade > 0:
        login = input("Digite seu login:  ")
        senha = input ("Digite sua senha: ")
        LOGIN = "1234"
        SENHA = "12345"
        if login == LOGIN and senha == SENHA:
            print("Acesso permitido!")
            break
        else:
            quantidade -= 1
            print(f"Acesso negado tentativas restantes: {quantidade}")