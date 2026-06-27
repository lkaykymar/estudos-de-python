#isinstance serve pra ver se um objeto é de determinado tipo ( é instância de)
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Kayky'}]
for item in lista:
    print(item, isinstance(item, set)) # Aqui diz: item, é um int?
print( )
# podemos usar condições e afins

for item in lista:
    if isinstance(item, set): # se o item for set adicione um 5 na lista
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
    print( )
    
    if isinstance(item, str): # Se for ua str, deixe maiúsculo 
        print('STR')
        print(item.upper())
    print( )
    
    if isinstance(item, (int, float)): # Se o item for str ou float, multiplique por 2
        print("NUM")
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)


