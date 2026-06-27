# Você escreve códigos para pessoas, não para computadores, existem boas práticas
# para torna-los compreensíveis para todos, mesmo que o código fique mais longo
# No python não há o conceito de variável constante, a qual você não pode mudar o valor
# Portanto, no python usamos letras maiúsculas para variáveis que não vão mudar
# Quando tem muito if, é difícil olhar e já entender, portanto evitamos muitas condições no mesmo if
# Complexidade não é bom, simples é mehor do que complexo



# **EXEMPLO COMPLEXO**

velocidade = 61 #velocidade atual do carro
local_carro = 100 #Local em que o carro está  na estrada

RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE) and \
velocidade > RADAR_1:
    print("Carro multado em radar 1")

# **TORNANDO MAIS SIMPLES E LEGÍVEL**
    
velocidade = 61 #velocidade atual do carro
local_carro = 100 #Local em que o carro está  na estrada

RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1 
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar')

if carro_passou_radar_1:
    print("Carro passou em radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")

    # As variáveis não resumem o código, elas dão nome para os trechos  do código, facilitando a leitura




