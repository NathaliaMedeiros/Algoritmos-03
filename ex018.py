"""
Em uma eleição sindical concorreram ao cargo de presidente trés candidatos(A, B e C). Durante a apuracão dos votos foram
computados votos nulos e votos em branco, além dos votos válidos para cada candidato. Deve ser criado um programa de
computador que efetue a leitura da quantidade de votos válidos para cada candidato, além de efetuar também a leitura
da quantidade de votos nulos e votos em branco.
Ao final o programa deve apresentar o número total de eleitores,considerando votos válidos em relação à quantidade de
eleitores;o percentual correspondente de votos valido do candidato A em relação a quantidade de eleitores;
o percentual correspondente de votos válidos do candidato B em relação à quantidade de eleitores; o percentual
correspondente de votos validos do candidato C em relação à quantidadede eleitores; o percentual de votos em nulos em
relação à quantidade de eleitores; e por ultimo o percentual correspondente de votos em branco em relação à quantidade
de eleitores.
"""


a = int(input('Quantos votos o candidato A recebeu? '))
b = int(input('Quantos votos o candidato B recebeu? '))
c = int(input('Quantos votos o candidato C recebeu? '))
branco = int(input('Quantos votos foram branco? '))
nulo = int(input('Quantos votos foram nulos? '))
total = a + b + c + branco + nulo


print(f'Número total de eleitores: {total}')
print(f'Número total de votos válidos: {a + b + c}')
print(f'Porcentagem de votos válidos do candidato A: {a * 100 / total}')
print(f'Porcentagem de votos válidos do candidato B: {b * 100 / total}')
print(f'Porcentagem de votos válidos do candidato C: {c * 100 / total}')
print(f'Percentual de votos brancos: {branco * 100 / total}')
print(f'Percentual de votos nulos: {nulo * 100 / total}')

