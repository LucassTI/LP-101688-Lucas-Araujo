import os
os.system("cls")

# Função com parâmetros

def somar(n1,n2):
    soma = n1 + n2
    return soma
    print(f"Soma: {soma}")

# Exemplo do uso da função

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# chamando função
# enviando parâmetros

resultad0 =somar(primeiro_numero, segundo_numero)

print(f"Soma: {resultad0}")