import os
os.system("cls")

nota = int(input("Digite a sua nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida")

elif nota >= 7:
    print("Aprovado")

elif nota <= 6:
    print("Recuperação")
    
else:
    print("Reprovado")    