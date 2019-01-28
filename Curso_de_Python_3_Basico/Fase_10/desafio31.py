#desafio 31
distancia=float(input('Escreva a distância em km: '))

if distancia<=200:
	preco=(distancia)*0.5
	print('Vai custar R$ {}' .format(preco))
else:
	preco=(distancia)*0.45
	print('Vai custar R$ {}' .format(preco))
print('Governo federal')