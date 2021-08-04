"""
Ler dois valores inteiros e apresentar o resultado do quadrado da diferença do primeiro valor pelo segundo
"""

a = int(input('Digite o primeiro valor: '))

b = int(input('Digite o segundo valor: '))

result = a * a - (2 * a * b) + (b * b)

print(f'A diferença do quadrado entre {a} e {b} é {result}')

