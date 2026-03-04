import os

os.system ("cls || clear")
#MENU
print("""
      ===================== MENU =======================
      CÓDIGO                PRATO               PREÇO
         1                  PICANHA             R$25,00
         2                  LASANHA             R$20,00
         3                  STROGONOFF          R$18,00
         4                  BIFE ACEBOLADO      R$15,00
         5                  PÃO COM OVO         R$5,00
      """)
escolha = int(input("\nDigite o Código do prato desejado: "))

# PROCESSAMENTO DE DADOS
match escolha:
    case 1:
        prato = " Picanha    //    Valor: R$25,00"
    case 2:
        prato = " Lasanha    //    Valor: R$20,00"
    case 3:
        prato = " Strogonoff // Valor: R$18,00"
    case 4:
        prato = " Bife Acebolado // Valor: R$15,00"
    case 5:
        prato = " Pão com Ovo    //    Valor: R$5,00"
    case _:
        prato = "Prato Inválido"






print(f"\nPrato: {prato}")

print("""
      ============= PROGRAMA FINALIZADO =============
      """)