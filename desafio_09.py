#Escreva um programa que leia um valor em metros e o axiba convertido em 
#quilômetros,hectometros, decametro, decimetros, centimetros e milímetros.

num=float(input('Digite o Valor em Metros: '))
km= num/1000
hm= num/100
dam= num/10
dm= num*10
cm= num*100
mm= num*1000
print(f'Quilometros; {km}\nHectometro{hm}\nDecametro; {dam}\nDecimetros{dm}\nCentimetro{cm}\nMilimetros{mm}')