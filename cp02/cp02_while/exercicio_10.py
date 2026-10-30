import os
os.system("cls")

# Controle de estoque e vendas

produto = input("Produto: ")
preco = float(input("Preço: R$ "))
estoque = int(input("Estoque inicial: "))

total_vendido = 0

while True:
  print(f"""
  CONTROLADOR DE ESTOQUE E VENDAS
  ================================
  1 - Consultar
  2 - Repor
  3 - Vender
  4 - Sair
  ================================
  """)

  opcao = input("Escolha uma opção: ")

  match opcao:
    case "1":
      print(f"\nEstoque atual: {estoque} unidades")

    case "2":
      qtd = int(input("\nReposição: "))
      
      if qtd > 0:
        estoque += qtd
            
      else:
        print("Quantidade inválida! Digite um valor maior que zero.")

    case "3":
      qtd = int(input("\nVenda: "))
      
      if qtd <= 0:
        print("Quantidade inválida! Digite um valor maior que zero.")
      
      elif qtd > estoque:
        print("Estoque insuficiente!")
           
      else:
        estoque -= qtd
        total_vendido = total_vendido + (qtd * preco)

    case "4":
      print("Saindo...")
      break

    case _:
      print("Opção inválida!")

print(f"""
Estoque restante: {estoque} unidades
Valor total vendido: R$ {total_vendido:.2f}
""")