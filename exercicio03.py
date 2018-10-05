#Atribuições de varaiveis
#7 semanas de 7 dias têm 49 dias
days = 7 * 7
print days # Vai mostrar na tela 49
days = 48 #Não é mais 49 mas sim 48, que foi atribuido agora
print days
days = days - 1 #Agora o valor vai ser 48 - 1
#Vai imprimir 47
print days

# = é usado como atribuição
#segue exemplo
horas = 9 
horas = horas + 1
horas = horas * 2
# resultado vai ser 20
print horas


# qual o valor em segundos para as seguintes atribuições
minutos = minutos + 1
segundos = minutos * 60
#Vai apresentar um erro porque a variavel minutos não foi inicializa e está sendo somanda ao valor 1
print segundos

#Fazendo o código funcionar
minutos = 1
segundos = minutos * 60
print segundos

# total de dias vividos conforme a quantidade de anos
age = 7
days_in_year = 365.25

print age * days_in_year