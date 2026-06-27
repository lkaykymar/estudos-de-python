'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
# args é usado pra quando tem muitos parâmetros
# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for i in args:
        print('Total', total)
        total += i
        print('Total', total)

soma(1, 2, 3, 4, 5)