'''
Retorno de valores das funções (return)
No Python, o return é a forma de devolver um valor de dentro de uma função para quem a chamou.
Se você não usa return, a função executa o código, mas não devolve nada (por padrão retorna None)
'''

def soma(x, y):
    print(x + y)

# nesse momento, soma 1 não recebe o resultado de soma(2,2)
# pois por padrão, funções em python retornam None
soma1 = soma(2, 2)

print(soma1)

# Vamos resolver usando return

def multiplicacao(a, b):
    return a*b

resultado1 = multiplicacao(3, 3)

print(resultado1)



variavel = print('Kayky') 

# print não tem valor, é uma função que exibe algum valor
# O 'valor' padrão do print, é none
print(variavel)
print(variavel is None) 

def soma(x, y):
    if x > 10:
        return 10
    return (x + y) 

soma1 = soma(11, 2)
soma2 = soma(11, 2)
print(soma1 + soma2)