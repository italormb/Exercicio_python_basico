#==========================================================================================================
#Nome: Ítalo Rodrigo Moreira Borges
# Data: 06/10/2018
#==========================================================================================================
# Desafios
num=int(input('5- Digite um numero ai:'))
print('5 -O desafio do sucessor e antecessor desse numero e: {} e {}' .format(num-1,num+1))
print('6 - O desafo do multiplo de 2: {} , 3: {} e raiz quadrada: {} ' .format(2*num,3*num, num**0.5))
nota1=int(input('7 - entra com sua primeira nota:'))
nota2=int(input('7 - entra com sua segunda nota:'))
print('7 - A nota 1: {} e note 2: {}, a médio do aluno é: {}' .format(nota1,nota2,(nota1+nota2)/2))
alt=float(input('8- Qual a sua altura em metros?'))
print('8 -A sua altura em milimetros: {} mm e sua altura em centimetros: {} cm'.format(alt*1000,alt*100))
ta = int(input('9 - digite um numero para informar a tabuada:'))
print('9 - Tabuado do numero e: {}x0 = {} \n {}x1 = {} \n {}x2= {} \n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {}x6= {} \n {}x7= {} \n {}x8= {} \n {}x9= {} \n {}x10 = {} \n' 
	.format(ta,ta*0,ta,ta*1,ta,ta*2,ta,ta*3,ta,ta*4,ta,ta*5,ta,ta*6,ta,ta*7,ta,ta*8,ta,ta*9,ta,ta*10))
real=float(input('10 - digite o dinheiro na sua carteira em reais para eu informar em dolares: '))
print('10 -O seu dinheiro em US${:.5f}' .format(real/3.27))
a=float(input('11-informe a altura da sua parede em (m)? '))
b=float(input('11-informe a base da parede em (m)?'))
print('11-A area da sua parede é: {} m² e vai gastar um total de: {} litros de tinta' .format(a*b, a*b/2))
var12= float(input('12 - Qual o preço do produto?'))
print('12 - O produto teve um desconto de 5%, logo ele custa: R${} ' .format(var12*0.95))
var13=float(input('13- Qual o seu saláro?'))
print('13 - Com aumento de 15%, o seu novo salário será: R$ {}' .format(var13*1.15))