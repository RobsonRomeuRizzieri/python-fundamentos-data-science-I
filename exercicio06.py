#obtendo a posição inicial da string contida em outra string
valor = 'Procurando por um valor aplicado para novo campos.'
#Nesse caso vai imprimir o valor 18 que é onde inicia a string procurada.
print valor.find('valor')
#vamos atribuir esse indice a uma variavel
indice = valor.find('valor')
#agora vamos reimprimir o texto somente apartir da palavra que encontramos
print valor[indice:]
#se procurar por uma string que não existe no texto de busca é retornado -1 
#Vale lembrar que diferencia letra maiuscula de minuscula
print valor.find('Robson')