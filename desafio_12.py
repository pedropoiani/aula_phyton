#Faça um programa que leia a largura a a altura de uma parada am metros, calcule a 
#sua Árca ga quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta. pinta uma área de 2m².

alt=float(input('Qual a Altura da Parede: '))
larg=float(input('Qual a Largura da Parede: '))
area=alt*larg

print(f'A Area total é de {area} m² e a quantidade de tinta é {area/2} litros')
