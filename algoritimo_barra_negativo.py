import os

os.system("cls")

# Inicialização das variáveis de controle
soma = 0
quantidade = 0

print("Digite valores inteiros positivos (ou um negativo para sair):")

while True:
    valor = int(input("Informe um número: "))
    
    # Condição de parada: se o valor for negativo, interrompe o loop
    if valor < 0:
        break
        
    # Acumula o valor e incrementa o contador
    soma += valor
    quantidade += 1

# Verificação para evitar divisão por zero caso o primeiro número seja negativo
if quantidade > 0:
    media = soma / quantidade
    print(f"\nQuantidade de números digitados: {quantidade}")
    print(f"A média aritmética é: {media:.2f}")
else:
    print("\nNenhum valor positivo foi informado.")