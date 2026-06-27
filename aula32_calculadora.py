'''Calculadora com while'''
# lower deixa todas as letras inserias minúsculas
#starts with confere se ele iniciou com a letra que você quer

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None:
        print('Números inválidos')
        continue  # <- impede que o programa continue com valores inválidos

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) != 1:
        print("Digite apenas um operador")
        continue

    print('Realizando sua conta. Confira o resultado a seguir:')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        if num_2_float == 0:
            print('Não é possível dividir por zero.')
            continue
        print(num_1_float / num_2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
