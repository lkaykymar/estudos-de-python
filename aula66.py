'''
Exercícios com funções
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variável e mostre o valor da variável
'''
### MINHA RESOLUÇÃO

def multiplica(*args):
    contador = 1
    for i in args:
        contador *= i
    print(contador)
    
multiplica(3, 3, 3, 3)

'''
crie uma função que fala se um número é par ou ímpar
retorne se o número é par ou ímpar
'''
### MINHA RESOLUÇÃO

def par_impar(x):
    if x % 2 == 0:
        print(f'{x} é par')
    else:
        print(f'{x} é ímpar')

par_impar(14215164372754642)

### RESOLUÇÃO DO OTÁVIO

def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_ou_impar(5))



