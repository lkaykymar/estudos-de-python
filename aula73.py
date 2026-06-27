# Métodos úteis dos dicionários em Python, dicionários são objetos
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro



### Quando você cria chaves iguais, ele usa o valor da última
pessoa = {
    'nome': 'Kayky',
    'sobrenome': 'Martins',
    'sobrenome': 'Martins',
    'sobrenome': 'Lourenço'
}

print(pessoa['sobrenome'])

### Len conta quantas chaves tem no dicionário
print(len(pessoa))

### Keys vai retorna as chaves e podemos fazer a coersão
print(pessoa.keys())
print(list(pessoa.keys()))
print(tuple[pessoa.keys()])

### Podemos fazer um for
for chave in pessoa:
    print(chave)

### Podemos pegar os valores com valuess
print(list(pessoa.values()))

### Podemos fazer um for para os valores
for valor in pessoa.values():
    print(valor)

### podemos pegar chaves e valores com items
print(list(pessoa.items()))

### Podemos usar o for no items também
for chave, valor in pessoa.items():
    print(chave, valor)

### setdefault serve para dar um valor padrão a uma chave que possivelmente não exista no dicionário, tipo o get
pessoa.setdefault('estado civil', 0) # Se tivesse um estado  civil, o zero não seria utilizado
print(pessoa['estado civil'])
