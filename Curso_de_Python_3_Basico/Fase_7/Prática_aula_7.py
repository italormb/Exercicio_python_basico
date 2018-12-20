var1=int(input('Digite o primeiro valor:'))
var2=int(input('Digite o segundo valor:'))
#Adição
print('O resultado da soma=', (var1+var2), end= ' ')
#Subtração
print('O resultado da subtração=', (var1-var2))
#Multipicação
print('O resultado da multiplicação=', (var1*var2))
#Divisão
print('O resultado da divisão= {:.4f}' .format((var1/var2)))
#Potencia
print('O resultado da potencia=', (var1**var2))
#Divisão inteira
print('O resultado da divisão inteira=', (var1//var2))
#Resto da divisão
print('O resultado do resto da divisão=', (var1%var2))
############Utilizando operandos não numericos###############
nome=str(input('Qual é sue nome?'))
print('o seu nome é:{:5}!' .format(nome) )
print('o seu nome é:{:>5}!' .format(nome) )
print('o seu nome é:{:<5}!' .format(nome) )
print('o seu nome é:{:=^5}!' .format(nome) )