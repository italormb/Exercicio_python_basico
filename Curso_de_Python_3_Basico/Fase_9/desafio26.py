#desafio 26
nome=str(input('Digite seu nome:'))
qtd=nome.upper().count('A');
print('A quatidadade de vezes que aparece "a": {}' .format(qtd))
print('A indice da primeira ocorrencia de a: {}' .format(nome.upper().find('A')))
print('O ultimo indice de ocorrencia de a: {}' .format(nome.upper().rfind('A')))