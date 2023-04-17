#Faça um programa que leia o comprimento do cateto oposto a do cateto adjacente de um
#triângulo retângulo. calcule & mostra o comprimento da hipotenusa.

from math import sqrt, pow
c1 = float(input('Qual o cateto oposto? '))
c2 = float(input('Qual o cateto adjacente? '))
h = sqrt(pow(c1, 2)+ pow(c2, 2))
print(f'{h}')

