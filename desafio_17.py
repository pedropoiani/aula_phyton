#Faça um programa que leia o comprimento do cateto oposto a do cateto adjacente de um
#triângulo retângulo. calcule & mostra o comprimento da hipotenusa.
import math
from math import sqrt, pow, hypot
c1 = float(input('Qual o cateto oposto? '))
c2 = float(input('Qual o cateto adjacente? '))
h = sqrt(pow(c1, 2) + pow(c2, 2))
print(f' A hipotenusa é: {h:.2f}')

'''Outra forma de fazer'''

h2 = hypot(c1, c2)
print(f'{h2:.2f}')

