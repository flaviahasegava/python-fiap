"""
6. Dada a temperatura em Fahrenheit, calcular e exibir o equivalente em 
Celsius. (Fórmula: C = (F − 32) × 5/9)
Entrada: F = 98.6
Saída: 98.6°F equivalem a 37.0°C
"""

Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9
print(Fahrenheit, "°F equivalem a", Celsius, "°C")