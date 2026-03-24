import os

os.system("cls")


soma_salario = 0
contador_pessoas = 0
maior_idade = 0
menor_idade = 0
mulheres_salario5k = 0

opcao = 0

while True:
    print("""
---     MENU DA PESQUISA ---
1   -   Adicionar pessoa
2   -   Exibir resultados
3   -   Sair                   
          """)
    
    opcao = int(input("Digite a opção desejada: "))
    
    match opcao:
        
    
        
        case 1:
            print("--- CADASTRO ---")
            idade = int(input("Digite sua idade: "))
            sexo = input("Digite o sexo (M/F): ").upper
            salario = float(input("Digite o Salário: R$ "))
            
            soma_salario += salario
            contador_pessoas += 1
            
            maior_idade = max(idade, menor_idade)
            menor_idade = min(idade, menor_idade)
            
            if sexo == "F" and salario >= 5000:
                mulheres_salario5k += 1
                print("Pessoa adicionada com sucesso. \n")
        case 2:
            if contador_pessoas == 0:
                print("\nNenhuma pessoa cadastrada ainda \n")
            else:
                media_salario = soma_salario / contador_pessoas
                
                print("\n--- RESULTADOS DA PESQUISA ---")
                print(f"Média de salário do grupo {media_salario:.2f}")
                print(f"Maior idade: {maior_idade}")
                print(f"Menor idade: {menor_idade}")  
                print(f"Mulheres com salário a partir de R$ 5.000,00: {mulheres_salario5k}")
                break
        case 3:
            print("\nEncerrando o programa... \n")
            break
        case _:
            print("\nOpção Inválida  \n")