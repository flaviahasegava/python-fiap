"""
PROBLEMA: 
Dada a temperatura em Fahrenheit, calcular e exibir o equivalente em Celsius
Fórmula: C = (F - 32) * 5/9)
Entrada: F = 98.6
Saída: 98.6°F equivalem a 37.0°C
"""
# - Digitar a temperatura em Fahrenheit
temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
# - Calcular e transformar a temperatura em Celsius
temp_celsius = (temp_fahrenheit - 32) * 5/9
# - Exibir o resultado 
print(temp_fahrenheit, "°F equivalem a ", temp_celsius, "°C")
