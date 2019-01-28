#desafio 28
import random
usuario=int(input('Chute um número entre 0 a 5:'))

computer=random.randint(0,5)

if usuario==computer:
	print('Parabéns usuário, você acertou!!!')
else:
	print('Lamento, tente outra vez.')