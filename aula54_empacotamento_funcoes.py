# Desempacotamente em chamadas de métodos e funções

string = 'ABCD'
lista = ['maria', 'helena', 1, 2, 3, 'eduarda']
tupla = 'python', 'é', 'legal'

a, b, *_, u = lista
print(a, b, u)

print(*lista)
print(*string)
print(*tupla)

# Melhor de enxergar

print(*lista, sep='\n')

