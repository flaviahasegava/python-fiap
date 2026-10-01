"""
Receba o preço de um produto e aplique 10% de desconto
"""

preco = float(input("Digite o preço do produto: "))
total = preco - (preco * 0.10)

print("Preço total com desconto de 10% é", total)