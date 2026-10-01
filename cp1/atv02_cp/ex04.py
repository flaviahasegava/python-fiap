import os
os.system("cls")

'''
4. Senha correta 
Solicite uma senha numérica. Considere que a senha correta é 1234. Informe se o acesso foi permitido ou 
negado. 
'''

# Solicitar uma senha numérica
senha = str(input("Qual a sua senha? "))
# Verificar se a senha está correta
if senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso NEGADO!")