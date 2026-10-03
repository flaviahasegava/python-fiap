import os
os.system("cls")

valor_compra = float(input("Qual o valor da compra? "))

if valor_compra < 0:
    print("Valor da compra inválido")

elif valor_compra < 100: 
    print("O valor da compra é menor que R$ 100,00. Você não tem nenhum desconto")

elif valor_compra >= 100 or valor_compra < 300:
    desconto_5 = valor_compra + (valor_compra * 0.05)
    print(f"Você tem 5% de desconto. Valor final: R$ {desconto_5:.2f}")

elif valor_compra >= 300 or valor_compra < 500:
    desconto_10 = valor_compra + (valor_compra * 0.10)
    print(f"Você tem 10% de desconto. Valor final: R$ {desconto_10:.2f}")

else:
    desconto_15 = valor_compra + (valor_compra * 0.15)
    print(f"Você tem 15% de desconto. Valor final: R$ {desconto_15:.2f}")