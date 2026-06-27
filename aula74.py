# A lista tem o método copy e o dicionário também
# Shallow copy quer dizer cópia rasa
# Deep copy quer dizer cópia profunda

import copy

pessoa = {
    'nome': 'Kayky',
    'sobrenome': 'Martins',
    'sobrenome': 'Martins',
    'sobrenome': 'Lourenço'
}

'''Quando utiliza essa atribuição com valores mutáveis, 
a atribuição não faz uma cópia para pessoa2,
apenas diz que pessoa2 aponta para o mesmo 
lugar que pessoa.
Isso significa que se eu alterar a pessoa2
pessoa também será alterada'''

pessoa2 = pessoa

pessoa2['estado civi'] = 'Solteiro'
print(pessoa)

### Para isso temos o método copy de dentro do dicionário, que faz a cópia rasa
dicionario = {
    '1': 'A',
    '2': 'B',
    'lista': [0, 1, 2, 3]
}

dicionario2 = dicionario.copy()  

dicionario2['3'] = 'C'

print(dicionario2)
print(dicionario)

# A cópia é rasa pois ele não copia subníveis dentro do dicionário como listas
# portanto, o que é alterdo em um é alterado no outro
dicionario2['lista'][1] = 9999999
print(dicionario2)
print(dicionario)

### Para corrijir tal problema, usamos o módulo copy, import copy
### Dentro desse módulo temos a shallow copy também, que seria copy.copy no lugar de copy do bloco anterior
### Mas dentro do módulo copy, temos o deep copy, que vai fazer a cópia profunda dos dubníveis do dicionário

dic = {
    'marca': 'nike',
    'tamanho': 'M',
    'valores': [0, 100, 200, 300]
}

dic2 = copy.deepcopy(dic)  

dic['valores'][1] = 999999

print(dic)
print(dic2)
