"""
PROBLEMA: 
Dada a temperatura em Celsius, calcular e exibir o equivalente em Fahrenheit
Fórmula: F = (C * 9/5) + 32)
Entrada: C = 25
Saída: 25°C equivalem a 77.0°F
"""
# - Digitar a temperatura em Celsius
temp_celsius = float(input("Digite a temperatura em Celsius: "))
# - Calcular e transformar a temperatura em Fahrenheit
temp_fahrenheit = (temp_celsius * 9/5) + 32
# - Exibir o resultado 
print(temp_celsius, "°C equivalem a ", temp_fahrenheit, "°F")
