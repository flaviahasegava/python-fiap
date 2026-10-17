
"""
PROBLEMA: 
Calcular quatro números dado pelo usuário e exibir a média
Entrada: 8, 6, 7, 9
Saída: A média é 7.5
"""
# - Digitar o primeiro número 
num1 = float(input("Digite o primeiro número: "))
# - Digitar o segundo número
num2 = float(input("Digite o segundo número: "))
# - Digitar o terceiro número 
num3 = float(input("Digite terceiro o número: "))
# - Digitar o quarto número 
num4 = float(input("Digite o quarto número: "))
# - Calcular a média
m = (num1 + num2 + num3 + num4)/ 4
# - Exibir o resultado 
print("A média de ", num1, ",", num2, ",", num3, ",", num4, "é", m)
