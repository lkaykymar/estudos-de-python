'''
Tipo tupla - Uma lista imutável
A lista é capaz de ser alterada pelos métodos
Quando você não vai alterar a lista, faça uma tupla
é só tirar os colchetes
'''

tupla = 'Kayky', 'lourenço', 'martins'
print(type(tupla))

# Tentando alterar uma tupla (errooo)
tupla = 'Kayky', 'lourenço', 'martins'
#tupla[0] = 'joaquim'
print(tupla)

# Os outro conceitos para lista se aplicam a tupla também
tupla = 'Kayky', 'Martins'
print(tupla[-1])

# Para ser mais específico, use parenteses
tupla = ('Kaky', 'Lourenço')
print(type(tupla))

# Você pode converter listas para tuplas
tupla = ['Kaky', 'Lourenço']
nomes = tuple(tupla)
print(type(tupla), type(nomes))
