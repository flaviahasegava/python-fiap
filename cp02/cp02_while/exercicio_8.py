import os
os.system("cls")

# Analisador de números

positivos = 0
negativos = 0
pares = 0
impares = 0
soma = 0
maior = 0
menor = 0
quantidade = 0

while True:
  numero = int(input("Número: "))

  if numero == 0:
    break

  elif numero > 0:
    positivos += 1
  
  elif numero < 0:
    negativos += 1

  if numero % 2 == 0:
    pares += 1
    
  else:
    impares += 1

  soma += numero

  if quantidade == 0:
    maior = numero
    menor = numero
  
  else:
    if numero > maior:
      maior = numero
      
    if numero < menor:
      menor = numero

  quantidade += 1

if quantidade == 0:
  print("Número inválido!")
  
else:
  print(f"""
  Positivos: {positivos}
  Negativos: {negativos}
  Pares: {pares}
  Ímpares: {impares}
  Soma: {soma}
  Maior: {maior}
  Menor: {menor}
  """)