import os
os.system("cls")

'''
Exercício:
2. Dado o valor de uma compra pelo usuário, calcular um desconto de 12%, caso a compra seja de ao menos 2000 reais, senão calcular o desconto de 6%. No final, exibir o valor do desconto atualizado.
ENTRADA: 5000    SAÍDA: Desconto de 12%, novo valor R$ 4400.00
ENTRADA: 1000    SAÍDA: Desconto de 6%, novo valor R$ 940.00
'''

# Solicitar o valor da compra
compra = float(input("Digite o valor da compra: "))
# Verificar qual desconto dar
if compra >= 2000:
    # 1 - 0.12
    compra = compra * 0.88
    print(f"Desconto de 12%, novo valor R$ {compra:.2f}")
else:
    # 1 - 0.06
    compra = compra * 0.94
    print(f"Desconto de 6%, novo valor R$ {compra:.2f}")

# >    <=
  >=   <
  !=   ==
  ==   !=
