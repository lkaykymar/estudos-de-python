p1 = {
    'nome': 'kayky',
    'sobrenome': 'Lourenço',
    'idade': 18,

}
print(p1['nome'])

# Get obtém uma chave, você pode passar um valor padrão

print(p1.get('nome'))
print(p1.get('idade', 'Não existe'))

# Pop apaga um item com a chave espeficicada (del)
nome = p1.pop('nome')
print(nome)
print(p1)

#popitem - Apaga a última chave do dicionário
idade = p1.popitem()
print(idade)
print(p1)

# Update atualiza o dicionário
p1.update({
    'nome': 'novo valor',
    'estado civil': 'solteiro'


})

print(p1)