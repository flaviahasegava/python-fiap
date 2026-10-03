import os
os.system("cls")

mes = int(input("Qual o número do mês? "))

match mes:
    case 1 | 2 | 3:
        print("Primeiro trimestre")

    case 4 | 5 | 6:
        print("Segundo trimestre")

    case 7 | 8 | 9:
        print("Terceiro trimestre")

    case 10 | 11 | 12:
        print("Quarto trimestre")
        
    case _:
        print("Mês inválido")