# Manipulando chaves e valores do dicionário

# Dicionário vazio
pessoa = {}
print(pessoa)

# Criando uma chave inexistente
pessoa['nome'] = 'Kayky'
print(pessoa)
print(pessoa['nome'])

# Podemos usar chaves dinâmicasn que podem ser alteradas na variável
chave = 'Anos de idade' # isso pode ser alterado sem gerar erro
pessoa[chave] = '21 anos'
print(pessoa)
print(pessoa[chave])

# Pra alterar o valor da chave é a mesma coisa,  altere na variável também
pessoa[chave] = '30 anos de idade'
print(pessoa[chave])

# Para apagar uma chave use o del
pessoa['sobrenome'] = 'Martins'
print(pessoa)
del pessoa['sobrenome']
print(pessoa)

# Como conferir se algo está no dicionário, use o método get
if pessoa.get('sobrenome') is None:
    print('NÃO existe')
else:
    print('Existe')
