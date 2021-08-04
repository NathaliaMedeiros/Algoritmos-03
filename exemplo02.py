"""
Construir um programa que calcule o salario liquido de um professor.
Deve-se conter: valor da hora aula, numero de horas trabalhadas no mês e
percentual de desconto INSS.
Primeiramente, calcular o salario bruto para fazer o desconto e ter o valor liquido
"""

# 1- Estabelecer a leitura da variável HT (horas trabalhadas no mes).

HT = float(input('Quantas horas trabalhou esse mes? '))

# 2- Estabelecer a leitura da variável VH (valor hora aula).

VH = float(input('Digite o valor da hora aula: R$'))

# 3- Estabelecer a leitura da variável PD (percentual de desconto)

PD = float(input('Digite o percentual de desconto: '))

# 4- Calcular o salario bruto (SB), sendo este a multiplicação das variaveis HT e VH

SB = HT * VH
print('Salário bruto: R$', SB)

# 5- Calcular o total de desconto (TD) com base no valor de PD dividido por 100

TD = PD / 100
print('Total de desconto: ', TD)

# 6- Calcular o salário líquido (SL), deduzindo o desconto do salario bruto.

SL = SB * (1 - TD)
print('Salário Liquido: R$', SL)





