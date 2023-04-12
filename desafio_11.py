#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira G 
#mostra quantos Dólares ela pode comprar.

saldo=float(input('Quanto de real você tem? '))
cota=float(input('Qual a cotação atual do dolar? '))
print(f'Seu saldo em dolar é ${saldo/cota:.2f}')