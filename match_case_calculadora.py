import os

os.system ("cls || clear")

# ENTRADA DE DADOS

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operador = input("a operação desejada ( + - * /): ")

# PROCESSAMENTO DE DADOS
match operador:
    case "+":
        resultado = numero1 + numero2
    case "-":
        resultado = numero1 - numero2
    case "*":
        resultado = numero1 * numero2
    case "/":
        resultado = numero1 / numero2
    case _:
        print("Opção Inválida")
        resultado = 0
    
# SAÍDA DE DADOS
print(f"\nResultado: {resultado}")
