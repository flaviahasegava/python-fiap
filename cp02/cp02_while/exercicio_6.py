import os
os.system("cls")

# Tabuada personalizada

while True:
  numero_tabuada = int(input("Número: "))

  while True:
    limite = int(input("Limite: "))

    if limite < 1 or limite > 20:
      print("Limite inválido! Digite um número entre 1 e 20.")
    break

  i = 1

  while i <= limite:
    print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")
    i += 1

  while True:
    resposta = input("\nCalcular outra? ").upper()

    if resposta == "S" or resposta == "N":
      break
    
    print("\nResposta inválida! Escolha S ou N.")

  if resposta == "N":
    print("\nPrograma encerrado.")
    break