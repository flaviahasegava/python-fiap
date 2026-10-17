import os
os.system("cls")

'''
7. Validação de login 
Solicite um nome de usuário e uma senha. O acesso deve ser permitido somente se o usuário for "admin" E a 
senha for "123". 
'''

# Solicitar o nome do usuário
usuario = str(input("Usuário: "))
# Solicitar a senha
senha = str(input("Senha: "))
# Verificar se o usuário e senha estão corretos
if usuario == "admin" and senha == "123":
    print("Login realizado com sucesso!")
else:
    print("Login ou senha incorreta! Digite novamente")