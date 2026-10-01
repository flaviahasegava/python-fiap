import os
os.system("cls")

# - Digitar uma quantidade de minutos
qtd_minutos = int(input("Qual a quantidade em minutos? "))
# - Calcular o tempo em horas/minutos
horas = qtd_minutos // 60 
minutos =  qtd_minutos % 60
# - Exibir o resultado
print(f"Tempo: {horas}h{minutos}m")