#Faça um algoritmo que leia o salário de um funcionário e 
#mostra seu novo salário, com 15% de aumento.

valor=float(input('Qual o valor do salário? '))
aumento=(valor*15)/100
print(f'Seu salário foi para: {valor+aumento}')