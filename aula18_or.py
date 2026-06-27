# Operador Lógico OR
# or - quaquer condição verdadeira avalia toda expressão como verdadeira
# são considerados falsy (que voce ja viu)
#0 0.0 '' false

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha ")

senha_permitida = "123456"
if (entrada ==  'E' or entrada =='e') and senha_digitada == senha_permitida: # and e or na mesma frase pode ficar ambígua
    print("Entrar")
else:
    print("Sair")

#Avaliação de curto circuito
print(True or False or '' or 'abc')

# O or pode ser usado como um if 
senha = input("Senha\t") or "Sem senha" # caso o  usuário não digite nada, ele executa a segunda parte
print(senha)