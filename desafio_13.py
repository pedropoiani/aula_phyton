#Faça um algoritmo que leia o preso de um produto a mostre seu novo preso, com 5% de desconto.

valor=float(input('Qual o preço do produto ?'))
desconto = (valor*5)/100
print(f'{valor - desconto}') 