import pprint

# Vamos filtrar, esse if vem depois do for e não tem else
# O que vem na esquerda é mapeamento, na direita é filtro
lista = [n for n in range(10) if n < 5]
print(lista)

# Um filtro é o if que vem depois do for, para separar uma coisa da outra quando quiser
# pprint serve pra minupular a maneira como as coisas aparecerão no terminal
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30}
]

novos_produtos = [{**produto, 'preco': produto["preco"] * 1.05} 
                  if produto['preco'] > 20 else {**produto}
                  for produto in produtos
                  if produto['preco'] > 20]

print(*novos_produtos, sep='\n') 

p(novos_produtos)

