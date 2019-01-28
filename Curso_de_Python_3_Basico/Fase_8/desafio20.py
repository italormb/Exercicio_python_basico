#desafio 20
import random
nome1=str(input('qual o nome do 1º:'))
nome2=str(input('qual o nome do 2º:'))
nome3=str(input('qual o nome do 3º:'))
nome4=str(input('qual o nome do 4º:'))

alunos = [nome1, nome2 ,nome3 ,nome4]

random.shuffle(alunos)

print('A nova ordem: {}' .format(alunos))