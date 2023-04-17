#faça um programa que leia um angulo e calcule
#Para encontrar os valores do seno, cosseno e tangente

import math
angulo = float(input('Qual o Angulo?'))
print(f' Seno: {math.sin(math.radians(angulo)):.2f}')
print(f' Cosseno: {math.cos(math.radians(angulo)):.2f}')
print(f' Tangente: {math.tan(math.radians(angulo)):.2f}')
