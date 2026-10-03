import os
os.system("cls")

'''
8. Pode votar pela idade 
Solicite a idade de uma pessoa. Para este exercício, considere que a pessoa pode votar se tiver 16 anos ou 
mais. Caso contrário, informe que ainda não pode votar. 
'''

# Solicitar a idade
idade = int(input("Qual a sua idade? "))
# Verificar se tem 16 anos ou mais
if idade >= 16:
    print("Você já pode votar!")
else:
    print("Você ainda não pode votar.")