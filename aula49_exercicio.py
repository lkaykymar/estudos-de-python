'''
Faça uma lista de compras com listas
O usuário deve ter a ossibilidade de inserir, apagar e listar valores da sua lista
não permita que o programa quebre com erros de índices inexistentes na lista
'''
lista_compras = ['morango', 'feijão', 'arroz']

while True:
    print('Menu')
    comando_ = input('[I]nserir, [A]pagar, [F]inalizar: ')
    comando = comando_.lower()

    if comando == 'i':
        item_inserir = input('Digite o item que deseja inserir ')
        lista_compras.append(item_inserir)
        for indice, nome in enumerate(lista_compras, start = 1):
            print(indice, nome)

    if comando == 'a':
        item_apagar = int(input('Digite o numero correspondente ao item que deseja apagar ')) 
        item_apagar -= 1
        if not lista_compras:
            print("LISTA VAZIA")
            continue
            
        if not len(lista_compras) > item_apagar:
            print('ITEM INEXISTENTE')
            continue
        else:
            lista_compras.pop(item_apagar)
            for indice, nome in enumerate(lista_compras, start = 1): 
                print(indice, nome)
    
    if comando == 'f':
        print("LISTA FINALIZADA")
        for indice, nome in enumerate(lista_compras, start = 1):
            print(indice, nome)
        break

##### SOLUÇÃO DO OTÁVIO (BEM MAIS SIMPLES RSRS)

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
        
        




       
    

    
        
         
    
    
