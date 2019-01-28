#desafio 35
reta1=float(input('Informe o tamanho da 1º reta:'))
reta2=float(input('Informe o tamanho da 2º reta:'))
reta3=float(input('Informe o tamanho da 3º reta:'))

if ((reta1+reta2)>reta3) and ((reta2+reta3)>reta1) and ((reta1+reta3)>reta2):
	print('Forma um triângulo!')
else: 
	print('Não forma um triângulo!!')
