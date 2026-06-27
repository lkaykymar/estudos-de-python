# IF ---> Serve pra testar uma condição, se for verdadeira, ela executa o código.

quantidade = int(input("Quantas peças de roupa deseja?\t"))
if quantidade >= 20 and quantidade <= 30:
    preco_unidade = 28.00
if quantidade < 20:
    preco_unidade  = 35.00
if quantidade > 30:
    preco_unidade = 20.00

valor_total = preco_unidade*quantidade

print(f"A quantidade total de roupas é de {quantidade} unidades, \no valor por peça é de {preco_unidade} e o vaor total será {valor_total}")

print("\nQuantidade de peças:\t", quantidade)
print("\nValor por peça:\t", preco_unidade)
print("\nValor total:\t ", valor_total)

# IF ELSE ---> Serve pra testar uma condição, se for verdadeira, ela executa um código, se não, executa outro.

quantidade = int(input("Quantas peças de roupa voce deseja?\t ",))

if quantidade < 20:
    valor_unidade = 35
else:
    if quantidade >= 20 and quantidade <= 30:
        valor_unidade = 28
    else:
        valor_unidade = 20

valor_total = quantidade*valor_unidade

print(f"A quantidade de peças é {quantidade}, o valor por peça é de {valor_unidade} reais e o valor total é de {valor_total}reais ")

# #OUTRO EXEMPLO

código_produto = int(input("Digite o códio do produto.\t"))

if código_produto == 1:
    print(13.30)
else:
    if código_produto == 2:
        print(1.40)
    else:
        if código_produto == 3:
            print(19.00)
        else:
            if código_produto == 4:
                print(123.79)
            else:
                if código_produto == 5:
                    print(44.33)
                else:
                    print("Código inválido!")


#OUTRO EXEMPLO

temperatura = int(input("Qual a temperatura no momento?\t"))

if temperatura < 16:
    print("Frio!")
else:
    if temperatura >= 16 and temperatura <= 30:
        print("Agradável!")
    else:
        print("Quente!")
            
#OUTRO EXEMPLO

estação = str(input("Digite a presente estação.\t"))

if estação == 'primavera':
    print("setembro, outuro e novembro")
else:
    if estação == 'verão':
        print("dezembro, janeiro e fevereiro")
    else:
        if estação == 'outono':
            print("março, abril e maio")
        else:
            if estação == 'inverno':
                print("junho, julho e agosto")

# ELIF ---> Se o if for verdadeiro, executa o código, se não, 
# testa cada elif até encontrar um verdadeiro e executar o código.

código = int(input("Digite o código do produto!\t"))

if código == 1:
    print(13.30)
elif código == 2:
    print(1.40)
elif código == 3:
    print(19.00)
elif código == 4:
    print(123.79)
elif código == 5:
    print(44.33)
else:
    print("Código inválido!")

'''    if:
Se a condição for verdadeira, executa o código.
Se for falsa, não faz nada.

if + else:
Se a condição for verdadeira, executa um código.
Se for falsa, executa outro código.

if + elif:
Se a primeira condição (if) for verdadeira, executa.
Se não, o programa testa os elif (um por um) até encontrar um verdadeiro.
O elif faz novos testes — não executa algo só porque o if deu falso (diferente do else).

else:
É o último caso, executa se nenhum if ou elif for verdadeiro.'''
 