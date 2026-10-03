import os
os.system("cls")

idade = int(input("Digite a sua idade: "))

match idade:
    case x if x < 0:
        print("Idade inválida")

    case x if x < 13:
        print("Criança")

    case x if x < 18:
        print("Adolescente")

    case x if x < 60:
        print("Adulto")

    case _:
        print("Idoso")