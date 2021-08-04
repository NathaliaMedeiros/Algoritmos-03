"""
Elaborar um programa que apresente o valor da conversão em real de um valor lido em dolar.
Solicite a cotação do dólar.
"""

dolar = float(input('Quantos dolares deseja converter? '))
price = float(input('Qual a cotação do dolar hoje? '))

print(f'US${dolar} convertido em reais é igual a R${dolar * price}')

