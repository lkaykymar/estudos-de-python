'''
Introdução às funções (def) em python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)

'''
### PRIMEIRO EXEMPLO
def carrinho(): 
    print('Kayky')
    print('Kayky')
    print('Kayky')

carrinho() # Com uma linha, executei 3

### SEGUNDO EXEMPLO
def camelo(a, b, c): # Dentro desse parenteses, você pode colocar parâmetros, "variáveis", nesse caso: a, b, c
    print('numeros:', a, b, c) # argumentos são os valores em si
   
    
camelo(1, 2, 3) # A cada vez que você chama a função, você pode mudar os argumentos
camelo(4, 5, 6)

### TERCEIRO EXEMPLO
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao('kayky')
saudacao('mari')
saudacao('cicero')

### QUARTO EXEMPLO

def saudando(nome='Sem nome'):
    print(f'Olá, {nome}')

saudando('Kayky')
saudando()

