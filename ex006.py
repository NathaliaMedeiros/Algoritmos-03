# Ler dois valores para as variáveis A e B e efetuar a troca dos valores

A = int(input('Digite um valor para A: '))

B = int(input('Digite um valor para B: '))

aux = B
B = A
A = aux

print('Valores atualizados: \nA = %s\nB = %s' % (A, B))



