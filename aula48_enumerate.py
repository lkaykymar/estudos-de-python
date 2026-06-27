# enumerate serve pra numerar listas
lista_ = ['kayky', 'Lourenço', 'martins']
lista_enumerada = enumerate(lista_)
print(lista_enumerada)

# Corrigindo com o for
lista = ['kayky', 'Lourenço', 'martins']
lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

# O iterator ja foi gasto, portando não vai aparecer nada no seguinte print:
print('O que tem na lista enumerada: ', lista_enumerada)

# Corrigindo com conversão
lista1 = ['kayky', 'Lourenço', 'martins']
lista1_enumerada = list(enumerate(lista1))
print(lista1_enumerada)

# Passando um start
lista2 = ['kayky', 'Lourenço', 'martins']
lista2_enumerada = list(enumerate(lista2, start = 10))
print(lista2_enumerada)

# Desempacotando 
lista3 = ['kayky', 'Lourenço', 'martins']
for indice, nome in enumerate(lista3):
    print(indice, nome)







