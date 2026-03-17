import os
os.system ("cls")

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Acesso negado")
        print("Tente novamente... \n")
    else:
        print("Acesso permitido.")
        break
    
print("Programa encerrado.")