import os

os.system("cls")
codigo = int(input('Insira o codigo do prato'))
preco_total = 0
pratos_solicitados = ""
preco = 0
while True:
    
    os.system("cls)")
    print("""
    Código |   Prato    |        Valor
    1         Picanha          25,00
    2         Lasanha          20,00
    3         Strogonoff       18,00
    4         Bife Acebolado   15,00
    5         Pão com ovo       5,00
    """)






    match codigo:
        case 1:
            prato = "Picanha"
            preço = 25
        case 2:
            prato = "Lasanha"
            preço = 20
        case 3:
            prato = "Strogonoff"
            preço = 18
        case 4:
            prato = "Bife Acebolado"
            preço = 15
        case 5:
            prato = "Pão com Ovo"
            preço = 5
        case _:
            prato = ""
            preco = 0
            print("Opção inválida.")
            print("Tente Novamente...\n")
        
        
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato

    mais_pedidos = input("Deseja fazer um novo pedido? \n Use S ou N: ").lower()

    if mais_pedidos== "n":
        break
    

    total_pagar = preco_total
    print("\n=== Nota Fiscal ===")
    print(f"Pratos solicitados: {pratos_solicitados}")
    print(f"Total da compra: R$ {preco_total}")



        
        
    
    