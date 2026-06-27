'''
Flag (Bandeira) - Marcar um local
none = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
algoritmo -> Solução que você cria pra um problema
'''
condicao = False # Isso aqui que define o resultado final
passou_no_if = None

if condicao:
    passou_no_if = True #temos uma bandeirinha fincada aqui e usamos o nome pra falar se a bandeira esta fincada ou não
    print(' Faça algo')
else: 
    print('Não faça algo')

if passou_no_if is None:
    print('NÃO PASSOU NO IF')

if passou_no_if is not None:
    print("PASSOU NO IF")

# Isso vai servir pra quando voce tiver um código grande e querer saber se ele passou em algum lugar