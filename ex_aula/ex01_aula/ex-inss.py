''' 
Criar um código para ver o ano que a pessoa poderá aposentar. Nome, Idade e exibir mensagem dizendo em qual ano ela irá se aposentar. Todas as pessoas podem se aposentar aos 65 anos de idade. 
'''

ano_atual = 2026

# - Digitar o nome
nome = str(input("Qual o seu nome? "))
# - Digitar a idade
idade = int(input("Qual a sua idade? "))
# - Calcular o ano de aposentadoria (65+)
ano = str((ano_atual - idade) + 65)
# - Exibir o resultado
print("Você poderá aposentar em", ano)



