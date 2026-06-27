'''
Operação ternária (condicional de uma linha)
<valor if <condição> else <outro valor>
'''
# Escrevendo if else em uma linha só
print('valor' if True else 'Outro valor')

# variável
condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

# variável
condicao = 10 == 11
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

# Para verificar um CPF
digito = 10
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

# Posso continuar fazendo ifs (apesar de não ser legal fazer isso)
print('valor' if True else 'Outro Valor' if True else 'Fim')