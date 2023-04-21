import random
n1=str(input('Qual primeiro nome?  '))
n2=str(input('Qual o segundo nom?  '))
n3=str(input('Qual o tercerio nome?'))
lista = [n1, n2, n3]
print(f'O aluno escolhido foi {random.choice(lista)}')

