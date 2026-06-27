nome = "kayky"
altura = 183
peso = 81
imc = 6
imc_formatado = 66

print(nome,'possui', altura, 'cmn de altura, pesa' , peso, "kg e seu IMC é", imc_formatado)

'''com o f-strings, é possível formatar strings para ter as variáveis dentro dela de uma 
forma mais fácil'''
#lembrando que :.2f, serve pra delimetar as casas decimais e :,.f serve pra colocar vírgula
print(f'{nome} possui {altura:,.2f} de altura, {peso} de peso e um imc de {imc_formatado}')

#podemos fazer essa mesma formatação usando .format
print("{} possui {:,.2f} de altura, pesa {}kg e seu imc é {}".format(nome, altura, peso, imc_formatado))

#podemos usar os índices também
print("{2} possui {3:,.2f} de altura, pesa {0}kg e seu imc é {1}".format(nome, altura, peso, imc_formatado))

#podemos usar parâmetros também
print("{nome3} possui {nome4:,.2f} de altura, pesa {nome1}kg e seu imc é {nome2}".format(nome1=nome, nome2=altura, nome3=peso, nome4=imc_formatado))






