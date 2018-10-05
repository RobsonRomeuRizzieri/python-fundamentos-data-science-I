import main
#import studentMain
import password_generator
import random
# Use an import statement at the top
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    senha = ''
    i = 0
    while i < 3: 
        senha = senha + random.choice(word_list)
        i = i + 1    
    return senha

# Add your function here
# It should return a string consisting of three random words 
# concatenated together without spaces
print(generate_password())


#Alternativamente, você pode usar a função random.sample e o método .join para sequências de caracteres:

#def generate_password():
#    return str().join(random.sample(word_list,3))

#Para criar senhas aleatórias, usamos import random. A definição da função foi simplesmente:

#def generate_password():
#    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
