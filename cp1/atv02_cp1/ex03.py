import os
os.system("cls")

'''
3. Aprovado ou reprovado 
Solicite a média final de um aluno. Considere aprovado quem obtiver média maior ou igual a 6,0. Caso 
contrário, informe que o aluno foi reprovado.
'''

# Solicitar a média final
media = float(input("Qual a sua média? "))
# Verificar se o aluno foi reprovado ou aprovado sendo a média 6
if media >= 6:  
    print("Aluno APROVADO.")
else:
    print("Aluno REPROVADO.")