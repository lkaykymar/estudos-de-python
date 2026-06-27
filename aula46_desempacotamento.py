'''
Introduçõ ao desempacotamento 
todo iterável você pode desempcotar
criar variáveis para exrair os valores da lista
'''
# o número de valores e variáveis deve ser igual
lista = ['kayky', 'Lourenço', 'martins']
nome1, nome2, nome3 = lista
print(nome2)

# Assim também funciona
nome1, nome2, nome3 = ['kayky', 'Lourenço', 'martins']
print(nome3)

# Caso queira pegar valores específicos, ocê deve fazer algo com o resto
nome1, *resto = ['kayky', 'Lourenço', 'martins']
print(nome1)
print(resto)

# Geralmente se usa _
nome1, *_ = ['kayky', 'Lourenço', 'martins']
print(nome1)
print(_)

_, nome2, *_ = ['kayky', 'Lourenço', 'martins']
print(nome2)

