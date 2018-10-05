#trabalhando com indexing de string
#'robson'[0] vai listar a letra 'r'
#Sempre lembrar que uma string é um sequencia de caracteres que inicia na posição zero
#'robson'[1+1] vali listar a letra 'b'

nome = 'robson' 
print nome[0] #vai listar a letra 'r'
print nome[1+1] #vai listar a letra 'b'

print nome[3:4] # vai listar as letras da posição 3 até a a 4 nesse caso a 4 casa não é listada.
print nome[3:] # vai imprimir da posição 3 até o final da string
print nome[:5] # vai imprimir desde o inicio até a quinta casa

#Vamos converter a primeira letra para maiusculo 
print 'R' + nome[1:]

#Se executar com um indice que não existe na strin vai dar erro
print nome[10]
#se executar dessa forma vai retornar vazio
print nome[10:]