# for interno na lista normal
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# for interno na lista comprehension
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
    ]

# lista comprehension interna
print(lista)
lista = [
    [letra for letra in 'Kayky']
    for x in range(3)

]
print(lista)