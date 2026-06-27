'''
Valores padrão para parâetros
ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para parâmetro, o valor padrão será
usado.
refatorar: editar seu código
sempre que criar um valor padrão para o parâmetro, os parâmetros seguintes precisarão de um valor padrão também
'''

# caso não tenha valor pra z, será usado o 0, evitando bugs
def soma (x, y, z=0):
    if z:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 3)
soma(3, 3)
soma(7, 3)

# zero é considerado false, então a primeira condição não vai ser atendida, apesar de ter um valor pra z
soma(2, 3, 0)

# Vamos usar o is not none
def soma_(x, y, z=None): 
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma_(5, 3, 0)
soma_(y=5, z=0, x=3)

