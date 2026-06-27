
# Listas dentro de listas
salas = [['Kayky', 'lourenço', 'martins'], [123, 'joaquim', 'claudio'], 5444]

print(f'Pegando um elemento da lista: {salas[2]}')
print(f'Pegando uma lista dentro da lista salas: {salas[0]}')
print(f'Pegandoum elemento dentro da lista que esta dentro da lista salas: {salas[0][1]}')

# Tupla dentro de listas

salas = [['Kayky', 'lourenço', 'martins'], [123, 'joaquim', 'claudio'], 5444, (0, 10, 20, 30, 40)]
print(f'Pegando um elemento dentro da tuplas: {salas[3][2]}')

# Podemos usar o for

lista = [['Kayky', 'lourenço', 'martins'], ['joaquim', 'claudio']]


for sala in lista:
    print(f'A sala é {sala}')
    for item in sala:
        print(item)