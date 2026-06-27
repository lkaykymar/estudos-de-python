"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

### Solução do Kayky

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

import copy

def encontra_duplicatas(lista):

# Capturando os elementos com cópias
    lista_sem_duplicatas = set(lista)
    lista_de_copias = []
    lista_unicos = []
    for i in lista_sem_duplicatas:
        quantidade = lista.count(i)
        if quantidade >= 2:
            lista_de_copias.append(i)
        else:
            lista_unicos.append(i)
    
    if len(lista_de_copias) == 0:
        return -1

# Removendo os originais e deixando as cópias
    lixeira = []
    nova_lista = lista.copy()
    for i in range(len(lista)):
        pivo = lista[i]
        if pivo in lista_de_copias and pivo not in lixeira:
            lixeira.append(pivo)
            nova_lista.remove(pivo)
    #return lista_de_copias, lixeira, nova_lista

# Pegando a primeira cópia
    for i in nova_lista:
        if i in lista_de_copias:
            return lista, lista_de_copias, lixeira, nova_lista, "Primeira cópia: ", i
    
for lista in lista_de_listas_de_inteiros:
    print(encontra_duplicatas(lista))

### Solução do otávio

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )











