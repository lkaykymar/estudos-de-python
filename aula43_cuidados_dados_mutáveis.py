'''
Cuidados com dados mutáveis

= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

'''

nome = 'Kayky'
noutra_variavel = nome
nome = 'Martins'

print(nome)
print(noutra_variavel)

####################################################################################################

lista_a = ['kayky', 'martins']
lista_b = lista_a # lista a não foi copiada, as duas variáveis apontam para um mesmo valor
lista_a[0] = 'Qualquer coisa'
print(lista_b) # Como é um valor para as duas, oq voce mudar em uma, muda na outra

####################################################################################################

# O copy copia o valor para a outra variável, portanto se mudar um não muda o outro
lista_5 = ['kayky', 'martins']
lista_6 = lista_5.copy() # lista a não foi copiada, as duas variáveis apontam para um mesmo valor
print(lista_6)
lista_5[0] = 'Marianna'
print(lista_6)





