import os 

os.system('cls')


print("""
    === MENU ===
    1   Picanha          R$ 25,00
    2   Lasanha          R$ 20,00
    3   Strogonoff       R$ 18,00
    4   Bife acebolado   R$ 15,00
    5   Pão com ovo      R$ 5,00
        """)

vetor_opcao = []

vetor_opcao = int(input("Digite a opção do cardápio desejada: "))

match vetor_opcao:
    case 1:
        prato = "Picanha"
        preco = 25
    case 2:
        prato = "Lasanha"
        preco = 20
    case 3:
        prato = "Strogonoff"
        preco = 18
    case 4:
        prato = ""
        preco = 15
    case 5:
        vetor_opcao = 5
        preco = 5
case_:
v


