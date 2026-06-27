#Operadore Lógico AND

# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São consideradas falsy (que voce ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor, não existe


entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha ")

senha_permitida = "123456"
if entrada ==  'E' and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")
 

# Avaliação de curto circuito
print(True and True and True)
print(bool(0))
print(bool(0.0))
print(bool(''))
print(True and '' and True)