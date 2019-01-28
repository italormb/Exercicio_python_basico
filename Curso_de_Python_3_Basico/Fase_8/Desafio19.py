# Desafio 19
import random
nome1=str(input('qual o nome do 1º:'))
nome2=str(input('qual o nome do 2º:'))
nome3=str(input('qual o nome do 3º:'))
nome4=str(input('qual o nome do 4º:'))

pos=random.randint(1,4)

#pos=int(input('digita o numero debug no if'))

if pos==1 :
	print('O aluno escolhido é {}'.format(nome1))
if pos==2 :
	print('O aluno escolhido é {}'.format(nome2))
if pos==3 :
	print('O aluno escolhido é {}'.format(nome3))
if pos==4 :
	print('O aluno escolhido é {}'.format(nome4))