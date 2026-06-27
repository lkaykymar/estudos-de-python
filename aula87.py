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

# Quero mapear os valores dessa lista para outro com preços diferentes
produtos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [produto for produto in produtos]

print(*novos_produtos, sep='\n')

# Posso mapear somente o nome, ou o valor
produtos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [produto['preco'] for produto in produtos]

print(*novos_produtos, sep='\n')

# Posso criar um dicionário
produtos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [{"nome": produto["nome"], 'preco': produto["preco"]} for produto in produtos]

print(*novos_produtos, sep='\n')

# Forma mais simples, desempacotando
produtos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [{**produto, 'preco': produto["preco"] * 1.05} 
                  if produto['preco'] > 20 else {**produto}
                  for produto in produtos]

print(*novos_produtos, sep='\n')

# Usando uma condição para manipular os preços
