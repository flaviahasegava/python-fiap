import os
os.system("cls")

# Apuração de votos

i = 0
projeto1 = 0
projeto2 = 0
projeto3 = 0
brancos = 0
nulos = 0

eleitores = int(input("Eleitores: "))

while True:
  if i == eleitores:
    break

  print(f"""
  VOTAÇÃO DE PROJETOS
  ========================
  1 - Projeto 1
  2 - Projeto 2
  3 - Projeto 3
  0 - Branco
  Outra entrada - Nulo
  ========================
  """)

  voto = input("Escolha seu voto: ")

  match voto:
    case "1":
      projeto1 += 1

    case "2":
      projeto2 += 1

    case "3":
      projeto3 += 1

    case "0":
      brancos += 1

    case _:
      nulos += 1

  i += 1

print(f"""
Projeto 1: {projeto1}
Projeto 2: {projeto2}
Projeto 3: {projeto3}
Brancos: {brancos}
Nulos: {nulos}
""")

if projeto1 > projeto2 and projeto1 > projeto3:
  print("Vencedor: Projeto 1")

elif projeto2 > projeto1 and projeto2 > projeto3:
  print("Vencedor: Projeto 2")

elif projeto3 > projeto1 and projeto3 > projeto2:
  print("Vencedor: Projeto 3")

else:
  print("Empate!")
