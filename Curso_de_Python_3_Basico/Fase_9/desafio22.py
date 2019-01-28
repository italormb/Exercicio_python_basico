#desafio 22
nome=str(input('Digite seu nome:'))
#nome completo maiusculo
print('O nome da pessoa em maiúsculo é {}' .format(nome.upper()))
#nome completo minusculo
print('O nome da pessoa em maiúsculo é {}' .format(nome.lower()))
#tamnho da letea da pessoa semcontar os espaços
print('O tamanho do nome das pessoas sem espaço é {}' .format(len(nome)-nome.count(' ')))
divisao=nome.split()
print('Quantas letras tem o primeiro nome: {}' .format(len(divisao[0])))