#Criar um programa que faça o monitoramento de combustivel
#Perguntar a pessoa a distância percorrida (em km)
#Quantidade de combustivel gasto (em litros)
#O programa deve calcular o consumo_medio:
#< 8 = Alto consumo
#8 – 12 = Consumo moderado
#> 12 = Econômico
#Dizer o resultado final com: alto consumo, cxonsumo moderado, econômico

input(consumo_medio = distancia / litros)
print("Digite a distância percorrida (em km):" )
print('---------------------------------------------------------')
print("Digite a quantidade de combustivel gasto (em litros):")
print("------------------------------------------------------------")

if consumo < 8  
print('Auto consumo')

elif consumo 8 - 12
print('Consumo moderado')

else consumo > 12 
print('Econômico')

