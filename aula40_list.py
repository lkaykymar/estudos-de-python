'''
Listas em python
tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +

'''

string = 'ABCDE' # 5 caracteres

lista = list() # Serve pra converter mas não é muito usada
lista_ = [] # Colchetes faz isso ser uma lista
print(f'{type(lista_)}\n')
print(f'{bool(lista_)}\n') # se estiver vazia é falsa


# Varios tipos de dados em ma única lista
lista_1 = [123, True, 'Kayky Lourenço', 18.5,]
print(f'Lista com vários tipos: {lista_1}\n')

# Lista dentro de outra lista
lista_2 = [123, True, ['Kayky', 'Júlia', 18.1], 45.5]
print(f'Lista dentro de outra lista: {lista_2}\n')

# É possível acessar o elemento por índice
lista_3 = [123, True, ['Kayky', 'Júlia', 18.1], 45.5]
print(f'Acessando por índice: {lista_3[2]}\n')

# A lista interna conta como um elemento
lista_4 = [123, True, ['Kayky', 'Júlia', 18.1], 45.5]
print(f'O tamanho da lista 4 é: {len(lista_4)}\n')

# É possível manipular individualmente cada elemento da lista
lista_5 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
print(f'{lista_5[3].upper()}\n')

# É possível alterar os valores dentro da lista (Por isso é mutável)
lista_6 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
lista_6[3] = 'Martins'
print(f'Lista_6 com índice 3 alterado: {lista_6}\n')

# Voce pode atribuir uma lista a uma variável
lista_7 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
posicao_2 = lista_7[2]
print(f'Pegando um elemento da lista pela variável: {posicao_2}\n')




