import os
os.system("cls")

'''
6. Desconto por idade 
Solicite a idade de uma pessoa. Se ela tiver menos de 12 anos OU 60 anos ou mais, informe que tem direito ao 
desconto. Caso contrário, informe que não tem direito. 
'''

# Solicitar a idade
idade = int(input("Qual a sua idade? "))
# Verificar se o a idade tem direito ao desconto
if idade < 12 or idade >= 60:
    print("Você tem direito ao desconto!")
else:
    print("Você ainda não tem direito ao desconto.")