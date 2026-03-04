import os

os.system("cls || clear")

# ENTRADA DE DADOS

usuario = input("Digite seu Login: ")
senha = input("Digite sua senha: ")
senhareal = "SENAIBAHIA"
loginreal = "Lucas123"

login_correto = loginreal == usuario 
senha_correta = senhareal == senha

# PROCESSAMENTO DE DADOS
if usuario == loginreal and senha == senhareal:
    acesso = "Bem-vindo!"
else:
    acesso = "Login ou senha inválidos"

# SAÍDA DE DADOS
print("\n- Exibindo Resultados -")
print(f"Acesso do Login: {acesso} ") 