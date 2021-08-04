"""
Ler uma temperatura em Fahrenheit e apresentá-la convertida em Celsius.
C = (F - 32) * (5 / 9)
"""

F = float(input('Entre com uma temperatura em Fahrenheit: '))

C = (F - 32) * (5 / 9)

print('%s graus Fahrenheit são %.2f graus Celsius' % (F, C))
