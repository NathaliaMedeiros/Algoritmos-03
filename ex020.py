"""
Calcular e apresentar, em metros por segundo, o valor da velocidade de um projétil que percorre uma determinada
distancia em quilometros a um determinado espaço de tempo em minutos.
"""


distance = float(input('Quantos km o projétil percorreu? '))
time = float(input('Quanto tempo durou? '))
velocity =  (distance * 1000) / (time / 60)

print(f'A velocidade, em metro por segundo, é {velocity} m/s')
