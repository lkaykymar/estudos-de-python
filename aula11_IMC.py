nome = input("Digite o nome\n\n")
altura = float(input("Digite a altura em cm\n\n"))/100
peso = float(input("Qual o peso?\n\n"))
imc = int(peso/altura ** 2)
imc_formatado = format(imc,".2f")

print(nome,'possui', altura, 'cmn de altura, pesa' , peso, "kg e seu IMC é", imc_formatado)