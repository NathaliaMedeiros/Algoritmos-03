"""
Ler uma temperatura em Celsius e apresentá-la convertida em Fahrenheit.
F = (9 * C + 160) / 5
"""

C = int(input('Entre com uma temperatura em Celsius: '))

F = (9 * C + 160) / 5

print('%s convertido para Fahrenheit são %r graus' %(C, F))