'''
+ - concatena listas

'''
# Unindo listas com +
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = lista_1 + lista_2
print(lista_3)

# extend

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)
print(f'Unindo sem a variável e com extend: {lista_a}')

#extend e variável não funciona

lista_d = [1, 2, 3]
lista_e = [4, 5, 6]
lista_f = lista_d.extend(lista_e)
print(f'Unindo com a variável e com extend: {lista_f}')