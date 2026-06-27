v1 = 'a'
v2 = 'a'
v3 = 'c'
v4 = 'd'
# Apesar de serem duas variáveis, o interpretador pode apontar para o mesmo lugar

print(id(v1))
print(id(v2))

print('--------------------')

print(id(v3))
print(id(v4))

