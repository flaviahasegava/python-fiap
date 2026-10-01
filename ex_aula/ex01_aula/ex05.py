import os
os.system("cls")

# - Digitar o nome do produto
nome_produto = str(input("Qual o nome do produto? "))
# - Digitar o preço unitário 
valor = float(input("Qual o preço unitário do produto? "))
# - Digitar a quantidade comprada
quantidade = int(input("Qual a quantidade comprada? "))
# - Digitar o percentual de desconto oferecido
percentual_desconto = int(input("Qual o percentual de desconto? "))
# - Calcular valor bruto da compra
valor_bruto = valor * quantidade
# - Calcular valor do desconto
desconto = valor_bruto * (percentual_desconto/100)
# - Calcular valor final da compra
valor_final = valor_bruto - desconto
# - Exibir o resultado
print(f"""
    Produto: {nome_produto}
    Valor bruto: R$ {valor_bruto}
    Desconto: R$ {desconto}
    Valor final: R$ {valor_final}
""")
