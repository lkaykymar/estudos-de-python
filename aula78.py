# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis(lista por exemplo);
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# sets removem naturalmente valores duplicados
s1 = {1, 2, 3, 3, 3, 3, 3, 3, 3, 1, 2}
print(s1)

# Se você tem uma lista com valores duplicados você pode remover usando set
lista = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8]
lista_set = set(lista)
print(lista_set)

# Imagina que o set é uma sacola que você vai jogando coisa
print(lista_set[0])