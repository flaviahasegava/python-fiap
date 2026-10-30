import os
os.system("cls")

# Média da turma

soma = 0
qtd_notas = 0
nota = 0

while nota != -1:
    nota = float(input("Nota: "))

    if nota == -1:
        break

    elif nota < 0 or nota > 10:
        print("Nota inválida!")
        continue

    qtd_notas += 1
    soma = soma + nota

media = soma / qtd_notas

if media <= 4:
    classificacao = "Insuficiente"

elif media <= 6:
    classificacao = "Regular"

elif media <= 8:
    classificacao = "Boa"

elif media <= 10:
    classificacao = "Excelente"

print(f"""
Quantidade de notas: {qtd_notas}
Média da turma: {media:.2f}
Classificação: {classificacao}
""")