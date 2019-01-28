#desafio 29
velocidade=float(input('Escreva a velocidade do seu carro em km/h:'))

if velocidade>80:
	multa=(velocidade-80)*7
	print('A multa vai custar {}' .format(multa))
else:
	print('Respeitou a leis de transito, Parabéns!!!')
print('DETRAN')