# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    "nome": "Kayky",
    "sobenome": "Martins"
}

dados_pessoa = {
    "idade": 45,
    "Altura": 1.83
}


# Aqui ele empacota as chaves
a, b = pessoa
print(a, b)

# Aqui ele empacota os valores
a, b = pessoa.values()
print(a, b)

# usando for
for chave, valor in pessoa.items():
    print(valor, chave)

# Extraindo dados de um dicionário para outro

dados_completos = {**pessoa, **dados_pessoa, "Estado Civil": "Solteiro"}
print(dados_completos)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
# Podemos usar em funções os dicionários com argumentos nomeados
# Estamos empacotando os argumentos no kwargs
def mostra_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(1, 2, nome="Joana", qualquer= 123)

# Em vez de jogar muitos argumentos, crie um dicionário e mande pra função

configuracoes = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4
}

mostra_argumentos_nomeados(**configuracoes)