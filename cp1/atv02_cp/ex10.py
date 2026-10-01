import os
os.system("cls")

'''
10. Acesso permitido por condição 
Solicite a idade e pergunte se a pessoa possui autorização, usando S ou N. Permita o acesso se ela tiver 18 
anos ou mais OU possuir autorização.
'''

# Solicitar a idade
idade = int(input("Qual a sua idade? "))
autorizacao = str(input("Você possui autorização? (S/N) "))
# Verificar se a idade é maior ou igual a 18 e se a autorização for "S" para permitir, caso ao contrário negar
if idade >= 18 or autorizacao == "S":
    print("Acesso permitido.")
else:
    print("Acesso negado!")
