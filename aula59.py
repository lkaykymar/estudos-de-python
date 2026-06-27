'''
Argumentos nomeados = tem nome com sinal de igual
Argumentos não nomeados = não tem nome, recebe apenas o argumento (valor), posicionais
'''

### Definição da função
### Aqui temos dois parâmetros
def soma(x, y):
    print(x + y)

print(soma) # Aqui ele ta lendo o nome da função apenas

print(soma(1,2)) # Retorna a soma e o que normalmente uma função retorna, none

soma(1, 9) # Aqui estamos passando argumentos posicionais, dependem da posição dos parâmetros

### Aqui provo que o argumento é posicional, pois a ordem influencia no resultado
def divisao(x, y):
    print(f'{x=} e {y=}', '|', 'x / y =', x / y)

divisao(10, 5)
divisao(5, 10)

### Vamos usar argumentos nomeados para resolver tal problema

divisao(10, 5)
divisao(y=5, x=10) 

### Outro exemplo

def divisao_(x, y, z):
    print(f'{x=}, {y=} e {z=}', '|', '(x / y) * z  =', (x / y) * z)

divisao_(10, 5, 2)
divisao_(5, y=5, z=4) # A partir do momento que você coloca um argumento nomeado, todos os outro depois dele terão que estar nomeados
