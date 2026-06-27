# Dicionários em Python (tipo dict)
# Estrutura de dados que geralmente são usadas para colocar coisas que tem atributos
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

### No dicionário, em vez de índices numéricos, usamos nomes de duas maneiras

maneira_1 = {'nome': 'Kayky', 'sobrenome': 'Lourenço', 'idade' : '21', 'estado civil': 'solteiro'}

maneira_2 = dict(nome='Kayky', sobrenome='Lourenço', idade='21', estado_civil='Solteiro')

print('dicionário 1: ', maneira_1)
print('dicionário 2:', maneira_2)
print(f'estado civil no dicionário 1 : {maneira_1['estado civil']}')
print(f'estado civil no dicionário 2 : {maneira_2['estado_civil']}')

### A maneira  1 é a mais utilizada

pessoa = {
    'nome': 'Kayky',
    'sobrenome': 'Lourenço',
    'idade': '21',
    'altura': '1,83',
    'endereços': [
        {'rua': 'Alfredo Descragnolly', 'numero': '385'},
        {'rua': 'tavares bastos', 'numero': '471'},
        ],
        }

print(pessoa['altura'])
print(pessoa['endereços'])
print(pessoa['idade'])

### Podemos usar o for na chave

for chave in pessoa:
    print(pessoa[chave] )

