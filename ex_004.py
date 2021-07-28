"""
Efetuar o calculo da quantidade de litros de combustivel gasto em uma viagem, utilizando um automovel que faz
12 KM por litro. Para obter o calculo, o usuario deve fornecer o tempo gasto e a velocidade media durante a viagem.
"""

T = int(input('Quantos minutos durou a viagem: '))
T = T / 60

VM = int(input('Qual a velocidade media da viagem? '))

D = T * VM

L = D / 12

print('Velocidade média: %s \nTempo gasto na viagem: %s \nDistância percorrida: %s km \n'
      'Litros utilizados na viagem: %.2f' % (VM, T, D, L))


