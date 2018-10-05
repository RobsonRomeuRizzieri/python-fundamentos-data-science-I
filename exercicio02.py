#declarando um váriavel que recebe em seu valor a velocidade da luz em metros por segundo
speed_of_light = 299792458
#imprimindo a velocidade da luz em metros por segundo
print speed_of_light
#imprimindo a velocidade da luz em centimetros por segundo
print speed_of_light * 100
# variavel que recebe um bilionésimo que é 1 dividade por 1 bilhão
bilhao = 1.0 / 1000000000
#tamanho do nanostick em metros
nanostick = speed_of_light * bilhao
#tamanho do nanostick em centimetros
nanostick = speed_of_light * bilhao * 100
# O resultado é 29.9792458
print nanostick

#definição de ciclos por segundo de um processador
#Adicionado o ponto para quando dividir por essa variavel ter o resultado exato
cycles_per_second = 2700000000. #Essa é a velocidade de 2.7GHz do nosso processador

#Imprimir a distância em metros que aluz viaja em um ciclo do processador de 2.7GHz
cycle_distance = speed_of_light / cycles_per_second
#Resultado de 0.111034243704 que representa 0.11 metros ou 11 centimetros
print cycle_distance
# convertendo o resultado em centimetros
print cycle_distance * 100