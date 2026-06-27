"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
'''Iterável é um elemento que tem um método chamado (como lower etc) de iter.
Se tem um método, então é um objeto  e tudo é objeto no python
'''
texto = iter('Kayky') #___iter___()
print(texto)
