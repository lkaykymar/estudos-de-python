# input serve pra extrair dados do usuário

nome = input("Qual o seu nome?\t")
print(f"O seu nome é {nome}")

#Voce pode converter o que o usuário inserir, já que sempre vem como str

num1 = int(input("Digite um número\t"))
num2 = int(input("Digite outro número\t"))
print(f"A soma dos números é: {num1 + num2}")

#Uma maneira mais inteligente é separar a conversão
#Permite que voce possa checar oq o usuário inseriu

numero1 = (input("Digite um número\t"))
numero2 = (input("Digite outro número\t"))

int_num1 = int(numero1)
int_num2 = int(numero2)
print(f"A soma dos números é: {int_num1 + int_num2}")