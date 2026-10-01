import os
os.system("cls")

'''
9. Temperatura de alerta 
Solicite uma temperatura. Informe "Alerta de temperatura" se o valor for menor que 10 OU maior que 35. Caso 
contrário, informe "Temperatura dentro da faixa". 
'''

# Solicitar a temperatura
temperatura = float(input("Informe a temperatura atual: "))
# Verificar se a temperatura for menor que 10 ou maior que 34 e informar o alerta
if temperatura <= 10 or temperatura > 35:
    print("Alerta de temperatura")
else:
    print("Temperatura dentro da faixa")