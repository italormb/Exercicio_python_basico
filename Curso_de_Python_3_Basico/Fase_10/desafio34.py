#desafio 34
salario=float(input('Informe seu salário: '))

if salario>1250:
	print('Seu sálario sera: {} com aumento de 15%' .format(salario*1.15))
else:
	print('Seu sálario sera: {} com aumento de 10%' .format(salario*1.1))