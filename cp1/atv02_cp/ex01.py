import os
os.system("cls")

'''
Exercício:
1. Dado o valor de uma compra pelo usuário, informar se ele terá desconto ou não. Se a compra for até 1000 reais, informar: "Não terá desconto", caso contrário, informar "Terá deconto de 10%".
ENTRADA: 3000    SAÍDA: Terá desconto de 10%
SAÍDA: 500       SAÍDA: Não terá desconto
'''

# Informar o valor da compra
compra = float(input("Qual o valor da compra? R$ "))
# Verifica se tem desconto ou não
# Se a compra foi de até 1000 reais
if compra <= 1000:
    print("Não terá desconto")
# Se a compra for acima de 1000 reais
else:
    print("Terá desconto de 10%")