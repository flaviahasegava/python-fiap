import os
os.system("cls")

medida1 = float(input("Primeira medida: "))
medida2 = float(input("Segunda medida: "))
medida3 = float(input("Terceira medida: "))

if medida1 < 0 and medida2 < 0 and medida3 < 0:
    print("Medida inválida")

elif medida1 == medida2 and medida1 == medida3:
    print("Triângulo equilátero")

elif medida1 == medida3 or medida1 == medida2:
    print("Triângulo isósceles")

else:
    print("Triângulo Escaleno")