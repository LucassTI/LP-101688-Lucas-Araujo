import os

os.system("cls")


familias = 0
media_salario = 0
media_filhos = 0
maior_salario = 0
menor_salario = 0
filhos = 0
opcao = 0

while True:
    print("""
---     MENU DA PESQUISA ---
1   -   Adicionar família
2   -   Sair e exibir resultados                  
          """)
    
    opcao = int(input("Digite a opção desejada: "))
    
    match opcao:
        
    
        
        case 1:
            print("--- CADASTRO ---")
            salario_familiar = int(input("Digite a média do sálario da sua família: "))
            filho = int(input("Digite a quantidade de filhos nessa fámilia:  "))
            
            maior_salario = max(media_salario, salario_familiar)
            menor_salario = min(media_salario, salario_familiar)
            filhos += 1
            media = media_filhos / filho
            familias =+ 1
            
            print("Família adicionada com sucesso. \n")
            
            
        case 2:
            if familias == 0:
                print("\nNenhuma familia cadastrada ainda \n")
            else:
                media_populacao = salario_familiar / familias
                
                print("\n--- RESULTADOS DA PESQUISA ---")
                print(f"Média de salário da população {media_populacao:.2f}")
                print(f"Maior media de filhos {media_filhos}")
                print(f"Maior sálario: {maior_salario}")
                print(f"Menor sálario: {menor_salario}")
                
                break
        case 3:
            print("\nEncerrando o programa... \n")
            break
        case _:
            print("\nOpção Inválida  \n")