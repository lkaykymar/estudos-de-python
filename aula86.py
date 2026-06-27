# List comprehension em python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

# Se eu quisesse gerar uma lista assim: print(list(range(10)))
# Uma maneira de fazer

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# Fazendo esse mesmo código usando list comprehension
lista2 = [numero for numero in range(10)]
print(lista2)

# Podemos fazer operações dentro dessa lista
lista3 = [numero * 2 for numero in range(10)]
print(lista3)