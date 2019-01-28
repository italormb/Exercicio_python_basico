#desafio 32
ano=int(input('Digite o ano: '))
if (ano%4==0) and (ano%100!=0):
	print('Esse é um ano Bissexto')
else:
	print('Não é um ano bissexto')