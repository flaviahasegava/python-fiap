import os
os.system("cls")

'''
13. Compra com frete grátis 
Solicite o valor da compra e informe se o cliente é membro do programa de fidelidade, usando S ou N. O frete 
será grátis se a compra for de pelo menos R$ 200,00 OU se o cliente for membro.
'''

# Solicitar o valor da compra e se o cliente é membro do programa de fidelidade
valor_compra = float(input("Qual o valor da compra? "))
cliente_membro = str(input("Você é cliente membro do programa de fidelidade? "))
# Verificar se tem frete grátis, sendo o valor maior ou igual a 200 reais e se o cliente é membro
if valor_compra >= 200.00 or cliente_membro:
    print("Frete grátis!")
else:
    print("Você ainda não possui frete grátis. Torne-se um membro do programa de fidelidade para ter frete grátis.")