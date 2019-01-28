#desafio 17
import math
opst=float(input('Informe o comprimento do cateto oposto:'))
adj=float(input('Informe o comprimento do cateto adjacente:'))
print('De acordo com o seus dados, o hipotenusa é igual a {}' .format(math.sqrt((opst*opst)+(adj*adj))))
print('De acordo com o seus dados, o hipotenusa é igual a {}' .format(math.hypot(opst,adj)))