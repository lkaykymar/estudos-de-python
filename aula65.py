x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total # return não exibe, apenas salva o valor, mande-o para uma variável

numeros = (1, 2, 3, 4, 5)
soma_ = soma(*numeros) # isso desempacota

print(f'Soma {soma_}')

# essa soma foi só para ver como o args funciona
# o sum ja soma tuplas
print(sum((1, 2, 3, 4, 5, 6, 7, 8, 8)))