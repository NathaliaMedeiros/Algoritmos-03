# Efetuar o calculo e a apresentacao do valor de uma prestacao em atraso

valor = float(input('Qual o valor atual em atraso? R$'))
tempo = int(input('Há quantos meses a parcela está atrasada? '))
taxa = float(input('Qual o valor da taxa de juros? '))

prestacao = valor + (valor * (taxa / 100) * tempo)
print('O valor da prestação é R$', prestacao)

