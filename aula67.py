'''
Hgher order functions
funções de primeira classe
as funções em python podem ser tratados como qualquer outro tipo de dado
'''

"""
Higher Order Functions
Funções de primeira classe
Funções é um tipo de dado, você pode jogar em uma variável por exemplo
"""

"""
No Python (e em várias linguagens), uma função de ordem superior é uma função que pode receber 
outra função como argumento e/ou pode retornar uma função como resultado.
"""

'''
Uma HOF é simplesmente uma função que trabalha com funções.
'''

### Função recebendo outra função como parâmetro:
def executa(funcao, *args):
    return funcao(*args)

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def quadrado(x):
    return x * x

print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Maria'))
print(executa(quadrado, 5))

### Função que retorna outra função
# multiplicador(fator) cria uma função que multiplica qualquer número pelo fator.
# O que multiplicador retorna é a função interna que faz essa multiplicação.
# dobro e triplo são funções criadas dinamicamente usando multiplicador.

def multiplicador(fator):
    def interna(x):
        return x * fator
    return interna

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(10))   # 20
print(triplo(10))  # 30
