import os
os.system("cls")

regiao_entrega = input("Qual a sua região de entrega? ").strip().lower()
valor_compra = float(input("Qual o valor da compra? "))

match regiao_entrega:
    case "norte" | "nordeste" | "sul" | "sudeste" if valor_compra >= 200:
        print("Frete grátis!")

    case "sul" | "sudeste":
        print("R$ 20,00 de frete")

    case "norte" | "nordeste":
        print("R$ 30,00 de frete")

    case _: 
        print("Região ou valor da compra inválido")