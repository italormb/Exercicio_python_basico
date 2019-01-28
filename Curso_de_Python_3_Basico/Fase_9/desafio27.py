#desafio 27
nome=str(input('Digite seu nome:'))
divisao=nome.split()
tam=len(divisao)
print('A primeira palavra é: {} e a última palavra é: {}' .format(divisao[0],divisao[tam-1]))