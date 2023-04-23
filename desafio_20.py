import random
n1=str(input('Qual o nome: '))
n2=str(input('Qual o nome: '))
n3=str(input('Qual o nome: '))
lista =[ n1, n2, n3]
random.shuffle(lista)
print(f'{lista}')