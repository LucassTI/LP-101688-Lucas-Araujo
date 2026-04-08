import os

os.system("cls")

# Função com parâmetros sem Retorno
def logo():
    os.system("cls")
    print("=======")
    print(" SENAI")
    print("=======")

# Função com parâmetros e com retorno.
def somar(a,b):
    return a + b

# Função com parâmetros e com retorno.
def subtrair(a,b):
    return a - b


# Função com parâmetros e com retorno.
def multiplicar(a,b):
    multiplicacao = a * b
    print(f"Multiplicação: {multiplicacao}")


# Função com parâmetros e com retorno.
def dividir(a,b):
    divisao = a / b
    print(f"Divisão: {divisao}")


# Função com parâmetros e com retorno.
def mediar(a,b):
    media = (a+b) / 2
    print(f"Média: {media}")

ns = []
QUANTIDADE = 2

logo()
print("= Solicitando Dados =")
for i in range(QUANTIDADE):
    ns2 = int(input(f"Digite o {i+1}ª número: "))
    ns.append(ns2)


soma = somar(ns[0], ns [1])
subtracao = subtrair(ns[0], ns[1])


logo ()
print("= Exibindo Dados =")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
multiplicar(ns[0], ns[1])
dividir(ns[0], ns[1])
mediar(ns[0], ns[1])