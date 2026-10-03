import os
os.system("cls")

idade = int(input("Qual a sua idade? "))

if idade <= 0:
    print("Idade inválida")

elif idade <= 5:
    print("Ingresso grátis!")

elif idade >= 6 and idade <= 12:
    print("Preço do ingresso: R$ 10,00")

elif idade >= 13 and idade <= 59:
    print("Preço do ingresso: R$ 25,00")

else:
    print("Preço do ingresso: R$ 12,00")