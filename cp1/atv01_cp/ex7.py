"""
PROBLEMA: 
Dado um valor, calcular e exibir o próximo múltiplo de 5.
Entrada: 12
Saída: O próximo múltiplo de 5 após 12 é 15
"""
# - Digitar o valor
valor = int(input("Digite um valor: "))
# Calcula o próximo múltiplo de 5
proximo_multiplo = valor + (5 - (valor % 5))
# - Calcular e exibir múltiplo de 5
print("O próximo múltiplo de 5 é: ", proximo_multiplo)

Imagine que os múltiplos de 5 são paradas de ônibus localizadas exatamente a cada 5 quilômetros (km 5, 10, 15, 20...). Se você está no km 12, a fórmula calcula a distância exata até a próxima parada.

Onde você está (valor % 5): O símbolo % descobre a sobra de uma divisão. Ao dividir 12 por 5, o resto é 2. Na prática, isso avisa que você já andou 2 quilômetros desde a última parada (que era no km 10).

O que falta caminhar (5 - ...): Como as paradas acontecem a cada 5 km e você já andou 2 km, a conta faz 5 - 2 = 3. Faltam exatos 3 quilômetros para chegar na próxima.

O destino final (valor + ...): A fórmula pega o local exato onde você está agora (12) e soma com o trecho que falta caminhar (3). Ao fazer 12 + 3, o código te entrega o resultado 15.


