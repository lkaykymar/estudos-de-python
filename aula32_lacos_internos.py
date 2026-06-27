qtd_linhas = 5
qtd_colunas = 5
 
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha = } {coluna = }')
        coluna += 1
    linha += 1

print('acabou')

# Equando a quantidade de linhas não atinge 5, ele entra no laço da coluna. 
# Enquanto a quantidade de colunas não atinge 5, ele escreve a linha em que está e a coluna
# Em seguida ele soma 1 na quantidade de colunas e vai repetindo o while das colunas até atingir 5
# Quando atinge 5 colunas, ele soma 1 na linha  e agora entra novamente no laço da coluna, mas como linha 2

''' Explicação reformulada:

Enquanto a quantidade de linhas ainda não atingiu 5, o código entra no laço da coluna.

Dentro do laço da coluna, enquanto a quantidade de colunas ainda não atingiu 5:

Ele escreve a linha atual e a coluna atual.

Em seguida, soma 1 à coluna e repete esse processo.

Quando a coluna atinge 5, o laço da coluna termina.

Agora, ele soma 1 na linha e recomeça o processo, mas com a linha seguinte e a coluna voltando para 1.

Esse ciclo continua até que a linha também atinja 5.

Ao final, o programa exibe "acabou".

'''