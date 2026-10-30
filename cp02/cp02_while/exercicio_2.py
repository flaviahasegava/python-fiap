import os
os.system("cls")

# Calculadora com menu

while True:
  print(f"""
  CALCULADORA (Menu de operações)
  ================================
  + Somar
  - Subtrair
  * Multiplicar
  / Dividir
  0 Sair
  ================================
  """)

  opcao = input("Escolha sua opção: ").strip().lower()

  num1 = float(input("Número 1: "))
  num2 = float(input("Número 2: "))
  
  match opcao:
    case "+" | "somar":
      print(f"\nSOMA\nResultado: {num1 + num2}")

    case "-" | "subtrair":
      print(f"\nSUBTRAÇÃO\nResultado: {num1 - num2}")
    
    case "*" | "multiplicar":
      print(f"\nMULTIPLICAÇÃO\nResultado: {num1 * num2}")

    case "/" | "dividir":
      if num2 == 0:
        print("\nErro! Não é possível dividir por zero.")
      
      else:
        print(f"\nDIVISÃO\nResultado: {num1 / num2}")

    case "0" | "sair":
      print("\nSaindo...")
      break
    
    case _:
      print("\nOpção inválida!")