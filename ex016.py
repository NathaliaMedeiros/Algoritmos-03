"""
Ler o valor correspondente ao salário mensal de um trabalhador e o valor do percentual de reajuste a ser atribuído.
Apresentar o novo valor de salário
"""

SalarioMensal = float(input('Digite o valor do saláro mensal: R$'))

percentual = float(input('Digite o valor do percentual de reajuste: '))
percentual = percentual / 100

print(f'O novo avlor de salário é {SalarioMensal * (1 + percentual)}')
