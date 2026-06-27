# Métodos úteis:
# add, update, clear, discard


# Adicionando elementos
s1 = set()
s1.add("Kayky")
s1.add("Martins")
print(s1)

# update adiciona também mas de forma iterável, portando use tupla
s1.update(("Lourenço", 1, 2, 3, 4, 5))
print(s1)

# Para remover um item do set
s1.discard(("Kayky", "Lourenço"))
print(s1)

# Limpa o set
s1.clear()
print(s1)