#desafio 33
num1=int(input('Digite um número: '))
num2=int(input('Digite um número: '))
num3=int(input('Digite um número: '))

if (num1>num2) and (num1>num3):
	print('Número {} é o maior' .format(num1))
	if num2<num3:
		print('Número {} é o menor' .format(num2))
	if num2>num3:
		print('Número {} é o menor' .format(num3))	
if (num2>num1) and (num2>num3):
	print('Número {} é o maior' .format(num2))
	if num1<num3:
		print('Número {} é o menor' .format(num1))
	if num1>num3:
		print('Número {} é o menor' .format(num3))	
else:
	print('Número {} é o maior' .format(num3))
	if num1<num2:
		print('Número {} é o menor' .format(num1))
	if num1>num2:
		print('Número {} é o menor' .format(num2))	
