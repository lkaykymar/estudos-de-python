# Operador lógico NOT
# Serve pra inverter expressões
# not true = false
# not false = true

senha = input("Senha ")

if not senha: # Aqui deu no mesmo, mas o usuário não digitando nada, seria falso e o código não mostraria nada, o not faz ser verdadeiro
    print("Você não digitou nada")

print(not 0)
print(not 1)
